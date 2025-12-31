from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # 安全密钥，随便写
socketio = SocketIO(app)

@app.route('/')
def index():
    # 渲染聊天室页面
    return render_template('chat.html')

# 监听名为 'send_message' 的事件
@socketio.on('send_message')
def handle_message(data):
    print(f"收到消息: {data}")
    # 将消息广播给所有人（包括发送者自己）
    emit('receive_message', data, broadcast=True)

if __name__ == '__main__':
    # 注意：启动方式变了，不再是 app.run，而是 socketio.run
    socketio.run(app, debug=True)