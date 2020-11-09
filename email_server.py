from mail.mailer import Mailer
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/mail", methods=['POST', 'GET'])
def mail():
    if request.method == "POST":
        data = request.get_json()
        mailer = Mailer(data['name'], data['email'], data['subject'], data['message'])
        response = mailer.send()
        return make_response(response)
    elif request.method == "GET":
        return 'Thank you for your interest in the site! Mailer is online.'

