from ingredients import getIngredients
from send import send_receive
import asyncio

item = asyncio.run(send_receive("ingredients"))
food_info = getIngredients(item)

print("Ingredients for:", food_info['name'])
print("Approximate preparation time:", food_info['time'])
print("Estimated Calories:", food_info['nutrition'])

for i, k in enumerate(food_info['ingredients']):
    print(str(i+1)+" -", k)
