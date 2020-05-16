from pizzapy import Customer,StoreLocator,Order,ConsoleInput

#customer=Customer("sakthi","ratnam","sakthi@gmail.com","9629356457","40 Bay St,Toronto,ON,M5J2X2")
customer=ConsoleInput.get_customer()

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print("closest store:\n")
print(my_local_dominos)

ans=input("would you like to order in this store (y/n)")
if ans.lower() not in ["yes","y"]:
	print("goodbye")
	quit()
print("\nMenu\n")

menu=my_local_dominos.get_menu()

def searchMenu(menu):
	print("you are now searching in the menu")
	
	item=input("type an item to look for").strip().lower()
	if len(item)>1:
		item=item[0].upper()+item[1:]
		print(f"Results for :{item}")
		menu.search(Name=item)
	else:
		print("invalid,existing search")


def addTOOrder(order):
	print("please type the codes of the item u like to order")
	while True:
		item=input("code: ").upper()
		try:
			order.add_item(item)
		except:
			if item=="":
				break
			print("Invalid code")

order=Order.begin_customer_order(customer,my_local_dominos,"ca")
while True:
	searchMenu(menu)
	addTOOrder(order)
	answer=input("would you like to continue (y/n)?")
	if answer.lower() not in ["yes","y"]:
		break

print("\n your order is as follows")
total=0
for item in order.data["Products"]:
	price=item["Price"]
	print(item["Name"]+ "$" + price)
	total+=float(price)
print(f"your total order price is {str(total)}")
payment=input("\n will you payong cash ")
if payment.lower() in ["card","creditcard"]:
	card=ConsoleInput.get_credit_card()
else:
	card=False
ans=input("would you like to place the order (y/n) ?")
if ans.lower() in ["y","yes"]:
	order.place(card)
	my_local_dominos.place_order(order, card,"in")
	print("Order Placed!")
else:
	print("good bye")

