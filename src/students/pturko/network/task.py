import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
FILE = 'json'
my_json = {'userId': 1, 'id': 99999, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipitsuscipit recusandae consequuntur expedita et cumreprehenderit molestiae ut ut quas totamnostrum rerum est autem sunt rem eveniet architecto'}
if __name__ == '__main__':
    response = requests.get(url)
    f = open(FILE, 'w')
    if response.ok:
        data = response.json()
        for x in range(0, 20):
            f.write(str(data[x]) + '\n')
        resp = requests.post(url, data=my_json)
        print(resp)
    else:
        print("Bad response code: {}".format(response.status_code))
