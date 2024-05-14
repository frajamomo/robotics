import requests
from math import radians, sin, cos, sqrt, atan2, degrees, pi

class ISSPosition:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def fetch_position(self):
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        if response.status_code == 200:
            self.latitude = float(data['iss_position']['latitude'])
            self.longitude = float(data['iss_position']['longitude'])
            return True
        else:
            print("Failed to fetch ISS position.")
            return False

class DistanceCalculator:
    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371.0  # Radius of the Earth in kilometers

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance

class AzimuthCalculator:
    @staticmethod
    def calculate_azimuth(lat1, lon1, lat2, lon2):
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1

        x = sin(dlon) * cos(lat2)
        y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)

        azimuth = atan2(x, y)
        azimuth_degrees = (degrees(azimuth) + 360) % 360  # Convert radians to degrees and adjust range
        return azimuth_degrees

class ElevationCalculator:
    @staticmethod
    def calculate_elevation(lat1, lon1, lat2, lon2):
        R = 6371.0  # Radius of the Earth in kilometers

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        elevation = atan2(distance, R) * 180 / pi
        return elevation

def main():
    user_latitude = float(input("Enter your latitude (in degrees): "))
    user_longitude = float(input("Enter your longitude (in degrees): "))

    iss_position = ISSPosition()
    if iss_position.fetch_position():
        distance = DistanceCalculator.calculate_distance(user_latitude, user_longitude, iss_position.latitude, iss_position.longitude)
        azimuth = AzimuthCalculator.calculate_azimuth(user_latitude, user_longitude, iss_position.latitude, iss_position.longitude)
        elevation = ElevationCalculator.calculate_elevation(user_latitude, user_longitude, iss_position.latitude, iss_position.longitude)
        print(f"The ISS is approximately {distance:.2f} kilometers away from your location.")
        print(f"The angle from the North Pole to the ISS is {azimuth:.2f} degrees.")
        print(f"The angle from the horizon to the ISS is {elevation:.2f} degrees.")
    else:
        print("Unable to calculate the distance.")

if __name__ == "__main__":
    main()
