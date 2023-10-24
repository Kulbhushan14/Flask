from flask import Flask,request,render_template,jsonify
import json
app=Flask(__name__)

@app.route('/')

def welcome():
    return "welcome to falsk"

@app.route('/cal',methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=='add':
        results=int(number1)+int(number2)
    elif operation=='mul':
        results=int(number1)*int(number2)
    elif operation=='divi':
        results+int(number1)/int(number2)
    else:
        results=int(number1)-int(number2)
    return jsonify(results)

if __name__=='__main__':
    app.run()  # flask run 5000 code of program 