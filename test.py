from ingredients import getIngredients

food_item = input("What food do you want to make?\n")
food_info = getIngredients(food_item)

print("Ingredients for:", food_info['name'])
print("Approx preparation time:", food_info['time'])
print("Estimated Calories:", food_info['nutrition'])

for i, k in enumerate(food_info['ingredients']):
    print(str(i+1)+" -", k)
