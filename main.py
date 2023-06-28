from flask import Flask, Response, jsonify, render_template
from queue import Queue
from datetime import datetime
from config import SERVER_URL

app = Flask(__name__)
event_queue = Queue()

cnt = 0

@app.route('/stream')
def get_pushes():
    def event_stream():
        while True:
            data = event_queue.get()
            yield data
    
    return Response(event_stream(), mimetype="text/event-stream")

@app.route('/call')
def get_call():
    global cnt
    cnt += 1
    timestamp = datetime.now().strftime("%y/%m/%d %H:%M:%S")
    event_queue.put(f'data: {cnt} {timestamp}\n\n')
    return jsonify({'status': 'ok', 'timestamp': timestamp})

@app.route('/')
def main():
    return render_template('index.html', SERVER_URL=SERVER_URL)

@app.route('/bell')
def bell():
    return render_template('bell.html', SERVER_URL=SERVER_URL)

if __name__ == '__main__':
    app.run()