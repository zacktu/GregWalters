
#!/usr/bin/python
#------------------------------------------------------
# Cookbook.py
# Created for Beginning Programming Using Python #8
# and Full Circle Magazine
#------------------------------------------------------
import apsw
import string
import webbrowser

class Cookbook:

    def PrintAllRecipes(self):
        print("Entering printAllRecipes")
        pass

    def SearchForRecipes(self):
        print("Entering SearchForRecipes")
        pass

    def PrintSingleRecipe(self, which) :
        print("Entering PrintSingleRecipe with argument", which)
        pass

    def DeleteRecipe(self, which):
        print("Entering DeleteRecipe with argument", which)
        pass

    def EnterNew(self):
        print("Entering EnterNew")
        pass

    def PrintOut(self, which):
        print("Entering PrintOut with argument", which)
        pass

    def __init__(self):
        pass

def Menu():
    cbk = Cookbook() # Initialize the class

    loop = True
    while loop == True:
        print( \
            '===================================================')
        print('RECIPE DATABASE')
        print(
            '===================================================')
        print(' 1 - Show All Recipes')
        print(' 2 - Search for a recipe')
        print(' 3 - Show a Recipe')
        print(' 4 - Delete a recipe')
        print(' 5 - Add a recipe')
        print(' 6 - Print a recipe')
        print(' 0 - Exit')
        print( \
            '===================================================')
        response = input('Enter a selection -> ')
        if response == '1': # Show all recipes
            cbk.PrintAllRecipes()
        elif response == '2': # Search for a recipe
            cbk.SearchForRecipes()
        elif response == '3': # Show a single recipe
            cbk.PrintSingleRecipe(3)
            pass
        elif response == '4': # Delete Recipe
            cbk.DeleteRecipe(4)
            pass
        elif response == '5': # Add a recipe
            cbk.EnterNew()
            pass
        elif response == '6': # Print a recipe
            cbk.PrintOut(6)
            pass
        elif response == '0': # Exit the program
            print('Goodbye')
            loop = False
        else:
            print('Unrecognized command. Try again.')

Menu()