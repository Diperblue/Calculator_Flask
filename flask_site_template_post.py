from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template') # Cria o app pric

@app.route('/')
def index() -> 'html':
    return render_template('index.html',
                           First_h1="Calculator!!",)
@app.route('/calc.html', methods=['POST'])
def calc() -> 'html':
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    return render_template('calc.html',
                           num1=num1,
                           num2=num2,
                           result=num1+num2,)
app.run(debug=True)
