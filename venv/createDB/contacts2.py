import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET phone=8055319222 WHERE contacts.name = 'Mahesh'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.commit()

db.close()