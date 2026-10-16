def calculate_profit(selling_price, purchase_price, quantity):
    profit_per_item = selling_price - purchase_price
    total_profit = profit_per_item * quantity
    return total_profit

product_name = "Peak Milk"
milktotal = calculate_profit(1500,1200,4)

print(product_name, "profit", milktotal)