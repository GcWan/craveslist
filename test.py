from ingredients import getIngredients

food_Item = input("What food do you want to make?\n")
ingredients_list = getIngredients(food_Item)

print(ingredients_list)
for k in ingredients_list:
    print(k)
