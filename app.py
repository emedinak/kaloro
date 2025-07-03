from flask import Flask, render_template_string, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = "Eduardomedinak7"

food_references = {
    "Chicken breast": "A medium chicken breast weighs about 150 g when cooked.",
    "Beef": "A typical beef steak is around 200 g before cooking.",
    "Ground beef": "Common serving size is 100 g cooked.",
    "Salmon": "A salmon fillet is about 120–150 g on average.",
    "White fish": "A fillet usually weighs 100–150 g.",
    "Pork": "A pork chop weighs about 150 g raw.",
    "Turkey breast": "One slice is around 30 g; a full breast about 200 g.",
    "Shrimp": "A medium shrimp weighs around 10 g peeled.",
    "Octopus": "Typically served in 100 g portions cooked.",
    "Lamb": "A lamb chop is about 100–150 g raw.",
    "Lobster": "A whole lobster is around 500 g (edible meat about 150 g).",
    "Crab": "A medium crab has 100–150 g edible meat.",
    "Tuna": "A tuna steak is usually 150–200 g.",
    "Egg": "A medium egg weighs about 50 g (without shell).",
    "Duck breast": "Usually 180–200 g raw.",
    "Cod": "A cod fillet weighs about 120 g.",
    "Scallops": "One scallop weighs about 20 g.",
    "White rice": "A cooked cup is about 150 g.",
    "Brown rice": "A cooked cup is about 150 g.",
    "Pasta (cooked)": "One cup cooked pasta weighs around 140 g.",
    "Quinoa (cooked)": "One cup cooked quinoa is about 185 g.",
    "Sweet potato": "A medium sweet potato weighs 130 g raw.",
    "Potato": "A medium potato is around 150 g raw.",
    "Banana": "A medium banana is about 120 g without peel.",
    "Apple": "A medium apple weighs about 150 g.",
    "Orange": "A medium orange weighs about 130 g peeled.",
    "Pineapple": "One slice is around 80 g; a whole pineapple about 900 g.",
    "Lentils (cooked)": "One cup cooked lentils is about 200 g.",
    "Black beans (cooked)": "One cup cooked is about 180 g.",
    "Chickpeas (cooked)": "One cup cooked is around 165 g.",
    "Olive oil": "One tablespoon is 13.5 g.",
    "Butter": "One tablespoon is about 14 g.",
    "Almonds": "A handful is about 28 g (1 oz).",
    "Walnuts": "A handful is about 28 g (1 oz).",
    "Peanut butter": "One tablespoon is about 16 g.",
    "Cashews": "A handful is about 28 g (1 oz).",
    "Chia seeds": "One tablespoon is about 12 g.",
    "Flaxseeds": "One tablespoon is about 10 g.",
    "Sunflower seeds": "A handful is about 28 g (1 oz).",
    "Sardines": "A typical can is around 100–120 g drained.",
    "Dates": "One date weighs about 8 g.",
    "Raisins": "A tablespoon is about 9 g.",
    "Pistachios": "A handful is about 28 g (1 oz).",
    "Avocado": "A whole avocado is around 200 g; half about 100 g.",
    "Tofu": "A slice is about 80–100 g.",
    "Rabbit meat": "One serving cooked is about 150 g.",
    "Serrano ham": "One slice is about 20 g.",
    "Manchego cheese": "One slice is about 30 g.",
    "Cottage cheese": "Half cup is around 110 g.",
    "Feta cheese": "A cube is about 20 g; a serving about 60 g.",
    "Greek yogurt": "One cup is about 245 g.",
    "Whey protein powder": "A scoop is about 30 g.",
    "Lettuce": "One leaf is about 15 g.",
    "Broccoli": "One medium stalk is about 150 g.",
    "Arepa": "One medium arepa weighs around 120 g.",
    "Corn tortilla": "One tortilla is about 30 g.",
    "Mango": "A medium mango is about 200 g peeled.",
    "Strawberries": "One berry is about 12 g.",
    "Grapes": "One grape is about 5 g; a bunch around 150 g.",
    "Kiwi": "One medium kiwi is about 75 g peeled.",
    "White bread": "One slice is about 25 g.",
    "Whole wheat bread": "One slice is about 28 g.",
    "Hazelnuts": "A handful is about 28 g (1 oz).",
    "Artichoke": "A medium artichoke weighs about 120 g cooked.",
    "Spinach": "A cup of raw spinach is about 30 g.",
    "Zucchini": "A medium zucchini weighs about 200 g raw.",
    "Cauliflower": "One cup of cauliflower florets weighs about 100 g.",
    "Green beans": "A handful is about 50 g raw.",
    "Veal": "A veal steak is about 150 g raw.",
    "Tempeh": "A serving is about 100 g.",
    "Seitan": "A portion is about 85 g cooked.",
    "Ghee": "One tablespoon is about 14 g.",
    "Pumpkin seeds": "A handful is about 28 g (1 oz)."
}

with open("combined_foods.json") as f:
    foods = json.load(f)

TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Kaloro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: "Inter", sans-serif;
            background: #fdf8f3;
            color: #333;
            padding: 1px;
            text-align: center;
        }
        form {
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 400px;
            margin: 5px auto;
            text-align: left;
        }
        label {
            font-weight: bold;
        }
        select, input {
            width: 100%;
            padding: 8px;
            margin: 6px 0 12px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #ff6b00;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            margin-right: 5px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button:hover {
            background-color: #e65c00;
            transform: scale(1.05);
        }
        ul {
            list-style: none;
            padding: 0;
        }
        .result-card {
            background-color: #fff7f0;
            border: 1px solid #ffdab9;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin: 20px auto;
            max-width: 400px;
            text-align: left;
        }
        .food-reference {
            font-size: 0.9em;
            color: #555;
            margin-top: -8px;
            margin-bottom: 12px;
        }
        .fade-in {
            opacity: 0;
            animation: fadeIn 0.8s forwards;
        }
        @keyframes fadeIn {
            to { opacity: 1; }
        }
        hr {
            border-top: 1px solid #ffdab9;
            max-width: 400px;
            margin: 30px auto;
        }
    </style>
</head>
<body>
<img src="{{ url_for('static', filename='kaloro_logo_transparent.png') }}" alt="Kaloro Logo"
     style="width: 400px; margin: 0 auto 10px auto; display: block;">
     
    <form method="post">
        <label for="type">Select type:</label>
        <select name="type" id="type" required onchange="this.form.submit()">
            <option value="">--Select--</option>
            {% for t in types %}
                <option value="{{ t }}" {% if selected_type == t %}selected{% endif %}>{{ t.capitalize() }}</option>
            {% endfor %}
        </select>
    </form>

    <hr>

    {% if selected_type %}
        <form method="post">
            <input type="hidden" name="type" value="{{ selected_type }}">
            <label for="food">Select food:</label>
            <select name="food" id="food" required>
                {% for food in food_list %}
                    <option value="{{ food['name'] }}">{{ food['name'].title() }}</option>
                {% endfor %}
            </select>
            <p id="food-ref" class="food-reference"></p>
            <label for="quantity">Enter quantity ({{ unit_label }}):</label>
            <input type="number" step="0.01" name="quantity" id="quantity" required>
            <button type="submit" name="action" value="calculate">🟰 Calculate</button>
            <button type="submit" name="action" value="add">➕ Add to Meal</button>
        </form>
    {% endif %}

    {% if result %}
        <div class="result-card fade-in">
            <h2>Result</h2>
            <p>{{ quantity }} {{ unit_label }} of {{ result['name'] }} provides:</p>
            <ul>
                <li>🔥 Calories: {{ result['calories'] }} kcal</li>
                <li>💪 Protein: {{ result['protein'] }} g</li>
                <li>🍞 Carbs: {{ result['carbs'] }} g</li>
                <li>🧈 Fat: {{ result['fat'] }} g</li>
            </ul>
        </div>
        <hr>
    {% endif %}

    {% if meal_total %}
        <div class="result-card fade-in">
            <h2>Meal Total</h2>
            <ul>
                <li>🔥 Calories: {{ meal_total.totales.calories | round(2) }} kcal</li>
                <li>💪 Protein: {{ meal_total.totales.protein | round(2) }} g</li>
                <li>🍞 Carbs: {{ meal_total.totales.carbs | round(2) }} g</li>
                <li>🧈 Fat: {{ meal_total.totales.fat | round(2) }} g</li>
            </ul>
            <h3>Foods in this meal:</h3>
            <ul>
                {% for item in meal_total.detalle %}
                    <li>{{ item.name }} - {{ item.amount | round(2) }} grams</li>
                {% endfor %}
            </ul>
            <form method="post">
                <input type="hidden" name="action" value="reset">
                <button type="submit">Reset Meal</button>
            </form>
        </div>
    {% endif %}

    {% if selected_type %}
    <script>
        const foodReferences = {{ food_references | tojson }};
        const selectFood = document.getElementById("food");
        const refText = document.getElementById("food-ref");

        selectFood.addEventListener("change", function() {
            const selected = this.value;
            if (foodReferences[selected]) {
                refText.textContent = foodReferences[selected];
            } else {
                refText.textContent = "";
            }
        });

        if (selectFood.value && foodReferences[selectFood.value]) {
            refText.textContent = foodReferences[selectFood.value];
        }
    </script>
    {% endif %}

    <footer style="margin-top: 40px; font-size: 0.9em; color: #555;">
      © 2025 Kaloro ·
      <a href="mailto:emedinak7@gmail.com"
         style="color: #ff6b00; text-decoration: none; font-weight: 600;">
        emedinak7@gmail.com
      </a>
      ·
      <a href="/about"
         style="color: #888; text-decoration: none; font-weight: 600;">
        About
      </a>
    </footer>
</body>
</html>
"""

from utils import crear_comida

meal = []

@app.route("/", methods=["GET", "POST"])
def index():
    types = sorted(set(f["type"] for f in foods))
    selected_type = None
    food_list = []
    result = None
    quantity = None
    unit_label = "grams"
    meal_total = None

    if "meal" not in session:
        session["meal"] = []
 
    if request.method == "POST":
        selected_type = request.form.get("type")
        food_list = [f for f in foods if f["type"] == selected_type]

        food_name = request.form.get("food")
        quantity = request.form.get("quantity")
        action = request.form.get("action")

        if action == "reset":
            session["meal"] = []
            session.modified = True

        if food_name and quantity:
            quantity = float(quantity)
            food = next((f for f in food_list if f["name"] == food_name), None)
            if food:
                if "unit" in food:
                    ratio = quantity / food["unit"]
                    unit_label = "units"
                else:
                    ratio = quantity / food["weight"]
                    unit_label = "grams"

                result = {
                    "name": food["name"],
                    "calories": round(food.get("calories", 0) * ratio, 2),
                    "protein": round(food.get("protein", 0) * ratio, 2),
                    "carbs": round(food.get("carbs", 0) * ratio, 2),
                    "fat": round(food.get("fat", 0) * ratio, 2)
                }

                if action == "add":
                    session["meal"].append((food["name"], ratio))
                    session.modified = True

    if session.get("meal"):
        meal_total = crear_comida(session["meal"])

    return render_template_string(TEMPLATE, types=types, selected_type=selected_type,
                                  food_list=food_list, result=result, quantity=quantity,
                                  unit_label=unit_label,meal_total=meal_total,
                                  food_references=food_references)


ABOUT_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>About Kaloro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: "Inter", sans-serif;
            background: #fdf8f3;
            color: #333;
            padding: 20px;
            text-align: center;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: left;
        }
        a {
            color: #ff6b00;
            text-decoration: none;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container fade-in">
        <h1>About Kaloro</h1>
        <p><strong>Kaloro</strong> is a personal web app to help you track and plan your meals, calculating calories, proteins, carbs, and fats in a simple way.</p>
        <p>This project was created by Eduardo Medina Krumholz, passionate about technology, nutrition and healthy lifestyles.</p>
        <p>Contact me anytime at <a href="mailto:emedinak7@gmail.com">emedinak7@gmail.com</a> or connect on 
        <a href="https://www.linkedin.com/in/eduardo-medina-krumholz-3b756b243" target="_blank">LinkedIn</a>.</p>
        <p style="margin-top:20px;">
            <a href="/">← Back to Kaloro</a>
        </p>
    </div>
</body>
</html>
"""

@app.route("/about")
def about():
    return render_template_string(ABOUT_TEMPLATE)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

