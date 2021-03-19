import requests as req

def launch_ec2_instance(server_ip, image_id, instance_type, count, subnet_id, security_group_id, key_name):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/aws/aws_auto_ha.py?x=launch_instance&image_id={image_id}&instance_type={instance_type}&count={count}&subnet_id={subnet_id}&security_group_id={security_group_id}&key_name={key_name}"
    res = req.get(url)
    contents = res.text
    return contents

def create_ebs_volume(server_ip, availability_zone, volume_type, size, key, value):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/aws/aws_auto_ha.py?x=create_ebs_volume&availability_zone={availability_zone}&volume_type={volume_type}&size={size}&key={key}&value={value}"
    res = req.get(url)
    contents = res.text
    return contents

def attach_ebs_volume(server_ip, volume_id, instance_id, device_name):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/aws/aws_auto_ha.py?x=attach_ebs_volume&volume_id={volume_id}&instance_id={instance_id}&device_name={device_name}"
    res = req.get(url)
    contents = res.text
    return contents

def upload_to_s3_bucket(server_ip, local_file_location, s3_bucket_location, acl):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/aws/aws_auto_ha.py?x=upload_to_bucket&local_file_location={local_file_location}&s3_bucket_location={s3_bucket_location}&acl={acl}"
    res = req.get(url)
    contents = res.text
    return contents

def create_cloudfront_distribution(server_ip, bucket_name, default_root_object):
    url = f"http://{server_ip}/cgi-bin/TerminalUI-CGI/aws/aws_auto_ha.py?x=create_distribution&bucket_name={bucket_name}&default_root_object={default_root_object}"
    res = req.get(url)
    contents = res.text
    return contents