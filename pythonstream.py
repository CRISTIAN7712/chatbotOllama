import ollama

messages = [{'role':'user','content':"""Escribe un articulo sobre desarrollo de software optimizado para SEO, con un titulo aleatorio de unas 2500 palabras"""}]

stream = ollama.chat(model='llama3.1:latest', messages=messages, stream=True)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)