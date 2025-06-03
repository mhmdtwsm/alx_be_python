def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter an item to add: ")
            shopping_list.append(item)
            # Prompt for and add an item
            pass
        elif choice == "2":
            item = input("Enter name of itme to remove: ")
            if item not in shopping_list:
                print("item not in the list\n")
            else:
                shopping_list.remove(item)
            pass
            # Prompt for and remove an item
            pass
        elif choice == "3":
            for i in shopping_list:
                print(i)
            # Display the shopping list
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
