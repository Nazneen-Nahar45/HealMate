import google.generativeai as genai
import os
from flask import Blueprint, render_template, request, jsonify

# Set up API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDsnA-IxyZa5ekF9xwkwA91YmnKceJT-xs"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# ✅ Use Blueprint instead of Flask app
chatbot_blueprint = Blueprint('chatbot', __name__, template_folder='templates')

# Memory-based chat storage
chats = [{'name': 'New Chat', 'id': 1, 'messages': []}]

def ai_response(prompt, chat_history=None):
    if chat_history:
        context = "\n".join(
            [f"User: {msg['text']}" if msg['text'].startswith('User') else f"AI: {msg['text']}" for msg in chat_history]
        )
        prompt = f"{context}\nUser: {prompt}\nAI:"
    response = model.generate_content(prompt)
    return response.text

# Routes
@chatbot_blueprint.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@chatbot_blueprint.route("/get_chats", methods=['GET'])
def get_chats():
    return jsonify({'chats': chats})

@chatbot_blueprint.route("/get_chat_history", methods=['GET'])
def get_chat_history():
    chat_id = int(request.args.get('chat_id'))
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    return jsonify({'messages': chat['messages']}) if chat else jsonify({'messages': []})

@chatbot_blueprint.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_input = data.get('input')
    chat_id = data.get('chat_id')
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    chat_history = chat['messages'] if chat else []
    response = ai_response(user_input, chat_history)
    if chat:
        chat['messages'].append({'text': f'User: {user_input}'})
        chat['messages'].append({'text': f'AI: {response}'})
    return jsonify({'response': response})

@chatbot_blueprint.route('/new_chat', methods=['POST'])
def new_chat():
    data = request.get_json()
    chat_name = data.get('chat_name')
    new_chat_id = len(chats) + 1
    chat_data = {'name': chat_name, 'id': new_chat_id, 'messages': []}
    chats.append(chat_data)
    return jsonify({'status': 'Chat created successfully', 'chat_id': new_chat_id})

@chatbot_blueprint.route('/delete_chat', methods=['POST'])
def delete_chat():
    data = request.get_json()
    chat_id = data.get('chat_id')
    global chats
    chats = [chat for chat in chats if chat['id'] != chat_id]
    return jsonify({'status': f'Chat {chat_id} deleted successfully'})