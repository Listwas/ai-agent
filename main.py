import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def get_response(user_prompt: str):
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
        return client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages
        )

def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("no prompt provided. aborting..")
        sys.exit(1)

    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv
    response = get_response(user_prompt)

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(response.text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    main()
