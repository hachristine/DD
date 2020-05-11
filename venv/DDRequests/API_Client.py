import json
import sys
import requests
import argparse
import getpass
from DDRequests import DDauth


if __name__ == "__main__":

    _PROTOCOL = "https"
    host = "192.168.180.81"
    port = 3009
    base_url = "{0}://{1}:{2}".format(_PROTOCOL, host, port)
    print(base_url)

    auth_info = {
        "auth_info": {
            "username": "sysadmin",
            "password": "P@ssw0rd!"
        }
    }

    authcli = DDauth(base_url,auth_info)


