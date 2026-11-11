
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 6 - REFERENCES AND MUTABILITY

# Warm-up: Predict, Then Run
a = [1, 2, 3]
b = a

b.append(4)

# Prediction: [1, 2, 3, 4]
print("List a:", a)

c = a.copy()
c.append(5)

# a and c are now different lists.
print("Original a:", a)
print("Copied c:", c)

print("a is b:", a is b)
print("a is c:", a is c)
print("a == a[:]:", a == a[:])


# Build: Demonstrating the Shared Cart Bug
def buggy_add_item(item, cart=[]):
    cart.append(item)
    return cart


print("\n=== SHARED CART BUG ===")
print("Customer 1:", buggy_add_item("Milk"))
print("Customer 2:", buggy_add_item("Bread"))

# Both customers accidentally share the same list.
# This happens because the default list is created once.


# Fixed Version
def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\n=== FIXED CART ===")
print("Customer 1:", add_item("Milk"))
print("Customer 2:", add_item("Bread"))
