#!usr/bin/env python3
from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/upload/', methods=['GET'])
def upload():
    # content = request.get_json()
    # print(content)
    # print(type(content))
    pass



if __name__ == '__main__':
    app.run(debug=True)
