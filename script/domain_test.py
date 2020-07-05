import os
import sys
import requests
file_name = sys.argv[1]
#print(file_name)
with open(file_name,'r+') as domain_file:
    content = domain_file.readlines()

content = [i.strip() for i in content]
c = [ "https://" + i for i in content]
print(c)
for i in c:
    try:
        req = requests.get(i)
        if req.status_code == 200:
            print("--------------------------------------")
            print(i)
            print(req.headers)
            print("---------------------------------------")
    except:
        pass


