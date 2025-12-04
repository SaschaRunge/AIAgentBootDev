import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from usage_schemes import schema_get_files_info, schema_get_file_content, schema_get_run_python_file, schema_write_file


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

    if "--bypass" not in args:
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
        response_text = response.text
        response_function_calls = response.function_calls
        if response_function_calls is not None:
            for function_call in response_function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")

    else:
        response_text = "test-response"
        prompt_token_count = 0
        candidates_token_count = 0

    if "--verbose" in args:
        print(
            f"User prompt: {user_prompt}\n"
            f"Prompt tokens: {prompt_token_count}\n"
            f"Response tokens: {candidates_token_count}"
        )

    print(response_text)
      
def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")


if __name__ == "__main__":
    main()

