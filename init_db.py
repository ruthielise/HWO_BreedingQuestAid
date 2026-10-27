import sqlite3

# open a connection to a database file named database.db, which will be created once this script is run
conn1 = sqlite3.connect("BreedingPartners.db")
conn2 = sqlite3.connect("QuestCascade.db")

# open the schema.sql file and execute its contents using the executescript() method that executes multiple SQL statements at once, 
# this will create the breeding partners table.
with open("schema1.sql") as database_schema:
    conn1.executescript(database_schema.read())

# this will create the quest cascade table.
with open("schema2.sql") as database_schema:
    conn2.executescript(database_schema.read())
# create a cursor object which allows us to process rows in a database.
cur1 = conn1.cursor()
cur2 = conn2.cursor()
# create array of content for breeding partner database and insert data
with open("pre_database_BreedingPartnerRequirements.csv") as file1:
  loop = 0;
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
        cur1.execute("INSERT INTO breeding_partners (name, crossbreed_bool, partner1, partner2) VALUES (?, ?, ?, ?)", (data[0], data[1], data[2], data[3]);
    else:
      break;
        
# create array of content for quest cascade database and insert data
with open("pre_database_QuestUnlockCascade.csv") as file2:
  loop = 0;
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
        cur2.execute("INSERT INTO quest_cascade (name, unlocks_bool, unlocked_by) VALUES (?, ?, ?)", (data[0], data[1], data[2]);
    else:
      break;

# commit the changes to the database and close the connection
conn1.commit()
conn2.commit()
conn1.close()
conn2.close()
