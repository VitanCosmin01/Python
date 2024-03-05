"""
Folosim Simple Books API, descris aici :
 https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client.
Pentru testare se va crea un obiect din aceasta clasa și se vor
apela metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token
(fa asta in constructor, client name si email ar trebui sa fie
atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.

3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta/crea o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.

"""
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
