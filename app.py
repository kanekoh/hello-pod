import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    """Say hello"""
    return socket.gethostname()

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
