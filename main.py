import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt, options = handle_arguments(sys.argv)
    call_llm(client, user_prompt, **options)

def handle_arguments(args):
    if len(args) < 2:
        print("Error: Usage is main.py 'prompt'.")
        print(
                "Valid arguments:" +
                "   - --verbose"
            )
        sys.exit(1)
    
    user_prompt = ""
    verbose = False
    for arg in args[1:]:
        if user_prompt == "" and not starts_with(arg, "--"):
            user_prompt = arg
        if arg == "--verbose" :
            verbose = True
   
    return user_prompt, {"verbose": verbose}
        
def starts_with(string, starting_characters):
    if(len(string) <= len(starting_characters)):
        return False
    else:
        return string[:2] == starting_characters
    
def call_llm(client, user_prompt, **kwargs):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    print(f"Verbose is: {'verbose' in kwargs}")

    sys.exit()

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

