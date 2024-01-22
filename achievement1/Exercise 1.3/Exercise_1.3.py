# Create empty list 
recipes_list = []
ingredients_list = []

#Function to take recipe from user
def take_recipe() :
    name = input("Name of recipe:")
    cooking_time = int(input("Cooking time(min):"))
    ingredients = input("Ingredients:").split(", ")

    recipe = {
        "Name": name,
        "Cooking Time": cooking_time,
        "Ingredients": ingredients
    }
    return recipe

# Get number of recipes the user wants to add
n = int(input("How many recipes would you like to add?"))

# Take recipes
for i in range(n):
    recipe = take_recipe()

    # Updated ingredient list
    for ingredient in recipe["Ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    # Adds recipe to recipe list
    recipes_list.append(recipe)

# Caluculate difficulty of each recipe
for recipe in recipes_list:
    if recipe["Cooking Time"] < 10 and len(recipe["Ingredients"]) < 4:
        recipe["Difficulty"] = "Easy"
    elif recipe["Cooking Time"] < 10 and len(recipe["Ingredients"]) >= 4:
        recipe["Difficulty"] = "Medium"
    elif recipe["Cooking Time"] >= 10 and len(recipe["Ingredients"]) < 4:
        recipe["Difficulty"] = "Intermediate"
    elif recipe["Cooking Time"] >= 10 and len(recipe["Ingredients"]) > 4:
        recipe["Difficulty"] = "Hard"
    
# Print details of each recipe
for recipe in recipes_list:
    print("Recipe:", recipe["Name"])
    print("Cooking Time (min):", recipe["Cooking Time"])
    print("Ingredients:")
    for ingredient in recipe["Ingredients"]:
        print(ingredient)
    print("Difficulty:", recipe["Difficulty"])

# Print all ingredients in alphabetical order
def print_ingredients():
    ingredients_list.sort()
    print("All Ingredients")
    print("----------------")
    for ingredient in ingredients_list:
        print(ingredient)

print_ingredients()