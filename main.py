from ingredients import getIngredients, getPrice
import aisleRead
from send import send_receive
import asyncio
from flask import Flask, render_template, request, escape, Response


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'submit_button' in request.args:
            item = str(escape(request.args.get("item", "")))
            if not item:
                return render_template("index.html", time="Please enter a search term")
        else:
            return render_template("index.html")
    else:
        print("Listening...")
        item = asyncio.run(send_receive("ingredients"))
    food_info = getIngredients(item)
    ingredients = food_info['ingredients']
    price_info = getPrice(ingredients)
    aisle_info = [aisleRead.find(k) for k in ingredients]

    return (
        render_template(
            "index.html",
            result=[[ingredients[i], price_info[i], aisle_info[i]] for i in range(len(price_info))],
            name="Ingredients for: " + food_info['name'],
            time="Approximate preparation time: " + food_info['time'],
            nutrition="Estimated Calories: " + food_info['nutrition'],
        )
    )


# @app.route('/audio')
# def audio():
#     return Response(sound())

# import time
#
# @app.route('/yield')
# def test():
#     def inner():
#         for x in range(100):
#             time.sleep(1)
#             yield '%s<br/>\n' % x
#     return Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately

app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
