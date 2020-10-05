from flask import Flask, send_file

api = Flask(__name__)

@api.route("/", methods=["GET"])
def website():
    return open("index.html").read()

@api.route("/<fp>", methods=["GET"])
def websitedata(fp):
    try:
        return send_file(fp)
    except FileNotFoundError:
        print(fp, "non existent")
        return {"success":False}

api.run("0.0.0.0", 80)
