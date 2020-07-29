import subprocess, json
from collections import OrderedDict

def execute_cmd(cmd):
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, error = pipe.communicate()
    return out.strip()

def host_details():
    host_name = execute_cmd('hostname')
    host_ip = execute_cmd('hostname -I')
    return host_name, host_ip

def out2json():
    host_name, host_ip = host_details()
    root = {}
    root['Node_Name'] = host_name
    root['Node_IP'] = host_ip
    root = OrderedDict(root)
    root.move_to_end('Node_Name', last=False)
    try:
        output = json.dumps(root, indent=4)
        return output
    except:
        return "Failed"

print(out2json())