import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from usage_schemes import schema_get_files_info, schema_get_file_content, schema_get_run_python_file, schema_write_file
from config import WORKING_DIRECTORY, AGENT_ITERATIONS


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info, 
            schema_get_file_content, 
            schema_get_run_python_file, 
            schema_write_file
            ],
    )

    user_prompt, options = handle_arguments(sys.argv)
    call_llm(client, user_prompt, available_functions, *options)

def handle_arguments(args):
    if len(args) < 2:
        handle_invalid_arguments()
    
    user_prompt = ""
    options = []

    
    for arg in args[1:]:
        if user_prompt == "" and not arg.startswith("--"):
            user_prompt = arg
        elif arg.startswith("--"):
            options.append(arg)
        else:
            handle_invalid_arguments()
   
    return user_prompt, options

def handle_invalid_arguments():
        print("Error: Usage is main.py 'prompt' optional-arguments.")
        print(
                "Valid arguments:\n"
                "   --verbose : outputs user prompt and token usage to console\n"
                "   --bypass : bypasses llm-usage (avoids using tokens while testing)"
            )
        sys.exit(1)
            
def call_llm(client, user_prompt, available_functions, *args):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    verbose = False
    if "--verbose" in args:
        verbose = True
    
    for i in range(0, AGENT_ITERATIONS):   
        if "--bypass" in args:
            response_text = "test-response"
            prompt_token_count = 0
            candidates_token_count = 0
        else:
            try:
                response = client.models.generate_content(
                    model='gemini-2.0-flash-001', 
                    contents=messages,
                    config=types.GenerateContentConfig(
                        tools=[available_functions], 
                        system_instruction=system_prompt
                        ),
                )
                prompt_token_count = response.usage_metadata.prompt_token_count
                candidates_token_count = response.usage_metadata.candidates_token_count
                response_function_calls = response.function_calls
                response_text = response.text
            except Exception as e:
                response_function_calls = None
                print(f"Error: Failed to generate agent response with error: {e}")

            function_result_parts = []
            if response_function_calls is not None:
                for function_call in response_function_calls:
                    function_call_result = call_function(function_call, verbose)
                    try:
                        dummy = function_call_result.parts[0].function_response.response
                        function_result_parts.append(function_call_result.parts[0])
                        if verbose:
                            print(f"-> {function_call_result.parts[0].function_response.response}")
                    except Exception as e:
                        raise Exception("Fatal error: function_result.parts[0].function_response.response attribute is missing.")

        if verbose:
            print(
                f"User prompt: {user_prompt}\n"
                f"Prompt tokens: {prompt_token_count}\n"
                f"Response tokens: {candidates_token_count}"
            )

        try:
            print(f"Agent Response: {response_text}")

            has_function_call = False
            for candidate in response.candidates:
                messages.append(candidate.content)
                for part in candidate.content.parts:
                    if part.function_call is not None:
                        has_function_call = True
                    #print(f"FUNCTION CALL: {part.function_call}")
            messages.append(
                types.Content(role="user", parts=function_result_parts),
            )
        except Exception as e:
            print(f"Error: Could not append candidate to messages. Is response.candidates undefined? {e}")

        #can potentially lead to fatal error if agent response failed to generate
        if response_text and not has_function_call:
            print(f"Agent finished after {i + 1} iterations.")
            break
      
def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    try:
        function_result = function_name[function_call_part.name](WORKING_DIRECTORY, **function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )


if __name__ == "__main__":
    main()

