import json

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def list_foods(foods, food_type):
    print(f"\nAvailable {food_type}s:")
    for idx, food in enumerate([f for f in foods if f["type"] == food_type], 1):
        print(f"{idx}. {food['name']}")

def get_food_by_index(foods, food_type, index):
    filtered = [f for f in foods if f["type"] == food_type]
    if 1 <= index <= len(filtered):
        return filtered[index - 1]
    return None

def calculate_macros(food, quantity):
    if "unit" in food:
        ratio = quantity / food["unit"]
    else:
        ratio = quantity / food["weight"]
    return {
        "calories": round(food.get("calories", 0) * ratio, 2),
        "protein": round(food.get("protein", 0) * ratio, 2),
        "carbs": round(food.get("carbs", 0) * ratio, 2),
        "fat": round(food.get("fat", 0) * ratio, 2)
    }

def main():
    foods = load_json("combined_foods.json")

    print("Select type: protein / carb / fat")
    type_choice = input("Type: ").strip().lower()

    if type_choice not in ["protein", "carb", "fat"]:
        print("Invalid type.")
        return

    list_foods(foods, type_choice)

    try:
        index = int(input("Enter the number of the food you want: "))
    except ValueError:
        print("Invalid input.")
        return

    food = get_food_by_index(foods, type_choice, index)
    if not food:
        print("Food not found.")
        return

    if "unit" in food:
        quantity = float(input("Enter quantity (units): "))
    else:
        quantity = float(input("Enter quantity (grams): "))

    macros = calculate_macros(food, quantity)
    print(f"\n{quantity} {'units' if 'unit' in food else 'g'} of {food['name']} provides:")
    print(f"Calories: {macros['calories']} kcal")
    print(f"Protein: {macros['protein']} g")
    print(f"Carbs: {macros['carbs']} g")
    print(f"Fat: {macros['fat']} g")

if __name__ == "__main__":
    main()
