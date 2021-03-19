import requests as req

def run_command(command):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/command.py?command={command}"
    res = req.get(url)
    contents = res.text
    return contents