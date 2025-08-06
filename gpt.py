import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(system_prompt, user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.4
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ошибка GPT: {e}"
