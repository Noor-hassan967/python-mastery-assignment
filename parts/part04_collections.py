
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 4 - COLLECTIONS

# Warm-up: Shopping List
items = ["milk", "bread", "eggs"]

items.append("tea")
items.remove("bread")
items.sort()

print("=== SHOPPING LIST ===")
for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")


# Build: Phone Book
contacts = {
    "Ali": "03000000001",
    "Sara": "03000000002",
    "Ahmed": "03000000003",
    "Ayesha": "03000000004",
    "Hamza": "03000000005"
}

while True:
    print("\n=== PHONE BOOK ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        name = input("Enter name to search: ")
        phone = contacts.get(name)

        if phone is None:
            print("Not found")
        else:
            print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Not found")

    elif choice == "4":
        for name, phone in sorted(contacts.items()):
            print(f"{name}: {phone}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
