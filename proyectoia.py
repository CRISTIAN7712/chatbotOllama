import ollama
import time

messages = [
    {
        'role': 'user',
        'content': 'Escribe una historia para un videojuego de supervivencia en español',
    },
]

try:
    print("Iniciando la solicitud a Ollama...")
    start_time = time.time()
    response = ollama.chat(model='llama3.1:latest', messages=messages)
    end_time = time.time()
    print("Solicitud completada.")
    print("Tiempo de respuesta: {:.2f} segundos".format(end_time - start_time))
    print(response['messages']['content'])

except Exception as e:
    print(f"Error al obtener la respuesta: {e}")
