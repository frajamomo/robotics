import requests

class CityGeocoder:
    @staticmethod
    def get_coordinates(city_name):
        url = f"https://geocode.xyz/{city_name}?json=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'latt' in data and 'longt' in data:
                latitude = float(data['latt'])
                longitude = float(data['longt'])
                return latitude, longitude
            else:
                print("Failed to fetch coordinates. Please try again.")
                return None, None
        else:
            print("Failed to fetch coordinates. Please try again.")
            return None, None

def main():
    city_name = input("Enter the name of the city: ")

    latitude, longitude = CityGeocoder.get_coordinates(city_name)
    if latitude is not None and longitude is not None:
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        # Continue with the rest of the calculations using latitude and longitude
    else:
        print("Unable to fetch coordinates. Exiting...")

if __name__ == "__main__":
    main()
