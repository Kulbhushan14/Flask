from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')

def welcome():
    return "<h1>welcome to falsk</h1>"

@app.route('/cal',methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=='add':
        results=number1+number2
    elif operation=='mul':
        results=number1*number2
    elif operation=='divi':
        results+number1/number2
    else:
        results=number1-number2
    return results

if __name__=='__main__':
    app.run()  # flask run 5000 code of program 