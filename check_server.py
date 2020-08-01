"""
Rob Marchetti
Description: simple script to see if server or other host is up or not
"""

import platform
import subprocess


def is_alive(server_name):
    """
    Returns True if the server responds to a ping request.
    Remember that a server may not respond to a ICMP request, even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 aws.amazon.com"
    command = ['ping', param, '1', server_name]

    response = subprocess.call(command) == 0

    # check the server's response...
    if response:
        print(f"{server_name} , 'is up!'")
    else:
        print(f"{server_name} , 'is down!'")


server_name = "aws.amazon.com"
is_alive(server_name)
