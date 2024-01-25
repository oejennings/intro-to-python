import pickle 

def calc_difficulty(recipe): 
    if recipe["Cooking Time"] < 10 and len(recipe["Ingredients"]) < 4:
        Difficulty = "Easy"
    
    elif recipe["Cooking Time"] < 10 and len(recipe["Ingredients"]) >= 4:
        Difficulty = "Medium"
    
    elif recipe["Cooking Time"] >= 10 and len(recipe["Ingredients"]) < 4:
        Difficulty = "Intermediate"

    elif recipe["Cooking Time"] >= 10 and len(recipe["Ingredients"]) >= 4:
        Difficulty = "Hard"

    return Difficulty

def take_recipe():
    name = str(input("Enter the name of your recipe: "))
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = list(input("Enter ingredients: ").lower().split(", "))

    recipe = {
        "Name": name,
        "Cooking Time": cooking_time,
        "Ingredients": ingredients
    }
    recipe["Difficulty"] = calc_difficulty(recipe)
    return recipe

recipes_list = []
all_ingredients = []

filename = input("Filename where recipes are stored: ")

try:
    recipes_file = open(filename, "rb")
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print("File not found. Creating new file.")
    data = {"recipes_list": [], "all_ingredients": []}
except:
    print("Unexpected Error. Creating new file.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    recipes_file.close()
finally: 
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

num = int(input("How many recipes would you like to add? "))

for i in range(num):
    recipe = take_recipe()

    # Updated ingredient list
    for ingredient in recipe["Ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    # Adds recipe to recipe list
    recipes_list.append(recipe)

recipes_file = open(filename, "wb")
pickle.dump(data, recipes_file)
recipes_file.close()
