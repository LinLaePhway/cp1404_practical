def main():
    name = input("Enter name: ")
    display_menu()
    choice = input(">>> ").upper()

    while choice != 'Q':
        if choice == 'H':
            print("Hello", name)
        elif choice == 'G':
            print("Goodbye", name)
        else:
            print("Invalid choice")

        display_menu()
        choice = input(">>> ").upper()
    print("Finished.")

        
def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


main()
