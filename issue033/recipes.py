
import apsw

#Opening/creating database
connection=apsw.Connection("cookbook8.db3")
cursor=connection.cursor()

sql = 'CREATE TABLE Recipes (pkiD INTEGER PRIMARY KEY, \
       name TEXT, servings TEXT, source TEXT)'
cursor.execute(sql)

sql = 'CREATE TABLE Instructions (pkID INTEGER PRIMARY KEY, \
    instructions TEXT, recipeID NUMERIC)'
cursor.execute(sql)

sql = 'CREATE TABLE Ingredients (pkID INTEGER PRIMARY KEY, \
    ingredients TEXT, recipeID NUMERIC)'
cursor.execute(sql)

# INSERT SPANISH RICE
sql = 'INSERT INTO Recipes (name, servings, source) \
    VALUES ("Spanish Rice", "4", "Greg Walters")'
cursor.execute(sql)

sql = 'SELECT last_insert_rowid()'
cursor.execute(sql)

for x in cursor.execute(sql):
    lastid = x[0]
    print ("lastid = ", lastid)

'''
sql = 'INSERT INTO Instructions (recipeID, instructions) ' \
    + 'VALUES (%s, "Brown hamburger. Stir in all other ingredients. " \
    + "Bring to a boil.  Stir.  Lower to simmer. " \
    + "Cover and cook for 20 minutes or until all liquid is absorbed.")' \
      % lastid
cursor.execute(sql)
'''
sql = '''INSERT INTO Instructions (recipeID, instructions) \
      VALUES (%s, "Brown hamburger. Stir in all other ingredients.   \
      Bring to a boil.  Stir.  Lower to simmer. ")''' \
      % lastid
cursor.execute(sql)

# Now the ingredients
sql = 'INSERT INTO Ingredients (recipeID, ingredients) ' \
      'VALUES (%s, "1 cup parboiled Rice (uncooked)")' \
      % lastid
cursor.execute(sql)

# INSERT BOILED MILK
sql = '''INSERT INTO Recipes (name, servings, source) \
    VALUES ("Boiled Milk", "8", "Bob Cannon")'''
cursor.execute(sql)

sql = 'SELECT last_insert_rowid()'
cursor.execute(sql)

for x in cursor.execute(sql):
    lastid = x[0]
    print ("lastid = ", lastid)

# INSERT RAISIN BRAN
sql = 'INSERT INTO Recipes (name, servings, source) \
    VALUES ("Raisin Bran", "1", "Bob Cannon")'
cursor.execute(sql)

sql = 'SELECT last_insert_rowid()'
cursor.execute(sql)

for x in cursor.execute(sql):
    lastid = x[0]
    print ("lastid = ", lastid)

'''
# First the instructions
sql = 'INSERT INTO Instructions (recipeID, instructions) ' \
    + 'VALUES (%s, "Brown hamburger. Stir in all other ingredients. " \
    + "Bring to a boil.  Stir.  Lower to simmer. " \
    + "Cover and cook for 20 minutes or until all liquid is absorbed.")' \
    %lastid
cursor.execute(sql)

# Now the ingredients
sql = 'INSERT INTO Ingredients (recipeID,ingredients) '\
    + 'VALUES ( %s, "1 cup parboiled Rice (uncooked)")' \
    % lastid
cursor.execute(sql)
'''