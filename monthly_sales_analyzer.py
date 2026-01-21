# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]


def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total_sales = 0
    for item in data:
        total_sales += item[product_key]
    return total_sales


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total_sales = total_sales_by_product(data, product_key)
    return total_sales / len(data)


def best_selling_day(data):
    """Finds the day with the highest total sales."""
    highest_sales = 0
    best_day_sales = 0
    for item in data:
        highest_sales_by_day = item['product_a'] + item['product_b'] + item['product_c']
        if highest_sales_by_day > highest_sales:
            best_day_sales = item['day']
            highest_sales = highest_sales_by_day
    return best_day_sales


def worst_selling_day(data):
    """Finds the day with the worst total sales."""
    worst_sales = data[0]['product_a'] + data[0]['product_b'] + data[0]['product_c']
    worst_day_sales = 0
    for item in data:
        worst_sales_by_day = item['product_a'] + item['product_b'] + item['product_c']
        if worst_sales_by_day < worst_sales:
            worst_day_sales = item['day']
            worst_sales = worst_sales_by_day
    return worst_day_sales


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    days = 0
    for item in data:
        if item[product_key] > threshold:
            days += 1
    return days


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    total_sales_product_a = total_sales_by_product(data, 'product_a')
    total_sales_product_b = total_sales_by_product(data, 'product_b')
    total_sales_product_c = total_sales_by_product(data, 'product_c')
    if total_sales_product_a > total_sales_product_b and total_sales_product_a > total_sales_product_c:
        return 'product_a'
    elif total_sales_product_b > total_sales_product_a and total_sales_product_b > total_sales_product_c:
        return 'product_b'
    else:
        return 'product_c'


def top_3_days_with_best_sales(data):
    """Create an array with the total sales by day regardless the product and return the top 3."""
    result = []
    for item in data:
        total_sales = item['product_a'] + item['product_b'] + item['product_c']
        total_item = {
            'day': item['day'],
            'total_sales': total_sales
        }
        result.append(total_item)

    # Sort by total_sales in descending order and return top 3
    result.sort(key=lambda x: x['total_sales'], reverse=True)
    return result[:3]


def minimum_sales_selling_by_product(data, product_key):
    """Finds the minimum sales for a product key."""
    worst_sales = data[0]['product_a'] + data[0]['product_b'] + data[0]['product_c']
    for item in data:
        minimum_sales_by_day = item[product_key]
        if minimum_sales_by_day < worst_sales:
            worst_sales = minimum_sales_by_day
    return worst_sales


def maximum_sales_selling_by_product(data, product_key):
    """Finds the maximum sales for a product key."""
    best_sales = 0
    for item in data:
        highest_sales_by_day = item[product_key]
        if highest_sales_by_day > best_sales:
            best_sales = highest_sales_by_day
    return best_sales


def calculate_max_min_sales_by_product(data, product_key):
    """Calculate the range (maximum - minimum) of the sales of a product."""
    max_sales = maximum_sales_selling_by_product(data, product_key)
    min_sales = minimum_sales_selling_by_product(data, product_key)
    result = {
        'product': product_key,
        'range': max_sales - min_sales
    }
    return result


def max_and_min_sales_by_product(data, product_key):
    """Returns the maximum and minimum sales for a specific product."""
    data.sort(key=lambda x: x[product_key], reverse=True)
    return data[0][product_key], data[-1][product_key]


# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Day with worst total sales:", worst_selling_day(sales_data))
print("Show the days with the top 3 best total sales:", top_3_days_with_best_sales(sales_data))
print("Show the range of sales by product a:", calculate_max_min_sales_by_product(sales_data, "product_a").get('range'))
print("Show the range of sales by product b:", calculate_max_min_sales_by_product(sales_data, "product_b").get('range'))
print("Show the range of sales by product c:", calculate_max_min_sales_by_product(sales_data, "product_c").get('range'))
