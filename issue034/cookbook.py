
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
        print('%s %s %s %s' \
            % ('Item'.ljust(5), 'Name'.ljust(30), \
               'Serves'.ljust(20), 'Source'.ljust(30)))
        print('---------------------------------')
        sql = 'SELECT * FROM Recipes'
        cntr = 0
        for recipe in cursor.execute(sql):
            cntr += 1
            print('%s %s %s %s' \
                % (str(recipe[0]).rjust(5), recipe[1].ljust(30), \
                   recipe[2].ljust(20), recipe[3].ljust(30)))
        print('---------------------------------')
        self.totalcount = cntr
        return

    def SearchForRecipes(self):
        print("Entering SearchForRecipes")
        return

    def PrintSingleRecipe(self, which) :
        print("Entering PrintSingleRecipe with argument", which)
        sql = 'SELECT * FROM Recipes WHERE pkID = "%s"' % str(which)
        x = cursor.execute(sql)
        print ('------------------------------------------------------')
        for x in cursor.execute(sql):
            recipeid = x[0]
            print ("RecipeID: ", recipeid)
            print ("Title: " + x[1])
            print ("Serves: " + x[2])
            print ("Source: " + x[3])
            print ('--------------------------------------------------')

            sql = 'SELECT * FROM Ingredients WHERE RecipeID = %s ' \
                  % recipeid
            print('Ingredient List:')
            for x in cursor.execute(sql):
                print(x[1])
            print ('')

            print('Instructions:')
            sql = 'SELECT * FROM Instructions WHERE RecipeID = %s ' \
                  % recipeid
            for x in cursor.execute(sql):
                print(x[1])
            print ('----------------------------------------------------')

            resp = input('Press a key -> ')
        return

    def DeleteRecipe(self, which):
        print("Entering DeleteRecipe with argument", which)
        sql = 'DELETE from Recipes where pkID = "%s"' % str(which)
        cursor.execute(sql)
        return

    def EnterNew(self):
        print("Entering EnterNew")
        return

    def PrintOut(self, which):
        print("Entering PrintOut with argument", which)
        return

    def __init__(self):
        global connection
        global cursor
        self.totalcount = 0
        connection = apsw.Connection(
            "cookbook8.db3")
        cursor = connection.cursor()

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
        elif response == '4': # Delete Recipe
            cbk.DeleteRecipe(1)
        elif response == '5': # Add a recipe
            cbk.EnterNew()
        elif response == '6': # Print a recipe
            cbk.PrintOut(6)
        elif response == '0': # Exit the program
            print('Goodbye')
            loop = False
        else:
            print('Unrecognized command. Enter a number between 0 and 6.')

Menu()