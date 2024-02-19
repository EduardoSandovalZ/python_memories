import os

def ping_range(first_ip,last_ip,num_paquets):
    first_ip = first_ip.split('.')
    ip_range = first_ip
    first_ip = int(first_ip[-1])

    num_paquets = 2
    ip_range.pop(-1)
    ip_range = '.'.join(ip_range)+'.'

    last_ip = last_ip.split('.')
    last_ip = int(last_ip[-1])

    ping_list = []
    not_ping_list= []
    
    for ip in range(first_ip,last_ip+1):
        answer = os.system(f'ping -n {num_paquets} {ip_range+str(ip)}')
        if answer == 0:
            ping_list.append(ip_range+str(ip))
        else:
            not_ping_list.append(ip_range+str(ip))
    return ping_list,not_ping_list






        

    



