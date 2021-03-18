import requests as req

def httpd_on_docker(server_ip, image_name):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/docker.py?x=httpd&image_name={image_name}"
    res = req.get(url)
    contents = res.text
    return contents