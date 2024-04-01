from flask import Flask, render_template, request

app = Flask(__name__)

label_mapping = {
    'A': '4',
    'B': '13',
    'C':'(',
    'D':'1 )',
    'E': '3',
    'G': '6',
    'H': '#',
    'I': '1',
    'O': '0',
    'R': '12',
    'S': '5',
    'T': '+',
}

def encode_message(text):
    return ''.join(label_mapping.get(char.upper(), char) for char in text)

def decode_message(text):
    reverse_mapping = {value: key for key, value in label_mapping.items()}
    return ''.join(reverse_mapping.get(char, char) for char in text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        message = request.form.get('message')
        
        if action == 'Encode':
            encoded_message = encode_message(message)
            return render_template('index.html', encoded_message=encoded_message)
        elif action == 'Decode':
            decoded_message = decode_message(message)
            return render_template('index.html', decoded_message=decoded_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
