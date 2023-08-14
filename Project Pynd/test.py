import sqlite3

conn = sqlite3.connect("items.db")
cursor = conn.cursor()

# all = cursor.execute("SELECT * FROM items")
# for i in all:
#     print(i)

excallibur_desc = cursor.execute("SELECT desc FROM items WHERE name = 'Excallibur'")
for i in excallibur_desc:
    with open(f'item_descriptions/{i[0]}', 'r') as f:
        contents = f.read()
        print(contents)


conn.close()