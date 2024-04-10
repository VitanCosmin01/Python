import requests


class ProductsApi:

    __BASE_URL = "https://dummyjson.com/products"

    def get_products(self):
        response = requests.get(self.__BASE_URL)
        return response

    def get_product_by_id(self, product_id):
        url = f"{self.__BASE_URL}/{product_id}"
        response = requests.get(url)
        return response

    def search_products(self, search_criteria):
        url = f"{self.__BASE_URL}/search?q={search_criteria}"
        response = requests.get(url, params={"q": search_criteria})
        return response

    def get_product_categories(self):
        url = f'{self.__BASE_URL}/categories'
        response = requests.get(url)
        return response

    def get_products_of_category(self, category):
        url = f'{self.__BASE_URL}/category/{category}'
        response = requests.get(url)
        return response

    def add_product(self, **kwargs):
        # add_product(title="produs_nou", price=23.45)
        # add_product(title="produs_nou")
        url = f'{self.__BASE_URL}/add'
        kwargs = {
            "title": "produs nou",
            "price": 23.45
        }
        response = requests.post(url, data=kwargs)
        return response

    def update_product(self, product_id, **kwargs):
        url = f"{self.__BASE_URL}/{product_id}"
        response = requests.patch(url, data=kwargs)
        return response

    def delete_product(self, product_id):
        url = f'{self.__BASE_URL}/{product_id}'
        response = requests.delete(url)
        return response


product_api = ProductsApi()
# response = product_api.get_products()
# print(response.status_code)
# print(response.json())
id_1 = product_api.get_product_by_id(1)
print(id_1.json())
print(id_1.status_code)

# categories = product_api.get_product_categories()
# print(categories.status_code)
# print(categories.json())
# smartphones = product_api.get_products_of_category("smartphones")
# print(smartphones.json())
# print(smartphones.status_code)
