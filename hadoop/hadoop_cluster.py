import requests as req

def create_hadoop_cluster(server_ip, namenode_ip, namenode_port, namenode_directory, datanode_ip, datanode_directory):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/hadoopCluster/hadoop.py?namenode_ip={namenode_ip}&namenode_port={namenode_port}&namenode_directory={namenode_directory}&datanode_ip={datanode_ip}&datanode_directory={datanode_directory}"
    res = req.get(url)
    contents = res.text
    return contents