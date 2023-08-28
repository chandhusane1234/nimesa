import requests

# Function to get temperature for a specific date and time
def get_temperature(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['main']['temp']
    return None

# Function to get wind speed for a specific date and time
def get_wind_speed(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['wind']['speed']
    return None

# Function to get pressure for a specific date and time
def get_pressure(data, target_date_time):
    for entry in data['list']:
        if entry['dt_txt'] == target_date_time:
            return entry['main']['pressure']
    return None

# Main function to fetch data from the API and handle user input
def main():
    api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    
    response = requests.get(api_url)
    
    if response.status_code != 200:
        print("Failed to retrieve data from the API. Please check your internet connection or try again later.")
        return
    
    weather_data = response.json()
    
    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            target_date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
            temperature = get_temperature(weather_data, target_date_time)
            if temperature is not None:
                print(f"Temperature at {target_date_time}: {temperature}°C")
            else:
                print("Data not found for the specified date and time.")
        
        elif choice == '2':
            target_date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
            wind_speed = get_wind_speed(weather_data, target_date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {target_date_time}: {wind_speed} m/s")
            else:
                print("Data not found for the specified date and time.")
        
        elif choice == '3':
            target_date_time = input("Enter date and time (yyyy-mm-dd hh:mm:ss): ")
            pressure = get_pressure(weather_data, target_date_time)
            if pressure is not None:
                print(f"Pressure at {target_date_time}: {pressure} hPa")
            else:
                print("Data not found for the specified date and time.")
        
        elif choice == '0':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
