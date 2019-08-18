"""
https://jsonplaceholder.typicode.com/posts
http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
"""
# import urllib3
import requests
import json
url = "https://jsonplaceholder.typicode.com/comments"

if __name__ == '__main__':

    response = requests.get(url)
    if response.ok:

        jsoned = response.text
        data = json.loads(jsoned)
        print(data)
        assert data == response.json()
    else:
        print("Bad response code: {}".format(response.status_code))
