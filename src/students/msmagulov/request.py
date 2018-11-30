import urllib3
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"

if __name__ == '__main__':

    response = requests.get(url)
    if response.ok:

        jsoned = response.text
        data = json.loads(jsoned)
        f = open("filename.txt", "w+")
    for post in data[:20]:
        f.write(str(post))
        f.write("\n")
    f.close()
    assert data == response.json()
    print("response code: {}".format(response.status_code))

