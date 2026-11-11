# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026


# PART 11 - TYPE HINTS AND DATACLASSES

from dataclasses import dataclass, field


# Build: Product Dataclass
@dataclass
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative.")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")


products = [
    Product("Laptop", 85000.0, 5, ["electronics"]),
    Product("Mouse", 1200.0, 0, ["accessories"]),
    Product("Keyboard", 2500.0, 8),
    Product("Monitor", 30000.0, 0),
    Product("USB Drive", 1500.0, 12),
]

print("=== PRODUCT INVENTORY ===")

for product in products:
    print(product)

print("\n=== OUT OF STOCK ===")

for product in products:
    if product.stock == 0:
        print(f"{product.name} is out of stock.")
