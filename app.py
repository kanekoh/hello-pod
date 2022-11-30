import os
import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    prefix = os.getenv('PREFIX', "sample")
    hostname = socket.gethostname()
    message = "{prefix:s} {hostname:s}"
    return message.format(prefix = prefix, hostname = hostname)

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
