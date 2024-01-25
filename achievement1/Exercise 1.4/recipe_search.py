import pickle

def display_recipe(recipe):
    print("Name: ", recipe["Name"])
    print("Cooking Time: ", recipe["Cooking Time"])
    print("Ingredients: ", recipe["Ingredients"])
    print("Difficulty: ", recipe["Difficulty"])

def search_ingredient(data):
    all_ingredients = data["all_ingredients"]
    all_ingredients_indexed = list(enumerate(all_ingredients, 1))

    for ingredient in all_ingredients_indexed:
        print("No ", ingredient[0], " - ", ingredient[1])

    try: 
        num = int(input("Enter ingredient number: "))
        index = num - 1
        ingredient_search = all_ingredients[index]
        ingredient_search = ingredient_search.lower()

    except IndexError:
       print("Then number you entered is not valid.")

    except:
        print("Unexpected error.")

    else: 
         for recipe in data["recipes_list"]:
            for recipe_ing in recipe["Ingredients"]:
                if (recipe_ing == ingredient_search):
                    print("\nThe following recipes includes the entered ingredient: ")
                    print("-----------------------------------------------------------")
                    display_recipe(recipe)


filename = input("Enter filename where your recipes are stored: ")

try: 
    recipes_file = open(filename, "rb")
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print("File not found.")

except:
    print("Unexpected Error")

else:
    search_ingredient(data)

finally:
    recipes_file.close()
    
