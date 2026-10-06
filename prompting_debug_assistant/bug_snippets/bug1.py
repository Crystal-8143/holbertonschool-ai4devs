def calculate_average(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return average

def display_average(numbers):
    result = calculate_average(numbers)
    print("Average:", result)

numbers = [10, 20, 30, 40]
display_average(numbers)