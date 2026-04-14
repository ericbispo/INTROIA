import google.generativeai as genai
import os

# Configure sua chave aqui
genai.configure(api_key="AIzaSyCuUKYS8qRbeY0KFuwQcFKXGFmiei4i3lw")

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Explique o que é recursividade em programação de forma simples.")

print(response.text)