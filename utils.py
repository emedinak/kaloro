import json

with open("combined_foods.json", "r") as f:
    food_data = json.load(f)

def find_food(name):
    for food in food_data:
        if food["name"].lower() == name.lower():
            return food
    return None

def crear_comida(selecciones):
    totales = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    detalle = []

    for nombre, cantidad in selecciones:
        alimento = find_food(nombre)
        if alimento:
            detalle.append({
                "name": nombre,
                "amount": cantidad,
                "calories": alimento["calories"] * cantidad,
                "protein": alimento["protein"] * cantidad,
                "carbs": alimento["carbs"] * cantidad,
                "fat": alimento["fat"] * cantidad
            })
            totales["calories"] += alimento["calories"] * cantidad
            totales["protein"] += alimento["protein"] * cantidad
            totales["carbs"] += alimento["carbs"] * cantidad
            totales["fat"] += alimento["fat"] * cantidad
        else:
            print(f"Alimento no encontrado: {nombre}")

    return {"totales": totales, "detalle": detalle}
