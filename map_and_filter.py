products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}

filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))

print(filtered_products)