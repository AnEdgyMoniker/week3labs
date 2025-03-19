# %% [markdown]
# # Final Fantasy 7: Vending Machine Code
# ### Brandon Kittle
# ### 03/18/2025
# 
# First I aplogize for the late turn in, I was pushing myself to try and utilize some type of formating for this and wanted to make this as clean as possible. I try to take the assignments and create more of a dynamic enviroment for me to play in, while understandin the simple concepts of the assignment. I want to create something more unique to challange my skill level and understanding of the concepts. Think, expanding upon the current assignment. However, I also want to have fun and create something I actually enjoy writing as well. I hope you enjoy this as much as I did creating it.

# %%
import os

# Function to clear the terminal 
#def clear_terminal():
    #os.system('cls' if os.name == 'nt' else 'clear')

# Note book clear function 
from IPython.display import clear_output

def clear_terminal():
    clear_output(wait=True)


# %% [markdown]
# Doing some quick research, as this was my first time doing this in python specifically for osx/windows, I found that this allows clearing of terminal outputs in Jupyter Notebooks. I did pull this concept from stack exchange. This was my first time making sure that the terminal could clear whether it was os or Nt (windows due to NT kernal). First, we defined the clear function so this code is much simipler to use on the fly. Saves memory, and makes it easier to read. We use the ternary operator for a conditional expression to decide if the command we are giving is 'cls' or 'clear'. 
# 
# Edit: I did not realize that the notebook has a truncated terminal. Due to this, I implemented a clear function for the terminal rather then based on OS. However, if this program was ran directly for the terminal in a py function. The clear functions should be swapped above!
# 
# Next, we will create the product class below.
# ## Product Class 

# %%
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self):
        return f"{self.name} - {self.price} gil"


# %% [markdown]
# The class is pretty simple. We define all the characteristics we need to have for each product as asked. Name, price, and I included category. This will allow us to sort the products by category... or menu *hint hint*. We then also create a function to print the product. Save us time in formating, and makes it easier to read. 
# 
# As I said above. I wanted to press myself to create a more complex enviroment. I wanted to reengineer one of my favorite kiosks. Vending machines or venders in Final Fantasy Games. However, we use menus to seperate the items that are purchasable with the ingame currency (Gil). Due to this, we need to create a product menu that categorizes the items. In c++ we used to call these node theories. They are really cool since you can actually items to level progression, or area unlocks. That way when you open a vending menu, you can create a unique experience for the player. Anywho, enough rambeling. Lets program. 
# 
# ## Products Menu

# %%
# Define Products
items = [
    Product("Potion", 50, "Item"),
    Product("Hi-Potion", 300, "Item"),
    Product("Ether", 1500, "Item"),
    Product("Phoenix Down", 500, "Item"),
]

weapons = [
    Product("Buster Sword", 1200, "Weapon"),
    Product("Mythril Saber", 3000, "Weapon"),
]

armor = [
    Product("Iron Bangle", 350, "Armor"),
    Product("Titan Bangle", 500, "Armor"),
]

materia = [
    Product("Fire", 600, "Materia"),
    Product("Ice", 600, "Materia"),
    Product("Lightning", 600, "Materia"),
    Product("Cure", 400, "Materia"),
]

# Combine into one list for easy handling
all_products = items + weapons + armor + materia


# %% [markdown]
# Now we will need to create a way to represent the menu. I originally had this below in the main body, but I wasn't getting the results I wanted. Some new line errors with the clearing function within the loop was making it difficult to read. Creating storage containers to carry over lines of text was just cumbersome and confusing. So we stopped, and created a display function. In such ways, we are kinda creating a class without the class features. Almost like a wrapper or interface in java. We need to be able to cleanly pass the display function of the menu contaning class objects. 

# %%
def display_menu():
    print("\n--- Welcome to the Shinra Company Vending Machine! ---")
    print("1. Items")
    print("2. Weapons")
    print("3. Armor")
    print("4. Materia")
    print("5. Checkout")


# %% [markdown]
# Now products. Catch? We need to make sure we are sorting by category. For this we will use a loop naturally. 

# %%
def display_products(category):
    print(f"\n--- {category} ---")
    products = [p for p in all_products if p.category == category]
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")
    print("0. Go Back")

# %% [markdown]
# Now this I would define as a true interface and wrapper for the product class. The shopping cart class. We need to be able to add items to the cart based of user interaction and contain the total price. Additionally, we need to display the cart. 
# 
# ## Shopping Cart

# %%
class ShoppingCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity
    
    def display_cart(self):
        print("\n--- Your Order ---")
        total = 0
        for product, quantity in self.cart.items():
            cost = product.price * quantity
            print(f"{product.name} x{quantity} - {cost} gil")
            total += cost
        print(f"Total: {total} gil")

    def get_total(self):
        return sum(product.price * quantity for product, quantity in self.cart.items())


# %% [markdown]
# The cart itself is a dictonary. I wanted to make sure we could add multiple items, remove, and have an easy way to interact with the cart as the wrapper. Key value pairs seemed the way to go rather then a list of objects that would create iterative searching, or creating dynamic searches as the object grows. Key values make a wonderful unique identifier to handle this information. 
# 
# Then we created the Add_to_cart function. Fairly self explanatory. 
# 
# Display cart to create neat formating. 
# 
# Then get total. This will make an auto acumulator for the total price of the cart. Coding that likely will be repeatitive. 
# 
# Next will be our main brick and mortar of the function. The logic of the kiosk. 
# 
# ## Kiosk Logic

# %%
def main():
    global cart 
    cart = ShoppingCart()
    while True:
        display_menu()
        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            category = 'Item'
        elif choice == '2':
            category = 'Weapon'
        elif choice == '3':
            category = 'Armor'
        elif choice == '4':
            category = 'Materia'
        elif choice == '5':
            clear_terminal()
            cart.display_cart()
            print("\nThank you for your purchase! See you again!")
            break
        else:
            print("\nThat is not an option. Please try again.")
            input("\nPress Enter to continue...")
            continue
        
        # ✅ Display products before the user makes a choice
        while True:
            display_products(category)
            product_choice = input("\nSelect an item to add to cart (0 to go back): ").strip()

            if product_choice == '0':
                clear_terminal()
                break
            
            try:
                product_index = int(product_choice) - 1
                products = [p for p in all_products if p.category == category]
                
                if 0 <= product_index < len(products):
                    product = products[product_index]
                    quantity = int(input(f"How many {product.name} would you like? "))
                    
                    if quantity > 0:
                        # ✅ Pass a copy to avoid modifying the original object
                        cart.add_to_cart(product, quantity)
                        clear_terminal()
                        print(f"\n{quantity} x {product.name} added to cart.")
                        input("\nPress Enter to continue...")
                    else:
                        print("\nInvalid quantity. Must be greater than 0.")
                        input("\nPress Enter to continue...")
                else:
                    print("\nInvalid selection.")
                    input("\nPress Enter to continue...")

            except ValueError:
                print("\nInvalid input. Please enter a number.")
                input("\nPress Enter to continue...")


# %% [markdown]
# Wouldn't be me if I didn't seperate the initilization of the program. So, below shall run our main to see the program completed. However, ask asked we used string and made sure to include options for invalid entries. Like prior programs, I'm more of a fan of try Catch blocks. I find them more efficient and cleaner to read. However, for the purposes of this assignment, we will use if else statements.
# 
# ## Start the kiosk

# %%
if __name__ == "__main__":
    main()

# %% [markdown]
# One thing I haven't figured out yet is how to clear out the terminal prior to the start of the program. What is happening is on a test run, depending how I escaped the program, the terminal will not populate the opening menu. If this happens I'm sorry, I found out this was due to the notebook. Please clear all outputs and start the notebook fresh! 
# 
# I was also having issues with truncating menus and had to adjust my clear function to work with the notebook using the direct library from the notebook instead of the system library for mac/windows. 


