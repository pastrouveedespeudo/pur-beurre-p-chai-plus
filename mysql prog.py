select * from customer;




#livreur
select customer.name, customer.number, customer.address, command.delay,
command.idProduct, product.name, product.price_product, command.ChoicePayment,
Linking_command_product.totalPrice
from customer
inner join command on command.id_customer = customer.id_customer
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on command.idProduct = product.id_product;
#-----

#serveur addition
select command.id_order, sum(product.price_product) as prix_command
from customer
inner join command on command.id_customer = customer.id_customer
inner join product on command.idProduct = product.id_product;

select idProduct,
price_product
from command
inner join customer on customer.id_customer = command.id_customer
inner join product on command.idProduct = product.id_product
where customer.id_customer = 1;
#------





#facture--
select bill.id_bill, bill.id_order, bill.price, bill.date_order,
command.id_customer, command.id_store, command.date,
Linking_command_product.id_product,
product.price_product
from bill
inner join command on command.id_order = bill.id_order
inner join Linking_command_product on Linking_command_product.id_order = command.id_order
inner join product on Linking_command_product.id_product = product.id_product;

select command.id_order, sum(product.price_product) as prix_command
from customer
inner join command on command.id_customer = customer.id_customer
inner join product on command.idProduct = product.id_product;
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
inner join product on product.id_product = Linking_cart_product.id_product;
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
select customer.id_customer, command.idProduct, product.name, product.picture
from command
inner join customer on customer.id_customer = command.id_customer
inner join Linking_command_product on Linking_command_product.id_order= command.id_order
inner join Product on product.id_product = Linking_command_product.id_product
where customer.id_customer = 2;


select customer.id_customer, command.idProduct, product.name, product.picture
from command
inner join customer on customer.id_customer = command.id_customer
inner join Linking_command_product on Linking_command_product.id_order= command.id_order
inner join Product on product.id_product = Linking_command_product.id_product
where customer.id_customer = 1;




















