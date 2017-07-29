#getpass will not display password
from getpass import getpass
#ConnectionHandler is the function used by netmiko to connect to devices
from netmiko import ConnectHandler

#create variables for username and password
uname = input("Username: ")
passwd = getpass("Password: ")
cmds = input("Enter file name of configuration file: ")
hostfile = input("Enter the name of file that has the devices: ")

#This will allow you to just press enter
#This sets default values Not recommanded in any place but a lab
if len(uname) < 1 : uname = "automate"
if len(passwd) < 1 : passwd = "automation"
if len(cmds) < 1 : cmds = "commands.txt"
if len(hostfile) < 1 : hostfile = "devices.txt"

#with is used to open and automatically close files
#The commands.txt has all configuration commands
#To view status use the do + show command
with open(cmds) as f:
    cmds_to_send = f.read().splitlines()

with open(hostfile) as f:
    devices = f.read().splitlines()


#use a for loop to iterate through the devices
for device in devices:
    device_ip = device
    ios_rtr = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": uname,
        "password": passwd,
        }

    #connect to the device via ssh
    net_connect = ConnectHandler(**ios_rtr)
    #print the device IP to identify which device is being configured
    print(device_ip)
    #this variable is used to capture the output of cmds sent to device
    output = net_connect.send_config_set(cmds_to_send)
    #print the output
    print(output)

