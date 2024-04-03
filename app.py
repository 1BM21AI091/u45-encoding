from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store messages uploaded by users
messages = []

# Encoding mapping
label_mapping = {
    'A': '4',
    'B': '13',
    'E': '3',
    'G': '6',
    'H': '#',
    'I': '1',
    'O': '0',
    'R': '12',
    'S': '5',
    'T': '+',
}

# Decoding mapping (reverse of encoding mapping)
reverse_mapping = {value: key for key, value in label_mapping.items()}

# Function to encode a message
def encode_message(text):
    return ''.join(label_mapping.get(char.upper(), char) for char in text)

# Function to decode a message
def decode_message(text):
    return ''.join(reverse_mapping.get(char, char) for char in text)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']
        encoded_message = encode_message(message)
        messages.append({'user': 'Guest', 'message': encoded_message})
        return redirect(url_for('home'))
    return render_template('index.html', messages=messages)

@app.route('/decode/<message>', methods=['GET'])
def decode(message):
    decoded_message = decode_message(message)
    return render_template('decoded.html', decoded_message=decoded_message)

if __name__ == '__main__':
    app.run(debug=True)
