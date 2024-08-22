from pyprik import find_top_matching
import pandas as pd
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Desktop'],
    'Brand': ['Dell', 'Apple', 'Samsung', 'Apple', 'HP'],
    'RAM': ['8GB', '4GB', '6GB', '512MB', '16GB'],
    'Storage': ['512GB SSD', '64GB', '128GB', '32GB', '1TB HDD'],
    'Processor': ['i5', 'A13', 'Exynos', 'S5', 'i7'],
    'Price': [600, 999, 300, 199, 800]
}

products = pd.DataFrame(data)

# Example parameters for finding the top matching products
requirements = {
    'Brand': 'Apple',
    'RAM': '4GB'
}
top_n = 2

# Call the function with the parameters
top_matching_products = find_top_matching(products, requirements, top_n)
print(top_matching_products)
