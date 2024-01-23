from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask import redirect, render_template ,request, url_for, flash,session
import requests
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')
    
@app.route('/send_test', methods = ["POST", "GET"])
def send_test():
    
    payload = json.dumps({
    "username": "mufaddalsr99@gmail.com",
    "password": "6$S9Czbw7d"
    })

    url = "http://127.0.0.1:5000/recive_test"

    response = requests.request("POST", url, data=payload)

    return 'HEllo'

@app.route('/recive_test', methods = ["POST", "GET"])
def recive_test():
    print('recive_test')
    data =  request.get_json(force=True)
    
    #data = request.json

    #data = request.values

    #data = request.form
    print(data)
    
    return f'{data}'



@app.route('/login/<x_swift_partner_user>',methods = ["POST"])
def user_login(x_swift_partner_user):
    
    url = "https://app.goswift.in/integrations/v2/auth/token/"
    url += x_swift_partner_user 

    payload = json.dumps({
    "username": "mufaddalsr99@gmail.com",
    "password": "6$S9Czbw7d"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    new_response = json.loads(response.text)

    if response.ok:
        return new_response
    else:
        return new_response, new_response["statusCode"]

@app.route('/order-list',methods = ["POST"])
def order_list():

    url = "https://app.goswift.in/integrations/order/list"
    header = {
        "Authorization":request.headers.get("Authorization"),
        "Content-Type":"application/json",
        "X-Swift-Partner-User":request.headers.get("X-Swift-Partner-User")
    }

    payload = json.dumps(request.get_json())
    
    response = requests.request("POST", url, headers=header, data=payload)
    print("dump")
    new_response = json.loads(response.text)
    print(type(new_response))
    if response.ok:
        return new_response
    else:
        return new_response, new_response["statusCode"]


@app.route('/order-confirm/<order_id>', methods = ["POST"])
def order_confirm(order_id):
    print("here")
    url = "https://app.goswift.in/integrations/order/confirm/"
    url += order_id
    header = {
        "Authorization":request.headers.get("Authorization"),
        "Content-Type":"application/json",
        "Accept": "application/json",
        "X-Swift-Partner-User":request.headers.get("X-Swift-Partner-User")
    }

    # payload = json.dumps(request.get_json())
    print("here")
    
    response = requests.request("POST", url, headers=header)
    new_response = json.loads(response.text)
    print(new_response)
    if response.ok:
        return new_response
    else:
        return new_response, new_response["statusCode"]


@app.route('/order-ship/<order_id>',methods = ["POST"])
def order_ship(order_id):

    url = "https://app.goswift.in/integrations/order/ship/"

    url += order_id
    header = {
        "Authorization":request.headers.get("Authorization"),
        "Content-Type":"application/json",
        "Accept": "application/json",
        "X-Swift-Partner-User":request.headers.get("X-Swift-Partner-User")
    }

    payload = json.dumps(request.get_json())
    
    response = requests.request("POST", url, headers=header, data=payload)
    new_response = json.loads(response.text)

    if response.ok:
        return new_response
    else:
        return new_response, new_response["statusCode"]

@app.route('/order-label',methods = ["POST"])
def order_label():

    # sendBlob = request.args.get('sendBlob', default = 1, type = int)
    url = "https://app.goswift.in/integrations/order/label?sendBlob=false"

    payload = json.dumps(request.get_json())

    header = {
        "Authorization":request.headers.get("Authorization"),
        "Content-Type":"application/json",
        "Accept": "application/json",
        "X-Swift-Partner-User":request.headers.get("X-Swift-Partner-User")
    }

    response = requests.request("POST", url, headers=header, data=payload)
    new_response = json.loads(response.text)

    if response.ok:
        return new_response
    else:
        return new_response, new_response["statusCode"]
      
if __name__ == '__main__':
  app.run(port=5000)
