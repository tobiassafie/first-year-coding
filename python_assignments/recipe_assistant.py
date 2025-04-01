# Program: hw08_food.py
# Purpose: Reads nutrition facts from .csv files and produces nutritional labels
# Author:  Tobias Safie - tks57@drexel.edu
# Date:    March 4, 2025

# Import CSV to be able to operate on them
import csv

def loadFoods(filename):
    # Referencing fileNotFound in case a file cannot be called
    foodDict = {}
    # Trying to load the file data
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            # Iterate thru each row in the file
            for row in reader:
                # Takes the name of the food
                foodName = row["Food (100g)"].strip()
                # Reads the file and attaches attributes to each food name, assuming they're given
                foodDict[foodName] = {
                    "Calories": float(row["Calories (kCal)"]) if row["Calories (kCal)"] else None,
                    "Protein": float(row["Protein (g)"]) if row["Protein (g)"] else None,
                    "Carbohydrate": float(row["Carbohydrates (g)"]) if row["Carbohydrates (g)"] else None,
                    "Fat": float(row["Fats (g)"]) if row["Fats (g)"] else None,
                    "Type": row["Type"].strip()
                    }
        # Return the dictionary
        return foodDict
    
    # In case the file does not exist, return None
    except:
        return None


def readRecipe(filename):
    # Attempt to open file
    try:
        with open(filename) as file:
            # Converts the file into lists
            reader = csv.reader(file)
            # Creates a lists of lists, almost like a 2D array
            lines = list(reader)
            # Creates the dictionary of the recipe
            recipeDict = {
                "Name": lines[0][0].strip(),
                "Serves": float(lines[0][1])
                }
            # Iterates thru recipe to extract each ingredient and ingredient weight
            for row in lines[1:]:
                recipeDict[row[0].strip()] = float(row[1])
        return recipeDict
    
    # If the file cannot be opened, return None
    except:
        return None


def analyzeIngredients(foodData, recipeDict):
    # Creates a dictionary that stores the nutritional info of a given recipe
    analysis = {
        "Calories": 0.0,
        "Protein": 0.0,
        "Carbohydrate": 0.0,
        "Fat": 0.0,
        "Total Grams": 0.0,
        "Incomplete": False
        }
    
    for ingredient, grams in recipeDict.items():
        # Skips reading of the name and the serving size
        if ingredient in ["Name", "Serves"]:
            continue
        
        # Check to see if the ingredient is in the database, then add its attributes to dictionary
        if ingredient in foodData:
            data = foodData[ingredient]
            analysis["Calories"] += data["Calories"]
            analysis["Protein"] += data["Protein"]
            analysis["Carbohydrate"] += data["Carbohydrate"]
            analysis["Fat"] += data["Fat"]
            analysis["Total Grams"] += grams
            
        # If the ingredient can't be found, offer an error message and mark the info as incomplete
        else:
            print(f"Trouble looking up {ingredient}")
            analysis["Incomplete"] = True
    
    # Iterate thru the recipe to give nutritional info according to 1 serving
    for i in ["Calories", "Protein", "Carbohydrate", "Fat"]:
        analysis[i] /= recipeDict["Serves"]
    analysis["Total Grams"] /= recipeDict["Serves"]        
    
    return analysis


def generateLabel(recipeDict, analysisDict):
    
    # Generates a string by appending each piece of nutritional info
    label = f"{recipeDict['Name']} ({analysisDict['Total Grams']:.1f} g)\n"
    label += f"Calories {analysisDict['Calories']:.1f}\n"
    label += f"Protein {analysisDict['Protein']:.1f} g\n"
    label += f"Carbohydrate {analysisDict['Carbohydrate']:.1f} g\n"
    label += f"Fat {analysisDict['Fat']:.1f} g\n"
    # In case any info is missing, will mention that the recipe is incomplete
    if analysisDict["Incomplete"]:
        label += "Note: Not all ingredients accounted for\n"
    return label

# Run main
if __name__ == "__main__":
    while True:
        foodFile = input("Enter filename for foods database: ")
        foodData = loadFoods(foodFile)
        if foodData:
            break
        print("That file could not be loaded.")
    
    while True:
        recipeFile = input("Enter recipe filename: ")
        recipeData = readRecipe(recipeFile)
        if recipeData:
            break
        print("That file could not be loaded.")
    
    analysis = analyzeIngredients(foodData, recipeData)
    print(generateLabel(recipeData, analysis))
    