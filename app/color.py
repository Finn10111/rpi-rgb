from flask import Blueprint
import socket
import os
import json


color_blueprint = Blueprint('color', __name__)


@color_blueprint.route('/color/<color>', methods=['POST'])
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
        return (json.dumps({
                'success': False,
                'message': 'socket not found'
                }),
                500,
                {'ContentType': 'application/json'})
