def order(dish):
    return "Your order: " + dish 

def process_order(dish, func):
    print(func(dish))

process_order ("Spaghettie", order)