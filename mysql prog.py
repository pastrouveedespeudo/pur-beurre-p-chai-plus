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
































