from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_message', methods=['POST'])
def save_message():
    message = request.form['message']
    with open('message.txt', 'a') as f:
        f.write(message)
    return 'Message saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
