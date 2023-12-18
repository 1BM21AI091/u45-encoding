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


def conv(label_mapping, x):
    result = ''
    for i in x:
        result += label_mapping.get(i, i)

    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        input_text = input_text.upper()
        output_text = conv(label_mapping, input_text)
        return render_template('index.html', output_text=output_text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
