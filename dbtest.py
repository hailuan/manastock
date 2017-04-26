import sqlite3


conn = sqlite3.connect('stock.db')
cursor = conn.cursor()
cursor.execute("""
insert into Products(code,name,price_purchase, price_new, price_sale)
values('C1', 'chen', 100, 100, 150);
""")

cursor.execute("""
insert into Products(code,name,price_purchase, price_new, price_sale)
values('C2', 'chenkieu', 110, 110, 150);
""")

cursor.execute("""
insert into Products(code,name,price_purchase, price_new, price_sale)
values('L1', 'ly', 50, 50, 100);
""")

cursor.execute("""
insert into Providers(name, adr, tel, desc) values('Nam','HCM',113,'nha cung 1')
""")

cursor.execute("""
insert into Providers(name, adr, tel, desc) values('Truc','HCM',114,'nha cung 2')
""")

cursor.executescript("""
insert into ProductFromProvider(idproduct,idprovider, amount, price) values(1,1,1,100);
insert into ProductFromProvider(idproduct,idprovider, amount, price) values(1,2,10,99);
insert into ProductFromProvider(idproduct,idprovider, amount, price) values(2,1,100,100);
insert into ProductFromProvider(idproduct,idprovider, amount, price) values(3,2,1,50);
""")

cursor.executescript("""
insert into Stock(location) values('A');
insert into Stock(location) values('B');
""")

cursor.executescript("""
insert into ManagerStock(idstock,idproduct,quantity) values(1,1,8);
insert into ManagerStock(idstock,idproduct,quantity) values(2,1,12);
insert into ManagerStock(idstock,idproduct,quantity) values(1,2,20);
insert into ManagerStock(idstock,idproduct,quantity) values(2,3,40);
""")

conn.commit()
conn.close()