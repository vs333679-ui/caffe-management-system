print("☕︎_WELCOME TO MY CAFETERI︎A_☕︎")
menu=[]
def show_menu():
    print("❀---MENU---❀")
    for item,price in menu:
        print(item,price)
        
def add_item(item,price):
    menu.append((item,price))

add_item("tea",100)
add_item("coffee",500)
add_item("burger",250)
add_item("pizza",500)
add_item("noodles",120)
add_item("pastry",50)
add_item("chilli potato",60)
add_item("oreo shake",55)
add_item("french fries",80)
add_item("cruison",575)

def take_order():
    total=0
    while True:
        choice=input("Enter item name (done to stop): ").strip().lower()
        if choice.lower()=="done":
            break
        found=False
        for item ,price in menu:
            if item.lower()==choice:
                qty=int(input("Enter quantity="))
                total+=price*qty
                found =True
                break
        if not found:
            print("item not found")
    
    print("your total bill:",total)
show_menu()        
take_order()
print("\n❤️_THANYOU FOR VISITING OUR CAFETERIA_❤️")
print("---VISIT AGAIN---")
print("°☆𝙲𝚘𝚏𝚏𝚎★ ☕️✨️")
