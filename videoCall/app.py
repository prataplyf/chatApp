from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecretkey'
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app)

@app.route('/')
@cross_origin()
def index():
    return render_template("./ChatAppPage.html")

@socketio.on('myEvent')
def handle_my_custom_event(json):
    print('received somethihng: ' + str(json))
    socketio.emit('myResponse',json)


if __name__ == "__main__":
    socketio.run(app, debug=True)