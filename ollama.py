import pandas as pd
import requests
import json

df = pd.read_excel("input.xlsx", 'small')
df = df.map(lambda x: x.replace('\n', ' ') if isinstance(x, str) else x)
df = df.rename(columns=lambda x: "" if str(x).startswith("Unnamed") else x)
df_csv = df.to_csv(index=False).strip()

prompt = f"""
У тебя есть CSV с данными:

{df_csv}

Преврати его в JSON массив объектов с полями:
- subject (регион)
- year (год)
- month (месяц, если есть)
- day (день, если есть)
- value (число на пересечении региона и периода)

Выведи только валидный JSON (полностью), без объяснений.
"""

payload = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False,
    # "options": {
    #     "temperature": 0.0,  # максимально детерминированный вывод
    #     "num_ctx": 16000
    # }
}

url = "http://localhost:11434/api/generate"

response = requests.post(url, json=payload)
print(response.json()["response"])


# import tiktoken

# enc = tiktoken.get_encoding("cl100k_base")  # универсальная кодировка (OpenAI-like)
# tokens = enc.encode(prompt)

# print("Tokens:", len(tokens))