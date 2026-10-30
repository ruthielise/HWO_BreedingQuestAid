import sqlite3

# open a connection to database files, which will be created once this script is run
conn = sqlite3.connect("BreedingQuests.db")

# open the schema.sql files and execute the contents using the executescript() method that executes multiple SQL statements at once, 
# this will create the two tables.
with open("schema1.sql") as database_schema:
    conn.executescript(database_schema.read())
    
# create a cursor object which allows us to process rows in a database.
cur = conn.cursor()

# create array of content for breeding partner database and insert data
with open("pre_database_BreedingPartnerRequirements.csv") as file1:
  loop = 1;
  dummy = file1.readline();
  while(true):
    loop += 1;
    input = file1.readline();
    if input = file1.readline() != null:
      data = input.split(',');
      if len(data) < 4:
        print("Line " + str(loop) + " could not be parsed.");
        continue;
      else:
        cur.execute("INSERT INTO breeding_partners (name, crossbreed_bool, partner1, partner2) VALUES (?, ?, ?, ?)", (data[0], data[1], data[2], data[3]);
    else:
      file1.close();
      break;
        
# create array of content for quest cascade database and insert data
with open("pre_database_QuestUnlockCascade.csv") as file2:
  loop = 1;
  dummy = file2.readline();
  while(true):
    loop += 1;
    input = file2.readline();
    if input = file2.readline() != null:
      data = input.split(',');
      if len(data) < 3:
        print("Line " + str(loop) + " could not be parsed.");
        continue;
      else:
        cur.execute("INSERT INTO quest_cascade (name, unlocks_bool, unlocked_by) VALUES (?, ?, ?)", (data[0], data[1], data[2]);
    else:
      file2.close();
      break;

# commit the changes to the database and close the connection
conn.commit()
conn.close()
