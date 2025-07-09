from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

buns = ['Флюоресцентная булка R2-D3',
        'Краторная булка N-200i']

ingredients = ['Соус Spicy-X',
               'Соус фирменный Space Sauce',
               'Соус традиционный галактический',
               'Соус с шипами Антарианского плоскоходца',
               'Мясо бессмертных моллюсков Protostomia',
               'Говяжий метеорит (отбивная)',
               'Биокотлета из марсианской Магнолии',
               'Филе Люминесцентного тетраодонтимформа',
               'Хрустящие минеральные кольца',
               'Мини-салат Экзо-Плантаго',
               'Сыр с астероидной плесенью']

types = ['Соусы',
         'Начинки']

available_buns = [
        {"name": "black bun", "price": 100},
        {"name": "white bun", "price": 200},
        {"name": "red bun", "price": 300},
    ]

available_ingredients = [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
    ]