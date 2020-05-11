import json
import sys
import requests
import argparse
import getpass

class DDauth:

    AUTH_HEADERS = {}
    def __init__(self, base_url, credentials):
        self.base_url = base_url
        self.credentials = credentials


    def authenticate(base_url, credentials):

        login_url = "{0}{1}".format(base_url,"/rest/v1.0/auth")

        try:
            response = requests.post(login_url,json=credentials,verify=False)
            status_code = response.status_code

            if status_code != 201:
                #handle error
                failed = json.loads(response.text)
                __handle_failure(failed)
                response.close()
                return False
            else:
                auth_headers["X-DD-AUTH-TOKEN"] = response.headers["X-DD-AUTH-TOKEN"]
                response.close()
                return True
        except Exception as e:
            print(e)



