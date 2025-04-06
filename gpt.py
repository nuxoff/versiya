import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_version_text(choice: str) -> str:
    prompt = f"""Пользователь выбрал: {choice}.
Сгенерируй креативное, вдохновляющее и немного юмористическое описание его "версии себя".
Пример:
Версия 3.7 "Улыбка сквозь шторм" - человек, который пережил многое, стал сильнее, но остался светлым. Характер: рассудительный, немного дерзкий, но с добрым сердцем."""

    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()
