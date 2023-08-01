import requests

def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    return response.json()

def main():
    print("Weather Data Program!")
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = int(input("Enter your choice (0-3): "))

        if option == 1:
            weather_data = get_weather_data()
            print("Weather:", weather_data["list"][0]["weather"][0]["description"])

        elif option == 2:
            weather_data = get_weather_data()
            print("Wind Speed:", weather_data["list"][0]["wind"]["speed"])

        elif option == 3:
            weather_data = get_weather_data()
            print("Pressure:", weather_data["list"][0]["main"]["pressure"])

        elif option == 0:
            print("Exiting the program")
            break

        else:
            print("Invalid option, Please try again.")

if __name__ == "__main__":
    main()