# Reference Documentation: http://support.collegiatelink.net/entries/22078465

import uuid, hashlib, time, requests

current_time = str(int(time.time()) * 1000)
public_key = "northwestern-07"
private_key = "accf29ccd8f549e48c47ff9ed09eec54"
random_string = str(uuid.uuid4())
myhash = hashlib.md5(public_key + current_time + random_string + private_key).hexdigest()

print "current_time", current_time
print "public_key", public_key
print "private_key", private_key
print "random_string", random_string
print "hashez", myhash

api_url = 'https://northwestern.collegiatelink.net/api/'
resource = 'organizations'
params = {
    'time': current_time,
    'apikey': public_key,
    'random': random_string,
    'hash': myhash
}

response = requests.get(api_url + resource, params=params)
with open('response.txt', 'w+') as f:
    f.write(response.text.encode('ascii', 'ignore'))