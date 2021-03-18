from flask import Flask, render_template, request
import requests as req

from docker.python_on_docker import python_on_docker
from docker.httpd_on_docker import httpd_on_docker
from hadoop.hadoop_cluster import create_hadoop_cluster
from kubernetes.kubernetes_cluster import configure_kube_master, configure_kube_slave

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
    elif choice == "2":
        template = "docker/httpd_docker.html"
    elif choice == "3":
        template = "hadoop/hadoop_cluster.html"
    elif choice == "4":
        template = "kubernetes/kubernetes_cluster.html"
    else:
        template = "menu.html"
    return render_template(template)

@app.route("/httpd-on-docker")
def httpd_docker():
    image_name = request.args.get("image-name")
    contents = httpd_on_docker(server_ip, image_name)
    template = "response.html"
    return render_template(template, response=contents)

@app.route("/create-hadoop-cluster")
def hadoop_cluster():
    namenode_ip = request.args.get("namenode-ip")
    namenode_port = request.args.get("namenode-port")
    namenode_directory = request.args.get("namenode-directory")
    datanode_ip = request.args.get("datanode-ip")
    datanode_directory = request.args.get("datanode-directory")
    contents = create_hadoop_cluster(server_ip, namenode_ip, namenode_port, namenode_directory, datanode_ip, datanode_directory)
    template = "response.html"
    return render_template(template, response=contents)

@app.route("/configure-kubernetes-master")
def config_kube_master():
    pod_network_cidr = request.args.get("pod-network-cidr")
    owner = request.args.get("owner")
    group = request.args.get("group")
    contents = configure_kube_master(server_ip, pod_network_cidr, owner, group)
    template = "response.html"
    return render_template(template, response=contents)

@app.route("/configure-kubernetes-slave")
def config_kube_slave():
    kube_join_command = request.args.get("kube-join-command")
    contents = configure_kube_slave(server_ip, kube_join_command)
    template = "response.html"
    return render_template(template, response=contents)