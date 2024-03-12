from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_message', methods=['POST'])
def save_message():
    message = request.form['message']
    messages.append(message)
    return 'Message saved successfully!'

@app.route('/messages')
def show_messages():
    return '<br><br><br>'.join(messages)

if __name__ == '__main__':
    app.run(debug=True)
