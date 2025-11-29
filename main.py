import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model_name = "gemini-2.0-flash-001"
system_prompt = """
Do whatever you think would solve the problem. The calculator is in "calculator/" directory. Try your best to use the tools at hand to access the files needed.
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="The prompt to generate content for")
    parser.add_argument("--verbose", action="store_true", help="Print verbose output")
    args = parser.parse_args()

    user_prompt = args.prompt

    if args.verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
      types.Content(role="user",
      parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(20):
        try:
            result = generate_content(client, messages, args.verbose)
            if result is not None:
                print(result)
                break
        except Exception as e:
            print(f"Error generating content: {e}")


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls and response.text:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)

        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    message_function_call = types.Content(
        role="user",
        parts=function_responses
    )

    messages.append(message_function_call)

    # return function_responses
    return None

if __name__ == "__main__":
    main()
