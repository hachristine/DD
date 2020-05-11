import json
import sys
import requests
import argparse
import getpass

_PROTOCOL = "https"
host = "192.168.180.81"
port = 3009
base_url = "{0}://{1}:{2}".format(_PROTOCOL, host, port)
auth_info = {
     "auth_info":{
         "username":"sysadmin",
         "password":"P@ssw0rd!"
     }
}
auth_headers = {}
system_id = "/dd-systems/0"

def authenticate():
    global system_id
    #print(login_url)
    login_url = "{0}{1}".format(base_url, "/rest/v1.0/auth")
    response = requests.post(login_url, json=auth_info, verify=False)
    status_code = response.status_code

    if status_code != 201:
        failed = json.loads(response.text)
        __handled_failure(failed)
        response.close()
    else:
        auth_headers["X-DD-AUTH-TOKEN"] = response.headers["X-DD-AUTH-TOKEN"]
        response.close()
    print("Authenticated")
    #print(json.dumps(auth_info, indent=2))

    #gettin system ID and adding it to the base_url
    url = "{0}{1}".format(base_url,"/rest/v1.0/system")
    response = requests.get(url,headers=auth_headers,verify=False)
    jresponse = json.loads(response.text)

    if response.status_code != 200:
        print("Error getting System info")
        response.close()

    #Retrieving systems ID
    model = jresponse["model"]
    if model == "DD Management Center":
        #url2 = "{0}{1}".format(base_url,"/rest/v1.0/dd-systems")
        system_id = "/dd-systems"
    else:
        #url2 = "{0}{1}".format(base_url,"/rest/v1.0/dd-systems/0")
        system_id = "/dd-systems/0"
    #menu()

def get_alerts():
    alerts_url = "{0}{1}{2}{3}".format(base_url,"/rest/v1.0",system_id,"/alerts")
    response = requests.get(alerts_url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_alerts_notifylists():
    alerts_url = "{0}{1}{2}{3}".format(base_url,"/rest/v1.0",system_id,"/alerts/notify-lists")
    response = requests.get(alerts_url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_cifs_shares():
    cifs_url = "{0}{1}{2}{3}".format(base_url,"/rest/v1.0",system_id,"/protocols/cifs/shares")
    response = requests.get(cifs_url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_cloudprofiles():
    url = "{0}{1}{2}{3}".format(base_url,"/rest/v1.0",system_id,"/cloud-profiles")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_cloudunits():
    url = "{0}{1}{2}{3}".format(base_url,"/rest/v1.0",system_id,"/cloud-units")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_compmeasurements():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/stats/compression/measurements")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_datamovement():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/data-movement")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_ddboost():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/protocols/ddboost")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_ddboost_clients():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/protocols/ddboost/clients")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_ddboost_storageunits():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/protocols/ddboost/storage-units")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_filesys():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/file-systems")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_filesys_stats():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/stats/file-systems")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_mtrees():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v3.0", system_id, "/mtrees")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_iscsi():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/services/iscsi")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_services():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/services")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_snapshots():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v1.0", system_id, "/snapshots")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_stats():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v2.0", system_id, "/stats")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_stats_capacity():
    url = "{0}{1}{2}{3}".format(base_url, "/rest/v2.0", system_id, "/stats/capacity")
    response = requests.get(url, headers=auth_headers, verify=False)
    jdata = json.loads(response.text)
    print(json.dumps(jdata, indent=2))

def get_users():

    users_url = "{0}{1}{2}{3}".format(base_url,"/rest/v1.0",system_id,"/users")
    #Request to get users
    response2 = requests.get(users_url,headers=auth_headers,verify=False)
    #Pretty JSON
    jdata = json.loads(response2.text)
    print(json.dumps(jdata, indent=2,))

    menu()

def menu():
    print("Main Menu \n1. Authenticate \n2. Get Users \n3. Get Alerts Notify List")
    parser = argparse.ArgumentParser("Select option")
    parser.add_argument("option", type=int)

    args = parser.parse_args()
    if args.option == 1:
        authenticate()

    if args.option == 2:
        get_users()

if __name__ == "__main__":
    print("Testing Rest APIs on DDVE...")
    #menu()
    authenticate()
    #get_alerts_notifylists()
    #get_alerts()
    #get_cifs_shares()
    #get_cloudprofiles()
    #get_cloudunits()
    #get_compmeasurements()
    #get_datamovement()
    #get_ddboost()
    #get_ddboost_clients()
    #get_ddboost_storageunits()
    #get_filesys()
    #get_filesys_stats() doesnt work yet requires extra paramter
    #get_mtrees()
    #get_iscsi()
    #get_services()
    #get_stats()
    #get_stats_capacity()

