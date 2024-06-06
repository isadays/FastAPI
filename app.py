import os
from flask import Flask

APP = Flask(__name__)



@APP.route('/')
def say_hello():
    name = os.environ["Name"]
    return f"Hello {name} \n"



if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, debug = True)


