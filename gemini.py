from google import genai

client = genai.Client(api_key="API_key")

def ask_gemini(user_text):
    prompt = f"""
    You are a helpful Telugu government assistant.
    Respond ONLY in Telugu.

    User: {user_text}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
