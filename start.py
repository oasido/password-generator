# gemaakt door ofek asido
# asido.ofek@gmail.com
# augustus 2021

from flask import Flask, render_template, request
import random

app = Flask(__name__)

#########
# pass generation:
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{}<>:;,.?!@#$%^&*_+"


#########

@app.route('/')
def home():
 return render_template('index.html', length=10)

@app.route('/', methods=['POST'])
def generate():
    length = request.form.get('length')
    
    form_uppercase = request.form.get('form_uppercase')
    form_lowercase = request.form.get('form_lowercase')
    form_symbols = request.form.get('form_symbols')
    form_numbers = request.form.get('form_numbers')

    upper, lower, syms, nums = True, True, True, True

    if form_uppercase == "on":
        upper = True
    else:
        upper = False
    
    if form_lowercase == "on":
        lower = True
    else:
        lower = False

    if form_symbols == "on":
        syms = True
    else:
        syms = False

    if form_numbers == "on":
        nums = True
    else:
        nums = False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols


    password  = "".join(random.choice(all) for i in range(int(length)))
    return render_template('index.html', password=password, length=length)


if __name__ == '__main__':
 app.run()
