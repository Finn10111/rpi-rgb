from flask import Flask, render_template
import socket
import os
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/color/<color>', methods=['POST'])
def color(color):
    socket_path = '/var/www/vhosts/rgb.local/rgb_socket'
    if os.path.exists(socket_path):
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client.connect(socket_path)
        client.sendall(color.encode())
        client.close()
        return (json.dumps({'success': True}),
                200,
                {'ContentType': 'application/json'})
    else:
        return (json.dumps({'success': False}),
                500,
                {'ContentType': 'application/json'})


if __name__ == "__main__":
    app.run()
