from google import genai

client = genai.Client(api_key="AIzaSyBfpCvz_CcuU2Tocaq7yAi0V8sd2p-lNMM")

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
