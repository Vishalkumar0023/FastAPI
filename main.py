from fastapi import FastAPI
from models import Products
from fastapi import HTTPException

app=FastAPI()

@app.get("/")
def greet():
    return "Welcome to telusko trac"

products=[
    Products(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Products(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Products(id=5, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Products(id=6, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/product")
def add_product(product:Products):
    products.append(product)
    return product


@app.put("/product")
def update_product(id:int,product:Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i]=product
            return "Product added succesfully"
    raise HTTPException(status_code=404, detail="Product not found")
    

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "product deleted"
    raise HTTPException(status_code=404, detail="Product not found")            