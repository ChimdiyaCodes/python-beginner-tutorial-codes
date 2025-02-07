class Nigerian_food:
    def __init__(self, food, ingredients):
        self.food = food
        self.ingredients = ingredients

    def origin(self):
        print("I'm enjoyed by Nigerians...")

    def get_food_ingredients(self):
        print(f"I'm {self.food} and I'm prepared with {self.ingredients}. ")


swallow = Nigerian_food('Eba', 'Garri and Hot water')

swallow.get_food_ingredients()

swallow.origin()

soup = Nigerian_food('Egusi soup', 'melon')

soup.get_food_ingredients()

soup.origin()


class Yoruba_food (Nigerian_food):
    def __init__(self, food, ingredients, texture):
        super().__init__(food, ingredients)
        self.texture = texture

    def origin(self):
        print('I originate from the Yoruba people of Nigeria...')

    def get_food_ingredients(self):
        print(f"I'm {self.food}, I'm prepared with {
              self.ingredients}, and {self.texture}.")


class Igbo_food (Nigerian_food):
    def origin(self):
        print('I originate from the Igbo people of Nigeria...')


class Jollof_rice (Nigerian_food):
    pass


amala_ewedu = Yoruba_food("Amala and Ewedu", "yam flour and efo ewedu",
                          "I'm rich in taste and stretchy in texture")
ofe_nsala = Igbo_food("Akpu and Ofe nsala",
                      "Cassava for Akpu and utazi and okpei with yam as thickener for nsala")
rice = Jollof_rice(
    "Jollof Rice", "Rice, oil, tomatoes and pepper with seasoning")

amala_ewedu.get_food_ingredients()
amala_ewedu.origin()
ofe_nsala.get_food_ingredients()
ofe_nsala.origin()
rice.get_food_ingredients()
rice.origin()


print('\n\n')

for x in (swallow, soup, amala_ewedu, ofe_nsala, rice):
    x.get_food_ingredients()
    x.origin()
