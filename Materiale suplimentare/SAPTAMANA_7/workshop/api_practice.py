# Folosim Simple Books API, descris aici :
# https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md
#
# Toata rezolvarea se va face într-o clasa numita Books API Client. Pentru testare se va crea un
# obiect din aceasta clasa și se vor apela metodele implementate.
#
# 1. Folosind endpoint-ul de authentication, genereaza un access token (fa asta in constructor,
# client name si email ar trebui sa fie atribute).
#
# 2. Adaugă o metoda prin care poți vedea toate comenzile.
#
# 3. Adaugă o metoda prin care poți vedea toate cărțile.
#
# 4. Adaugă o metoda prin care poți posta o comanda.
#
# 5. Adaugă o metoda prin care poți șterge o comanda.
import requests


# class BooksAPIClient:
#     __BASE_URL = 'https://simple-books-api.glitch.me'
# #    accessToken = "4444061090c27ecea12e2b8764e5740f4acd498d7cad22a33f2483d8df8c26c0"
# date = {
#    "clientName": "Fanta1",
#    "clientEmail": "cosmin1@example.com"
# }
#     def __init__(self, client_name, client_email):
#         self.client_name = client_name
#         self.client_email = client_email
#         accessToken = requests.post(f'{self.__BASE_URL}/api-client', date)
#         return accessToken
#
#
# client1 = BooksAPIClient(date)
# print(client1)
