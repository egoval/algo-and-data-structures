class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class ProductManager:
    def __init__(self):
        self.products = []

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(', ')
                self.products.append(Product(id, name, float(price), category))

    def insert_product(self, product):
        self.products.append(product)

    def update_product(self, id, name=None, price=None, category=None):
        for product in self.products:
            if product.id == id:
                if name: product.name = name
                if price: product.price = price
                if category: product.category = category
                return True
        return False

    def delete_product(self, id):
        self.products = [product for product in self.products if product.id != id]

    def search_product(self, id=None, name=None):
        results = []
        for product in self.products:
            if (id and product.id == id) or (name and product.name == name):
                results.append(product)
        return results

    def insertion_sort(self):
        for i in range(1, len(self.products)):
            key = self.products[i]
            j = i - 1
            while j >= 0 and key.price < self.products[j].price:
                self.products[j + 1] = self.products[j]
                j -= 1
            self.products[j + 1] = key

# Example Usage
pm = ProductManager()
pm.load_data('product_data.txt')

# Test Insert
print("Insert Test:")
new_product = Product('99999', 'New Product XYZ', 123.45, 'Electronics')
pm.insert_product(new_product)
for product in pm.products:
    if product.id == '99999':
        print(f"Inserted: {product.id}, {product.name}, {product.price}, {product.category}")

# Test Update
print("\nUpdate Test:")
pm.update_product('99999', name='Updated Product XYZ', price=543.21)
for product in pm.products:
    if product.id == '99999':
        print(f"Updated: {product.id}, {product.name}, {product.price}, {product.category}")

# Test Delete
print("\nDelete Test:")
pm.delete_product('99999')
print("Deleted product with ID 99999. Search result:")
deleted_product = pm.search_product(id='99999')
print("Product found" if deleted_product else "Product not found")

# Test Search
print("\nSearch Test:")
search_result = pm.search_product(id='40374')
for product in search_result:
    print(f"Found: {product.id}, {product.name}, {product.price}, {product.category}")

# Test Sort
print("\nSort Test:")
print("Before sorting by price:")
for product in pm.products[:5]:  # Display first 5 products for brevity
    print(f"{product.id}, {product.name}, {product.price}, {product.category}")

pm.insertion_sort()
print("\nAfter sorting by price:")
for product in pm.products[:5]:  # Display first 5 products for brevity
    print(f"{product.id}, {product.name}, {product.price}, {product.category}")
