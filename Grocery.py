grocery_list = []

def grocery_program(grocery_list):
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. View items")
        print("3. Remove item")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            # Add item
            item = input("Enter the item to add: ")
            grocery_list.append(item)
            print(f"{item} has been added to the list.")
            
        elif choice == "2":
            # View items
            if grocery_list:
                print("\nGrocery List:")
                for i, item in enumerate(grocery_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The grocery list is empty.")
                
        elif choice == "3":
            # Remove item
            if grocery_list:
                print("\nGrocery List:")
                for i, item in enumerate(grocery_list, start=1):
                    print(f"{i}. {item}")
                
                try:
                    item_number = int(input("Enter the number of the item to remove: "))
                    if 1 <= item_number <= len(grocery_list):
                        removed_item = grocery_list.pop(item_number - 1)
                        print(f"{removed_item} has been removed from the list.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("The grocery list is empty.")
                
        elif choice == "4":
            # Exit the program
            print("Exiting the program.")
            break
            
        else:
            print("Invalid option. Please try again.")

grocery_program(grocery_list)

"""
hi! well done! very unique approach by using the number of the item to remove it, this does prevent errors well. you did a perfect job with error handling and input validation :D
"""
