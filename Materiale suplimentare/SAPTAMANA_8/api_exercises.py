"""
Folosim Simple Books API, descris aici :
https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client.
Pentru testare se va crea un obiect din aceasta clasa și se vor apela
metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token
(fa asta in constructor, client name si email ar trebui sa fie atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.

3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta/crea o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.

"""
import requests
#
# response = requests.get("https://simple-books-api.glitch.me/status")
# print(response.status_code)
# print(response.json())

# varianta Cosmina
def get_status(url):
    res = requests.get(url)
    return res


response1 = get_status("https://simple-books-api.glitch.me/status")
print(response1.status_code)
print(response1.json())
url = 'https://simple-books-api.glitch.me'
token = "5ef6aa91653030a7a3450d9b20388282d85446ecf82f4babcb787c984fe4cabf"

# get all books
#avem posibilitatea (este OPTIONAL) sa furnizam query params: limit si type
# https://simple-books-api.glitch.me/books
# https://simple-books-api.glitch.me/books?limit=1
# https://simple-books-api.glitch.me/books?type=1
# https://simple-books-api.glitch.me/books?type=1&limit=2
def get_all_books(url, limit=0, type=''):
    link = url
    # if limit is not None:
    #     link = f"{url}?limit={limit}"
    # if type is not None:
    #     link = f"{url}?type={type}"
    # if limit is not None and type is not None:
    #     link = f"{url}?type={type}&limit={limit}"
    data = {
        "limit": limit,
        "type": type
    }
    res = requests.get(link, params=data)
    return res


response2 = get_all_books("https://simple-books-api.glitch.me/books")
response2 = get_all_books("https://simple-books-api.glitch.me/books", 1)
response2 = get_all_books("https://simple-books-api.glitch.me/books", 2, "fiction")
response2 = get_all_books("https://simple-books-api.glitch.me/books", type="fiction")
print(response2.status_code)
print(response2.json())


# and operator
# x = 5
# y = 2
#
# print(x and y == 2)
# FALS/GRESIT ! => se verifica daca x este 2 SI daca y este 2: False AND True -> FALSE
# CORECT => se evalueaza bool(x) si daca y este egal cu 2: True AND True -> TRUE
# print(bool(x))
# print(x == 2 and y == 2)

# varianta Laurentia

import requests
# practice:
url = 'https://simple-books-api.glitch.me'
# 1 Get all books

response = requests.get(f'{url}/books')

print(response.status_code)
print(response.json())

# 2 Get all books filtered by type and limit (query params)
# VAR 1
response1 = requests.get(f'{url}/books?type=fiction&limit=2')
print(response1.status_code)
print(response1.json())

# VAR 2
data = {
    'type': 'fiction',
    'limit': 2
}
response2 = requests.get(f'{url}/books', params=data)

print(response2.status_code)
print(response2.json())

# 3 Post create token
# data2 = {
#     "clientName": "Laurentia",
#     "clientEmail": "lau1@example.com"
# }
# response3 = requests.post(f'{url}/api-clients', json=data2)
#
# print(response3.status_code)
# print(response3.json())

# 4 Post place an order

token = '0ff8bd4864bd32845dd3c6f3bc240abf73a70618f99987e37a240a1358036ad2'
comanda = {
    "bookId": "3",
    "customerName": "Laurentia"
}
headers_params = {
    'Authorization': token
}

response4 = requests.post(f'{url}/orders', json=comanda, headers=headers_params)
print(response4.status_code)
print(response4.json())