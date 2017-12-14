#!/usr/bin/python3
from getpass import getpass
from netmiko import ConnectionHandler

uname = input("Username: ")
passwd = getpass("Password: ")
cmd = input("Enter show commands separated by ',': ")
host = input("Enter the host IPs separate with space: ")

#host = """<Paste_host_list>"""

if len(uname) < 1: uname = "<default>"
if len(passwd) < 1: passwd = "<default>"

hosts = host.split()
cmds = cmd.split(",")
  
for ip in hosts:
    hp_rtr = {
        "device_type": "hp_procurve",
        "ip" : ip,
        "username" : uname,
        "password" : passwd,
        }
    try:
        net_connect = ConnectHandler(**hp_rtr)
    except Exception as unknown_error:
        print("************************************")
        print("Unable to log into this device:", ip)
        print(unknown_error)
        print("************************************")
        continue

    print("Connected to host: ", ip)
    for show_commands in cmds:
        output = net_connect.send_command(show_commands)
        print("Command issued:",show_commands)
        print(output)
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("End of configs for device", ip)
