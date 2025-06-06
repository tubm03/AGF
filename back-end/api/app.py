from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Cấu trúc dữ liệu tin nhắn
messages = []
typing_users = set()

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "status": "success",
        "message": "Backend is running",
        "timestamp": datetime.now().isoformat()
    })

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')
    emit('messages', messages)
    update_typing_status()

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')
    if request.sid in typing_users:
        typing_users.remove(request.sid)
        update_typing_status()

@socketio.on('new_message')
def handle_new_message(data):
    try:
        message = {
            'id': len(messages) + 1,
            'text': data['text'],
            'user': data['user'],
            'timestamp': datetime.now().isoformat()
        }
        messages.append(message)
        emit('new_message', message, broadcast=True)
        
        # Reset typing status
        if request.sid in typing_users:
            typing_users.remove(request.sid)
            update_typing_status()
            
    except KeyError as e:
        print(f"Invalid message format: {e}")

@socketio.on('user_typing')
def handle_user_typing(typing):
    try:
        if typing:
            typing_users.add(request.sid)
        elif request.sid in typing_users:
            typing_users.remove(request.sid)
        update_typing_status()
    except Exception as e:
        print(f"Typing error: {e}")

def update_typing_status():
    is_typing = len(typing_users) > 0
    emit('user_typing', is_typing, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)