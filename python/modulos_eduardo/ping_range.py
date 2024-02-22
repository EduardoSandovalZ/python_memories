import os

def ping_range(first_ip,last_ip,num_paquets):

    ip_range = '.'.join(first_ip.split('.')[:3])+'.'
        
    first_ip = int(first_ip.split('.')[-1])
    last_ip = int(last_ip.split('.')[-1])
    
    ping_list = []
    not_ping_list= []
    
    for ip in range(first_ip,last_ip+1):
        full_ip = ip_range+str(ip)
        answer = os.system(f'ping -n {num_paquets} {full_ip}')
        
        if answer == 0:
            ping_list.append(full_ip)
        else:
            not_ping_list.append(full_ip)
            
    return ping_list,not_ping_list

lista1,lista2 = ping_range('142.250.189.1','142.250.189.5',2)