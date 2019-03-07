CREATE TABLE IF NOT EXISTS Customer(
Id_customer INTEGER NOT NULL AUTO_INCREMENT,
Name VARCHAR(30) NOT NULL,
FirstName VARCHAR(30) NOT NULL,
Mail VARCHAR(30) NOT NULL UNIQUE,
Address TINYTEXT NOT NULL,
Number VARCHAR(10) NOT NULL,
Password VARCHAR(30) NOT NULL,
Identification VARCHAR(30) NOT NULL,
Date DATETIME NOT NULL,
Picture MEDIUMBLOB ,
Sexe VARCHAR(1) NOT NULL,

PRIMARY KEY(Id_customer) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Cart(
Id_cart INTEGER NOT NULL AUTO_INCREMENT,

Id_customer INTEGER NOT NULL UNIQUE,

PRIMARY KEY(Id_cart))

ENGINE=InnoDB ;	





CREATE TABLE IF NOT EXISTS Product(

Id_product INTEGER NOT NULL AUTO_INCREMENT, 

Name VARCHAR(25) NOT NULL UNIQUE,
Price_product INT,
Description TINYTEXT NOT NULL,
Picture MEDIUMBLOB NOT NULL,

PRIMARY KEY(Id_product) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Linking_cart_product(

Id_cart INTEGER NOT NULL,
Id_product INTEGER NOT NULL, 

Quantity VARCHAR(30) NOT NULL,
TotalPrice VARCHAR(10),

PRIMARY KEY(Id_cart, Id_product) )

ENGINE=InnoDB ;	





CREATE TABLE IF NOT EXISTS Command(
Id_order INTEGER NOT NULL AUTO_INCREMENT,

Id_customer INTEGER NOT NULL,
Id_store INTEGER NOT NULL,
Type_order VARCHAR(15) NOT NULL,
State_order VARCHAR(10),
IdProduct INT NOT NULL,
Price INTEGER NOT NULL,
Date DATETIME NOT NULL,
Delay VARCHAR(10) NOT NULL,
Commentary TINYTEXT,
ChoicePayment VARCHAR(10) NOT NULL,

PRIMARY KEY(Id_order) )

ENGINE=InnoDB ;	





CREATE TABLE IF NOT EXISTS Bill(

Id_bill INTEGER NOT NULL AUTO_INCREMENT,

Id_order INTEGER NOT NULL,
Price INTEGER NOT NULL,
Date_order TIMESTAMP NOT NULL,

PRIMARY KEY(Id_bill) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Claim(


Id_Claim INTEGER NOT NULL AUTO_INCREMENT,

Id_order INTEGER NOT NULL,
MessageClaim TINYTEXT NOT NULL,
TypeClaim VARCHAR(50) NOT NULL,
IdCustomer INTEGER NOT NULL UNIQUE,
IdStore INTEGER NOT NULL UNIQUE,
ObjectClaim VARCHAR(50) NOT NULL,
Description TINYTEXT NOT NULL,

PRIMARY KEY(Id_Claim) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Oc_Pizzeria(

Id_store INTEGER NOT NULL AUTO_INCREMENT,

Name_director VARCHAR(30) NOT NULL,
Phone_number VARCHAR(10) NOT NULL UNIQUE,
Mail VARCHAR(30) NOT NULL,
Address VARCHAR(100) NOT NULL,
SiteWeb VARCHAR(50) NOT NULL,
NameStore VARCHAR(10) NOT NULL,
StatutStore VARCHAR(10) NOT NULL,

PRIMARY KEY(Id_store) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Linking_command_oc_pizzeria(

Id_order INTEGER NOT NULL, 
Id_store INTEGER NOT NULL,

PRIMARY KEY(Id_order, Id_store) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Staff(

Id_staff INTEGER NOT NULL AUTO_INCREMENT,

Id_store INTEGER NOT NULL,
Id_access INTEGER NOT NULL UNIQUE,
Name VARCHAR(20) NOT NULL,
Address VARCHAR(50) NOT NULL,
Mail VARCHAR(20) NOT NULL,
Number VARCHAR(10) NOT NULL UNIQUE,
Date_add TIMESTAMP,
FirstName VARCHAR(30) NOT NULL,
Password VARCHAR(30) NOT NULL,
Identification VARCHAR(30) NOT NULL,
Picture MEDIUMBLOB,
Sexe VARCHAR(1) NOT NULL,

PRIMARY KEY(Id_staff) )

ENGINE=InnoDB ;	





CREATE TABLE IF NOT EXISTS Permission(

Id_access INTEGER NOT NULL AUTO_INCREMENT,

Access VARCHAR(3) NOT NULL,
NAME VARCHAR(30) NOT NULL,

PRIMARY KEY(Id_access) )

ENGINE=InnoDB ;	






CREATE TABLE IF NOT EXISTS Linking_command_product(

Id_order INTEGER NOT NULL,
Id_product INTEGER NOT NULL,

Quantity VARCHAR(30) NOT NULL,
TotalPrice VARCHAR(10),

PRIMARY KEY(Id_order, Id_product) )

ENGINE=InnoDB ;	





CREATE TABLE IF NOT EXISTS Category_product(

Id_category INTEGER NOT NULL AUTO_INCREMENT,

Name VARCHAR(30) NOT NULL UNIQUE,
Description TINYTEXT NOT NULL,

PRIMARY KEY(Id_category) )

ENGINE=InnoDB ;	





CREATE TABLE IF NOT EXISTS Linking_product_category_product(

Id_category INTEGER NOT NULL,
Id_product INTEGER NOT NULL,

PRIMARY KEY(Id_category, Id_product) )

ENGINE=InnoDB ;





CREATE TABLE IF NOT EXISTS Help_memo(

Id_help INTEGER NOT NULL AUTO_INCREMENT,

id_product INTEGER NOT NULL,
Description LONGTEXT NOT NULL,
Picture MEDIUMBLOB NOT NULL,
NameMemo VARCHAR(30) NOT NULL,
Date DATETIME NOT NULL,

PRIMARY KEY(Id_help) )

ENGINE=InnoDB ;





CREATE TABLE IF NOT EXISTS Stock(

Id_stock INTEGER NOT NULL AUTO_INCREMENT,

Statut VARCHAR(20),
Quantity VARCHAR(5) NOT NULL,

PRIMARY KEY(Id_stock) )

ENGINE=InnoDB ;





CREATE TABLE IF NOT EXISTS Ingredient(

Id_ingredient INTEGER NOT NULL AUTO_INCREMENT,

Id_stock INTEGER NOT NULL, 
Name VARCHAR(20) UNIQUE,

PRIMARY KEY(Id_ingredient) )

ENGINE=InnoDB ;





CREATE TABLE IF NOT EXISTS Linking_product_ingredient(

Id_product INTEGER NOT NULL,
Id_ingredient INTEGER NOT NULL,

PRIMARY KEY(Id_product, Id_ingredient) )

ENGINE=InnoDB ;
