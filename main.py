from ingredients import getIngredients, getPrice
from send import send_receive
import asyncio
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        item = str(escape(request.args.get("item", "")))
        if item:
            food_info = getIngredients(item)
            price_info = getPrice(food_info['ingredients'])
            return (
                render_template(
                    "index.html",
                    result=[[food_info['ingredients'][i], price_info[i]] for i in range(len(price_info))],
                    name="Ingredients for: " + food_info['name'],
                    time="Approximate preparation time: " + food_info['time'],
                    nutrition="Estimated Calories: " + food_info['nutrition']
                )
            )
    elif request.method == 'POST':
        print("Listening...")
        item = asyncio.run(send_receive("ingredients"))
        food_info = getIngredients(item)
        price_info = getPrice(food_info['ingredients'])
        return (
            render_template(
                "index.html",
                result=[[food_info['ingredients'][i], price_info[i]] for i in range(len(price_info))],
                name="Ingredients for: " + food_info['name'],
                time="Approximate preparation time: " + food_info['time'],
                nutrition="Estimated Calories: " + food_info['nutrition']
            )
        )
    return render_template("index.html")

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
    app.run(host="127.0.0.1", port=8080, debug=True)
