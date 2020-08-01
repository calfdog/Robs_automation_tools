"""
Rob Marchetti
Description: simple script to see if server or other host is up or not
"""

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

server_name = "google.com"


def is_alive(server_name):
    """
    Returns True if the server responds to a ping request.
    Remember that a server may not respond to a ICMP request, even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', server_name]

    response = subprocess.call(command) == 0

    # check the response...
    if response:
        print(f"{server_name} , 'is up!'")
    else:
        print(f"{server_name} , 'is down!'")


is_alive(server_name)
