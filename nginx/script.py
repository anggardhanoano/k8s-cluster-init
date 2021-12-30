import os
import re

lines_after_ip_upstream = ['      }\n', 
                            '\n', 
                            '      server {\n', 
                            '        listen 80;\n', 
                            '\n', '        location / {\n', 
                            '          proxy_pass http://nodes;\n', 
                            '        }\n', 
                            '      }\n', 
                            '    }']

def main():
    four_tab = " " * 8
    nginx_file = open("configMap.yaml", "r")
    list_of_lines = nginx_file.readlines()
    nginx_file.close()
    
    os.system("kubectl get nodes --selector='!node-role.kubernetes.io/master' -o wide --no-headers | awk '{print $6}' > ip.txt")
    
    ip_line = open("ip.txt", "r")
    list_of_ip = ip_line.readlines()
    for idx, ip in enumerate(list_of_ip):
        list_of_ip[idx] = four_tab + f"server {ip.strip()}:30001 max_fails=1 fail_timeout=60s;\n"
    ip_line.close()
    os.remove("ip.txt")
    
    list_of_lines = list_of_lines[0:10] + list_of_ip + lines_after_ip_upstream
    
    nginx_file = open("configMap.yaml", "w")
    nginx_file.writelines(list_of_lines)
    nginx_file.close()

main()
