def calculate_profit(selling_price, purchase_price, quantity):
    profit_per_item = selling_price - purchase_price
    total_profit = profit_per_item * quantity
    return total_profit

product_name1 = "Peak Milk"
milktotal = calculate_profit(1500,1200,4)

product_name2 = "Milo"
milototal = calculate_profit(1200,1000,5)
product_name3 = "indomie"
indomietotal = calculate_profit(800,600,10)

aggregate = "Total"
gentotal = milktotal + milototal + indomietotal

print(product_name1, "profit", milktotal)
print(product_name2, "profit", milototal)
print(product_name3, "profit", indomietotal)
print(aggregate, "profit", gentotal)