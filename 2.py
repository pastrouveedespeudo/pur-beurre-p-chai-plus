INSERT INTO Customer (Name,FirstName,Mail,Address,Number,Password,Identification,Date,Sexe)
VALUES("jb", "servais", "jb26400@hotmail.fr", "monaco","0606060606","yoyo", "alitoo", "2010:02:02 12:12:12","m");

INSERT INTO Customer (Name,FirstName,Mail,Address,Number,Password,Identification,Date,Sexe)
VALUES("jean baptiste", "servais", "jb26400@gmail.fr", "aouste","0606060605","yoyo", "bouboule", "2010:02:02 12:12:12","m");

INSERT INTO Cart(id_customer) 
VALUES(1);

INSERT INTO Cart(id_customer) 
VALUES(2);

INSERT INTO Oc_Pizzeria (Name_director, Phone_number, Mail, Address, SiteWeb, NameStore, StatutStore)
VALUES("DOCTOR No", "060606", "directeur@hot","yoyo rue yoyo", "My_profil", "Ocpizzeria", "open");







INSERT INTO Command (Id_customer, Id_store, Type_order, State_order, Price, Date, Delay, Commentary, ChoicePayment)
VALUES(1, 1, "sur place", "en cours", 50, "2010:02:02 12:12:12", "20 minutes", "pas d'olive","carte");

INSERT INTO Command (Id_customer, Id_store, Type_order, State_order, Price, Date, Delay, Commentary, ChoicePayment)
VALUES(2, 1, "a emporté", "en cours", 10, "2010:02:02 12:12:12", "15 minutes", "double tomate, extra olive","espece");






INSERT INTO Bill (Id_order, Price, Date_order)
VALUES(1, 50, "2010:02:02 12:12:12");

INSERT INTO Bill (Id_order, Price, Date_order)
VALUES(2, 10, "2010:02:02 12:12:12");



Insert INTO Staff (Id_store, Id_access, Name, Address, Mail, Number, Date_add, FirstName, Password, Identification, Sexe)
VALUES(1,1, "robert", "robert villle", "robertdu91@yahou.com", "0606", "10-10-10 10:26:26", "noel", "crobert123","roro","m" );

Insert INTO Staff (Id_store, Id_access, Name, Address, Mail, Number, Date_add, FirstName, Password, Identification, Sexe)
VALUES(1,2, "jo","robert villle", "robertdu91@yahou.com", "060604", "10-10-10 10:26:26", "noel", "crdert123","roro","m" );

Insert INTO Staff (Id_store, Id_access, Name, Address, Mail, Number, Date_add, FirstName, Password, Identification, Sexe)
VALUES(1,3, "mick","robert villle", "robertdu91@yahou.com", "060609", "10-10-10 10:26:26", "noel", "crozrt123","roro","m" );



Insert INTO Permission (Access, Name)
VALUES("1","cuisinier");

Insert INTO Permission (Access, Name)
VALUES("2","serveur");

Insert INTO Permission (Access, Name)
VALUES("3", "livreur");

Insert INTO Permission (Access, Name)
VALUES("4","directeur");



INSERT INTO Category_product (Name, Description)
VALUES("pizza", "produit fare");

INSERT INTO Category_product (Name, Description)
VALUES("soda", "coca, limonade");


INSERT INTO Category_product (Name, Description)
VALUES("dessert","gateau, glace");



INSERT INTO Stock (statut, quantity)
VALUES("plein", "250");

INSERT INTO Stock (statut, quantity)
VALUES("vide","300");

INSERT INTO Stock (statut, quantity)
VALUES("moitié","6000");

INSERT INTO Stock (statut, quantity)
VALUES("moitié","6000");


INSERT INTO Stock (statut, quantity)
VALUES("moitié","6000");

INSERT INTO Stock (statut, quantity)
VALUES("moitié","6000");




INSERT INTO Ingredient (id_stock,Name)
VALUES(1, "jambon");


INSERT INTO Ingredient (id_stock,Name)
VALUES(5, "gruyere");


INSERT INTO Ingredient (id_stock,Name)
VALUES(4,"pate");


INSERT INTO Ingredient (id_stock,Name)
VALUES(2, "tomate cerise");


INSERT INTO Ingredient (id_stock,Name)
VALUES(3, "morue dalsace");


INSERT INTO Product (Name, Price_product, Description, Picture)
VALUES("pizza tomate", 10, "super bonne", "pizza tomate.jpg");

INSERT INTO Product (Name, Price_product, Description, Picture)
VALUES("pizza Mozza",10,"chesse car", "pizza Mozza.jpg");

INSERT INTO Product (Name, Price_product, Description, Picture)
VALUES("pizza anchois", 10, "base tomate", "anchois.jpg");

INSERT INTO Product (Name, Price_product, Description, Picture)
VALUES("pizza du chef", 10, "base tomate","chef.jpg");

INSERT INTO Product (Name, Price_product, Description, Picture)
VALUES("canette coca", 5, "10 cl", "canettecoca.jpg");

INSERT INTO Product (Name, Price_product, Description, Picture)
VALUES("glace mmns", 5, "pot", "glace mmns.jpg");


INSERT INTO Help_memo (Id_product, Description,Picture,NameMemo, Date)
VALUES(1, "Faire la cuisson en premier", "Pizza tomate Memo.png", "tomateMemo", "10-10-10 10:26:26");


INSERT INTO Claim (Id_order,MessageClaim, TypeClaim, IdCustomer, IdStore, ObjectClaim, Description)
VALUES(1,"Bonjour ... Cordialement","prix", 1, 1, "canette 1euro de plus", "canette coca un euro de plus");





insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(1,1,1,50);

insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(1,2,1,50);

insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(1,3,1,50);

insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(1,4,1,50);

insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(1,5,1,50);

insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(1,6,1,50);


insert into Linking_command_product (id_order, id_product, quantity, totalPrice)
value(2,6,1,10);



insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (1,1,1,50);

insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (1,2,1,50);

insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (1,3,1,50);

insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (1,4,1,50);

insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (1,5,1,50);

insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (1,6,1,50);


insert into Linking_cart_product (id_cart, id_product, quantity, totalPrice)
values (2,6,1,10);




insert into Linking_command_oc_pizzeria (id_order, id_store)
values(1,1);







insert into Linking_product_ingredient(id_product, id_ingredient)
values(1,1);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(1,2);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(1,3);


insert into Linking_product_ingredient(id_product, id_ingredient)
values(1,4);



insert into Linking_product_ingredient(id_product, id_ingredient)
values(2,1);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(2,2);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(2,3);


insert into Linking_product_ingredient(id_product, id_ingredient)
values(2,4);


insert into Linking_product_ingredient(id_product, id_ingredient)
values(4,1);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(4,2);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(4,3);


insert into Linking_product_ingredient(id_product, id_ingredient)
values(4,4);

insert into Linking_product_ingredient(id_product, id_ingredient)
values(4,5);


