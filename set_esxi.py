
import requests,json,getpass
def get_host_id(box,name,auth):
    url="http://{}/api/rest/hosts?name={}".format(box,name)
    hosts=requests.get(url=url,auth=auth).json()
    if hosts['result']:
        return hosts['result'][0]['id']
    else:
        if hosts['error']:
            print "****ERROR::******"
            print hosts['error']['message']
        else:
            print "Failure: Host {} Not Found".format(name)
        return None

 
def change_host_type(box,auth,host_id):
    headers={'Content-Type':'application/json'}
    body={'host_type':'esxi'}
    url="http://{}/api/rest/hosts/{}".format(box,host_id)
    change=requests.put(auth=auth,data=json.dumps(body),url=url,headers=headers)
    if change.json()['error']:
        print change.json()['error']['message']
        return False
    else:
        return True


try:
    box=raw_input("Enter box name/Ip:")
    username=raw_input("Enter Usename:")
    password=getpass.getpass('Password:')
    host=raw_input("Enter ESXi Host Name:")
    auth=(username,password)
    host_id=get_host_id(box,host,auth)
    if (host_id):
        if (change_host_type(box,auth,host_id)):
            print "Success!"
        else:
            print "Failure!"
except Exception as E:
    print "Caught Exception:",E