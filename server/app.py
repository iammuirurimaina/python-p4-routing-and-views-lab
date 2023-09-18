#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
   
    print (parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    num = ""
    for i in range(parameter):
        num += '/n' + str(i)
    return '<p>n + num</p>'
    

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            abort(400, description="Division by zero is not allowed.")
    elif operation == '%':
        result = num1 % num2
    else:
        abort(400, description="Invalid operation.")
    
    return str(result)
    


    

 
        


if __name__ == '__main__':
    app.run(port=5555, debug=True)
