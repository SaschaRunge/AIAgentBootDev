import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt, options = handle_arguments(sys.argv)
    call_llm(client, user_prompt, *options)

def handle_arguments(args):
    if len(args) < 2:
        handle_invalid_arguments()
    
    user_prompt = ""
    options = []
    for arg in args[1:]:
        if user_prompt == "" and not starts_with(arg, "--"):
            user_prompt = arg
        elif starts_with(arg, "--"):
            options.append(arg)
        else:
            handle_invalid_arguments()
   
    return user_prompt, options

def handle_invalid_arguments():
        print("Error: Usage is main.py 'prompt' optional-arguments.")
        print(
                "Valid arguments:\n" +
                "   --verbose"
            )
        sys.exit(1)
        
def starts_with(string, starting_characters):
    if(len(string) <= len(starting_characters)):
        return False
    else:
        return string[:2] == starting_characters
    
def call_llm(client, user_prompt, *args):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    if ("--verbose" in args):
        print(
            "\n\n\n"
            f"User prompt: {user_prompt}\n"
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
            f"Response tokens: {response.usage_metadata.candidates_token_count}"
        )

    print(f"\n\n")
    print(response.text)
    
    
    




if __name__ == "__main__":
    main()

