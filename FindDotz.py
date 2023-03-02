import os

print("Finding Dotz...")
os.system("mkdir dots")

for dotID in range(7999, 9001):
    os.system("wget https://www.diamonddotz.com/image/cache/catalog/products/main/ddc/ddc." + str(dotID) + "-200x200.jpg")

