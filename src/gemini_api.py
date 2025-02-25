import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# Initialize the Gemini client
client = genai.Client(api_key=API_KEY)

def analyze_error(code: str, error_message: str) -> str:
    """
    Sends the code and error message to Gemini and retrieves a humanized explanation.
    """
    prompt = (
        f"You are an intelligent debugging assistant. A user has provided the following code and error message. "
        f"Please explain the cause of the error in simple terms, indicate where it occurs, and suggest how to fix it.\n"
        f"Code:\n{code}\n"
        f"Error Message:\n{error_message}\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text.strip() if response and response.text else "No analysis found."
    except Exception as e:
        return f"API request failed: {e}"