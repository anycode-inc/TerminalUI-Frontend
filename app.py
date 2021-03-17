from flask import Flask, render_template, request
import requests as req

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
        url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/docker.py?x=python"
        res = req.get(url)
        contents = res.text
        template = "docker.html"
    else:
        template = "menu.html"
    return render_template(template, response=contents)

