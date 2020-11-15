from mail.mailer import Mailer
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route("/mail", methods=['POST', 'GET'])
def mail():
    if request.method == "POST":
        if request.is_json():
            data = request.get_json()
            mailer = Mailer(data[0], data[1], data[2], data[3])
            response = mailer.send()
            return make_response(jsonify(response))
        else:
            return make_response(jsonify('No input detected.'))
    elif request.method == "GET":
        return 'Thank you for your interest in the site! Mailer is online.'


if __name__ == '__main__':
    app.run(port=8080)
