import os
from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()
api_key = os.environ.get("API_KEY")
print("Digite o assunto para ser gerado os exercicios")


subject = str(input())
persona_system= """Você deve criar 3 questões com o gabarito delas em formato de JSON 
                   a partir do tema relacionado a ciência da computação que o usuário digitar
                   as questões devem envolver conceitos de computação junto com o que está pedindo
                   
                   EXEMPLO DE INPUT
                      Grafos
                   EXEMPLO DE RESPOSTA
                      Pode envolver roteamento, ciclos em grafos e afins

                   EXEMPLO EM JSON

                   topic: Grafos,
                   questions:{
                    1: 'Pergunta sobre roteamento',
                    2: 'Pergunta sobre balanceamento',
                    3: 'Pergunta sobre ciclos'
                   },
                   answers:{
                    1:'Resposta da 1',
                    2: 'Resposta da 2',
                    3: 'Resposta da 3'
                   }
                   """

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("API_KEY"),
)

response = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=[
        {"role": "system", "content": persona_system},
        {"role": "user", "content": subject}
    ],
    temperature=0.7,  
    max_tokens=1500   
)

raw_content = response.choices[0].message.content.strip().strip("`").replace("json", "").strip()
output = json.loads(raw_content)

print("+-------------------------------------------------------+")
print("|                     QUESTÔES                          |")
print("+-------------------------------------------------------+")
print(output["topic"])

print("QUESTÃO 1")
print(output["questions"]["1"])

print("QUESTÃO 2")
print(output["questions"]["2"])

print("QUESTÃO 3")
print(output["questions"]["3"])

