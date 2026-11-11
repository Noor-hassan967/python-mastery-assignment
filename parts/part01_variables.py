# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# Part 1 - Variables, Data Types, Input and Output



# Warm-up: Student ID Card
print("=== STUDENT ID CARD ===")

name = input("Enter name: ")
age = int(input("Enter age: "))
student_class = input("Enter class: ")
city = input("Enter city: ")

print("\n======== STUDENT CARD ========")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"Class: {student_class}")
print(f"City : {city}")
print("==============================")

print("Data Types:")
print("Name:", type(name))
print("Age:", type(age))
print("Class:", type(student_class))
print("City:", type(city))


# Build: Shop Bill
print("\n=== SHOP BILL ===")

item_name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

if price < 0 or quantity < 0:
    print("Price and quantity cannot be negative.")
else:
    subtotal = price * quantity
    discount = subtotal * 0.05
    discounted_amount = subtotal - discount
    tax = discounted_amount * 0.17
    final_total = discounted_amount + tax

    print("\n======= RECEIPT =======")
    print(f"Item: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: Rs {subtotal:.2f}")
    print(f"Discount (5%): Rs {discount:.2f}")
    print(f"Tax (17%): Rs {tax:.2f}")
    print(f"Final Total: Rs {final_total:.2f}")
    print("=======================")
