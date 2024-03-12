def read_temperature_file(filename):
    daily_temperatures = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            time = lines[i].strip()
            temperature = float(lines[i+1])
            date = time.split()[0]
            if date in daily_temperatures:
                daily_temperatures[date].append(temperature)
            else:
                daily_temperatures[date] = [temperature]
    return daily_temperatures

def calculate_daily_average(temperatures):
    daily_averages = {}
    for date, temps in temperatures.items():
        daily_averages[date] = sum(temps) / len(temps)
    return daily_averages

def calculate_time_range_average(temperatures, start_time, end_time):
    total_temps = 0
    count = 0
    for temps in temperatures.values():
        for temp in temps:
            if start_time <= temp <= end_time:
                total_temps += temp
                count += 1
    if count == 0:
        return 0
    return total_temps / count

def main():
    temperatures = read_temperature_file('temp.txt')
    daily_averages = calculate_daily_average(temperatures)
    print("Average daily temperatures:")
    for date, avg_temp in daily_averages.items():
        print(f"{date}: {avg_temp:.2f}")

    temp_range_1 = calculate_time_range_average(temperatures, 5, 15.9999)
    temp_range_2 = calculate_time_range_average(temperatures, 16, 21.9999)
    print(f"Average temperature from 5:00 to 15:59:59: {temp_range_1:.2f}")
    print(f"Average temperature from 16:00 to 21:59:59: {temp_range_2:.2f}")

if __name__ == "__main__":
    main()
