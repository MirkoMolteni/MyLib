import requests

class Meal:
    def __init__(self):
        self.url = "https://www.themealdb.com/api/json/v1/1/"
        
    def get_meal(self, name):
        response = requests.get(self.url+"search.php", params={"s": name})
        return response.json()
    
    def get_random_meal(self):
        response = requests.get(self.url+"random.php")
        return response.json()
    
    def get_meals_by_ingredient(self, ingredient):
        response = requests.get(self.url+"filter.php", params={"i": ingredient})
        return response.json()