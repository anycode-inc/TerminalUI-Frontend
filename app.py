from flask import Flask, render_template, request
import requests as req

from docker.python_on_docker import python_on_docker

app = Flask("terminal_ui")

server_ip = "13.235.69.120"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    template = "menu.html"
    return render_template(template)

@app.route("/task")
def task():
    choice = request.args.get("choice")
    template = "menu.html"
    if choice == "1":
        contents = python_on_docker(server_ip)
        template = "response.html"
    else:
        template = "menu.html"
    return render_template(template, response=contents)
