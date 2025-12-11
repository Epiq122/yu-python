print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

price = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_on_small_price = 2
pepperoni_on_med_or_large_price = 3
extra_cheese_price = 1

if size == "s":
    price += small_pizza
    if pepperoni == "y":
        price += pepperoni_on_small_price

    if extra_cheese == "y":
        price += extra_cheese_price
    print(f"Your final bill is: ${price}.")


elif size == "m":
    price += medium_pizza

    if pepperoni == "y":
        price += pepperoni_on_med_or_large_price

    if extra_cheese == "y":
        price += extra_cheese_price

    print(f"Your final bill is: ${price}.")


elif size == "l":
    price += large_pizza

    if pepperoni == "y":
        price += pepperoni_on_med_or_large_price

    if extra_cheese == "y":
        price += extra_cheese_price

    print(f"Your final bill is: ${price}.")
