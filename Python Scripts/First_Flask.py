from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/page1')
def page1func():
    return 'Page 1 Data'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
