import requests as req

def configure_kube_master(server_ip, pod_network_cidr, owner, group):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/kubernetesCluster/kubernetes_cluster.py?node=master&pod_network_cidr={pod_network_cidr}&owner={owner}&group={group}"
    res = req.get(url)
    contents = res.text
    return contents

def configure_kube_slave(server_ip, kube_join_command):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/kubernetesCluster/kubernetes_cluster.py?node=slave&kube_join_command={kube_join_command}"
    res = req.get(url)
    contents = res.text
    return contents