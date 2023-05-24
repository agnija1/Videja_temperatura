def calculate_average_temperature():
    temperatures = []
    
    # Input temperatures for each day of the month
    for day in range(1, 32):
        temperature = float(input(f"Enter the temperature for day {day}: "))
        temperatures.append(temperature)
    
    # Calculate average temperature in a day
    average_temperature_day = sum(temperatures) / len(temperatures)
    
    # Calculate average temperature at the end of the month
    average_temperature_month = sum(temperatures) / 31
    
    return average_temperature_day, average_temperature_month

# Call the function and print the results
average_day, average_month = calculate_average_temperature()
print(f"Average temperature in a day: {average_day}")
print(f"Average temperature at the end of the month: {average_month}")