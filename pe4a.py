from datetime import datetime

def read_temperature_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [lines[i:i+2] for i in range(0, len(lines), 2)]
        return data

def calculate_average_daily_temperature(data):
    daily_temperatures = {}
    for measurement_time, temperature in data:
        date = datetime.strptime(measurement_time.strip(), "%d-%m-%Y %H:%M:%S").date()
        if date not in daily_temperatures:
            daily_temperatures[date] = []
        daily_temperatures[date].append(float(temperature.strip()))
    
    daily_average_temperatures = {}
    for date, temperatures in daily_temperatures.items():
        daily_average_temperatures[date] = round(sum(temperatures) / len(temperatures), 3)
    
    return daily_average_temperatures

def calculate_average_temperature_in_range(data, start_hour, end_hour):
    total_temperatures = 0
    count = 0
    for measurement_time, temperature in data:
        time = datetime.strptime(measurement_time.strip(), "%d-%m-%Y %H:%M:%S").time()
        if start_hour <= time.hour <= end_hour:
            total_temperatures += float(temperature.strip())
            count += 1
    
    if count == 0:
        return 0
    else:
        return round(total_temperatures / count, 3)

def main():
    file_path = "temp.txt"
    data = read_temperature_data(file_path)
    
    daily_average_temperatures = calculate_average_daily_temperature(data)
    print("Average daily temperatures:")
    for date, average_temp in daily_average_temperatures.items():
        print(f"{date}: {average_temp}°C")

    avg_temp_5_to_15 = calculate_average_temperature_in_range(data, 5, 15)
    print(f"\nAverage temperature from 5:00 to 15:59: {avg_temp_5_to_15}°C")

    avg_temp_16_to_21 = calculate_average_temperature_in_range(data, 16, 21)
    print(f"Average temperature from 16:00 to 21:59: {avg_temp_16_to_21}°C")

if __name__ == "__main__":
    main()