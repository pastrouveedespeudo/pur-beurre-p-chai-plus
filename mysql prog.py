select * from customer;




#livreur
select customer.name, customer.number, customer.address,
command.id_order,
product.name,product.price_product

from customer

inner join command on command.id_customer = customer.id_customer
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on product.id_product = Linking_command_product.id_product

where command.id_order = 1;


select customer.name, customer.number, customer.address,
command.id_order,
product.name,product.price_product

from customer

inner join command on command.id_customer = customer.id_customer
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on product.id_product = Linking_command_product.id_product

where command.id_order = 2;


#-----

#serveur addition
select command.id_order, sum(product.price_product) as prix_command
from customer

inner join command on command.id_customer = customer.id_customer
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on product.id_product = Linking_command_product.id_product

where customer.id_customer = 2;

select command.id_order, sum(product.price_product) as prix_command
from customer

inner join command on command.id_customer = customer.id_customer
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on product.id_product = Linking_command_product.id_product

where customer.id_customer = 1;



select customer.name, customer.id_customer,
Product.Price_product , Product.name, Product.id_product
from customer

inner join Command as commande on commande.id_customer = customer.id_customer
inner join Linking_command_product on commande.id_order = Linking_command_product.id_order
inner join Product on Linking_command_product.id_product = Product.id_product

where customer.id_customer = 1;
#------





#facture detail
select bill.id_bill, bill.id_order, bill.price, bill.date_order,
command.id_customer, command.id_store, command.date,
Linking_command_product.id_product,
product.price_product

from bill

inner join command on command.id_order = bill.id_order
inner join customer on command.id_customer = customer.id_customer
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on Linking_command_product.id_product = product.id_product

where customer.id_customer = 2;


#prix total facture
select command.id_order, sum(product.price_product) as prix_command
from customer
inner join command on command.id_customer = customer.id_customer
inner join Linking_command_product on command.id_order = Linking_command_product.id_order
inner join product on Linking_command_product.id_product = product.id_product
where customer.id_customer = 2;




#--------



#panier
select customer.id_customer,
cart.id_cart,
Linking_cart_product.id_product,
Product.price_product,
Linking_cart_product.totalPrice
from customer
inner join cart on cart.id_customer = customer.id_customer
inner join Linking_cart_product on Linking_cart_product.id_cart = cart.id_cart
inner join product on product.id_product = Linking_cart_product.id_product
where customer.id_customer = 2;
#---------------------


#produit et aide mémoire
select product.name, help_memo.nameMemo, product.picture,
help_memo.description
from product
inner join help_memo on help_memo.id_product = product.id_product
where product.id_product = 1;


select distinct product.id_product
from Linking_product_ingredient
inner join product on product.id_product = Linking_product_ingredient.id_product
where product.id_product = 1;



select Ingredient.id_ingredient, Ingredient.name
from Linking_product_ingredient
inner join Ingredient on Ingredient.id_ingredient = Linking_product_ingredient.id_ingredient
inner join product on product.id_product = Linking_product_ingredient.id_product
where product.id_product = 1;

#-----------------------

#ou chercher les ingredients ?

select ingredient.name, ingredient.id_stock,
stock.id_stock
from ingredient
inner join stock on stock.id_stock = ingredient.id_stock;

#---------------

#gerer les stock:
select id_stock, statut, quantity
from stock
where id_stock = 1;

select id_stock, statut, quantity
from stock
where id_stock = 2;


select id_stock, statut, quantity
from stock
where id_stock = 3;
#---------------





#liste commande
select distinct customer.id_customer
from command
inner join customer on customer.id_customer = command.id_customer;
#-----------------


#appuie sur l'une des commandes
select customer.id_customer, command.id_order, product.name, product.picture
from customer
inner join command on customer.id_customer = command.id_customer
inner join Linking_command_product on Linking_command_product.id_order= command.id_order
inner join Product on product.id_product = Linking_command_product.id_product
where customer.id_customer = 1;


select customer.id_customer, command.id_order, product.name, product.picture
from customer
inner join command on customer.id_customer = command.id_customer
inner join Linking_command_product on Linking_command_product.id_order= command.id_order
inner join Product on product.id_product = Linking_command_product.id_product
where customer.id_customer = 1;
#--------------


#category d'un produit ?
select product.name, product.price_product, product.picture,
category_product.name
from category_product
inner join Linking_product_category_product on category_product.id_category = Linking_product_category_product.Id_category
inner join Product on Product.id_product = Linking_product_category_product.id_product
where product.id_product = 1;

select product.name, product.price_product, product.picture,
category_product.name
from category_product
inner join Linking_product_category_product on category_product.id_category = Linking_product_category_product.Id_category
inner join Product on Product.id_product = Linking_product_category_product.id_product
where product.id_product = 5;

select product.name, product.price_product, product.picture,
category_product.name
from category_product
inner join Linking_product_category_product on category_product.id_category = Linking_product_category_product.Id_category
inner join Product on Product.id_product = Linking_product_category_product.id_product
where product.id_product = 6;
#-----------------

#qui est dans mon magasin ?
select Oc_Pizzeria.namestore,
staff.name, staff.id_store, staff.picture,
permission.access, permission.name

from Oc_Pizzeria

inner join staff on staff.id_store = Oc_Pizzeria.id_store

inner join permission on permission.id_access = staff.id_access

where Oc_Pizzeria.id_store = 1;


















