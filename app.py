from flask import Flask,request,render_template,jsonify  #importing the falsk
import json
app=Flask(__name__)

@app.route('/')    #creating route(way) for welcome page or home page 
def welcome():         # method or defination
    return "welcome to falsk"   # for the message 

@app.route('/cal',methods=["GET"])  #route for calculator and also mehtod get as well   
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    #all the operation and results 
    if operation=='add':
        results=int(number1)+int(number2)
    elif operation=='mul':
        results=int(number1)*int(number2)
    elif operation=='divi':
        results+int(number1)/int(number2)
    else:
        results=int(number1)-int(number2)
    return jsonify(results)
    #for run the file to create the starting point 
if __name__=='__main__':
    app.run()  # flask run 5000 code of program 