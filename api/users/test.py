from datetime import datetime
class  TimestampMixin:
    def __init__(self, *args, **kwargs):
        # Call any parent constructors to ensure compatibility.
        super().__init__(*args, **kwargs)
        # Initialize timestamp fields.
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Simulate saving the model and updating the timestamp."""
        self.updated_at = datetime.now()
        print(f"Model saved. Updated at {self.updated_at}")
class BaseModel:
    def __init__(self, name):
        self.name = name


class Product(TimestampMixin, BaseModel):
    def __init__(self, name, price):
        # Initialize both Mixin and BaseModel.
        super().__init__(name=name)
        self.price = price
# Create a product instance
product = Product(name="Laptop", price=1000)
print(product.name)
print(f"Product created at: {product.created_at}")

# Simulate saving the product
product.save()
