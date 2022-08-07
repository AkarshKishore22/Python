import sqlite3
conn = sqlite3.connect('testdb.db')
conn.execute('''create table product (
productId INT PRIMARY KEY NOT NULL,
productName TEXT NOT NULL,
PRICE REAL NOT NULL,
MANUFACTURER TEXT NOT NULL,
QUANTITY INT NOT NULL,
CATEG TEXT NOT NULL);''')
listItems = [
(1, 'Apple', 200, 'ABC', 20, 'Fruit'),
(2, 'Orange', 100, 'ABD', 10, 'Fruit'),
(3, 'Butterflow', 10, 'AAA', 150, 'Pen')
]
conn.executemany("INSERT INTO product VALUES (?, ?, ?, ?, ?, ?)",
listItems)
conn.commit()
print('Database created successfully')
# Operation 01
data = conn.execute("SELECT * FROM product ORDER BY -PRICE")
count = 0
for i in data:
    if count == 3:
        break
print(i)
count+=1
# Operation 02
data = conn.execute("SELECT * FROM product WHERE MANUFACTURER = 'ABC' AND PRICE <= 200")
for i in data:
    print(i)
# Operation 03
data = conn.execute("SELECT * FROM product WHERE PRICE <= 200 and PRICE > 20")
for i in data:
    print(i)
# Operation 04
data = conn.execute("SELECT * FROM product")
count = 0
for i in data:
    count += 1
print(count)
# Operation 05
data = conn.execute("SELECT CATEG FROM product")
category = ""
for i in data:
    if(i[0] != category):
        print(i[0])
category = i[0]