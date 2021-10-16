from ingredients import getIngredients
from send import send_receive
import asyncio
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    item = request.args.get("item", "")
    if item:
        food_info = getIngredients(item)
        return (
                """<form action="" method="get">
                        What would you like to make?: <input type="text" name="item">
                        <input type="submit" value="Get Ingredients">
                    </form>"""
                + "Ingredients for: " + food_info['name']
                + "\nApproximate preparation time:" + food_info['time']
                + "\nEstimated Calories:" + food_info['nutrition']
                + "\n".join([str(i+1)+" : " + k for i, k in enumerate(food_info['ingredients'])])
        )
    else:
        return (
            """<form action="" method="get">
                        What would you like to make?: <input type="text" name="item">
                        <input type="submit" value="Get Ingredients">
                    </form>"""
        )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)