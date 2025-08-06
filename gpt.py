"""Wrapper around the OpenAI chat completion API.

The project previously relied on the deprecated ``openai.ChatCompletion`` API
which was removed in ``openai`` 1.x.  The modern library exposes a client class
that manages configuration and authentication.  This module now uses that
``OpenAI`` client to perform chat completion requests.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(system_prompt: str, user_input: str) -> str:
    """Send a chat completion request to the OpenAI API.

    Parameters
    ----------
    system_prompt: str
        Text used to prime the assistant with role instructions.
    user_input: str
        Content supplied by the user.

    Returns
    -------
    str
        Assistant response or an error message if the request failed.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.4,
        )
        return response.choices[0].message.content
    except Exception as e:  # pragma: no cover - used for runtime resilience
        return f"Ошибка GPT: {e}"
