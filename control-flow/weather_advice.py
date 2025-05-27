ch = input("What's the weather like today? (sunny/rainy/cold):").lower()

if ch == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif ch == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif ch == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
