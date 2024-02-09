import requests

class Cocktail:
    def __init__(self):
        self.url = "https://www.thecocktaildb.com/api/json/v1/1/"
        
    def get_cocktail(self, name):
        response = requests.get(self.url+"search.php", params={"s": name})
        return response.json()
    
    def search_ingredient_by_name(self, id):
        response = requests.get(self.url+"search.php", params={"i": id})
        return response.json()
    
    def get_random_cocktail(self):
        response = requests.get(self.url+"random.php")
        return response.json()
    
    def get_cocktails_by_ingredient(self, ingredient):
        response = requests.get(self.url+"filter.php", params={"i": ingredient})
        return response.json()
    
    def get_non_alcoholic_cocktails(self):
        response = requests.get(self.url+"filter.php", params={"a": "Non_Alcoholic"})
        return response.json()
    
    def get_alcoholic_cocktails(self):
        response = requests.get(self.url+"filter.php", params={"a": "Alcoholic"})
        return response.json()
