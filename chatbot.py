import ollama
from flask import Flask, request, jsonify

app = Flask(__name__)
conversation_history = ""

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history
    data = request.get_json()
    user_input = data.get('message')
    
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    
    # Añadir el mensaje del usuario al historial de la conversación
    conversation_history += f"Usuario: {user_input}\n"
    
    # Generar respuesta usando el historial de conversación
    prompt = conversation_history + "Bot:"
    response = ollama.generate(model='llama3.1:latest', prompt=prompt)
    
    # Obtener la respuesta del bot
    bot_response = response['response']
    
    # Añadir la respuesta del bot al historial de la conversación
    conversation_history += f"Bot: {bot_response}\n"
    
    return jsonify({'response': bot_response})

@app.route('/reset', methods=['POST'])
def reset():
    global conversation_history
    conversation_history = ""
    return jsonify({'message': 'Conversation history reset'}), 200

if __name__ == '__main__':
    app.run(debug=True)
