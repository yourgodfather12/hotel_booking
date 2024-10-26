# Path: apps/bookings/external_booking.py

import requests
from datetime import datetime

# API configurations - Replace these with actual API details
API_URL = "https://api.example.com/booking"  # The base URL of the booking API
API_KEY = "YOUR_API_KEY"  # Your API key for authentication


class ExternalBookingAPI:
    def __init__(self):
        self.api_url = API_URL
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    def search_accommodations(self, location, check_in, check_out, guests):
        """
        Search for accommodations based on location, check-in/check-out dates, and number of guests.
        """
        params = {
            "location": location,
            "check_in": check_in.strftime("%Y-%m-%d"),
            "check_out": check_out.strftime("%Y-%m-%d"),
            "guests": guests,
        }

        response = requests.get(f"{self.api_url}/search", headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()  # Return the list of accommodations
        else:
            response.raise_for_status()

    def check_availability(self, accommodation_id, check_in, check_out):
        """
        Check availability for a specific accommodation.
        """
        params = {
            "check_in": check_in.strftime("%Y-%m-%d"),
            "check_out": check_out.strftime("%Y-%m-%d"),
        }

        response = requests.get(
            f"{self.api_url}/accommodations/{accommodation_id}/availability",
            headers=self.headers,
            params=params
        )

        if response.status_code == 200:
            return response.json().get("available", False)  # Return availability status
        else:
            response.raise_for_status()

    def make_booking(self, accommodation_id, user_data, check_in, check_out):
        """
        Make a booking for a specific accommodation.
        """
        payload = {
            "accommodation_id": accommodation_id,
            "user": {
                "name": user_data.get("name"),
                "email": user_data.get("email"),
                "phone": user_data.get("phone"),
            },
            "check_in": check_in.strftime("%Y-%m-%d"),
            "check_out": check_out.strftime("%Y-%m-%d"),
        }

        response = requests.post(
            f"{self.api_url}/bookings",
            headers=self.headers,
            json=payload
        )

        if response.status_code == 201:
            return response.json()  # Return booking confirmation
        else:
            response.raise_for_status()


# Example usage
if __name__ == "__main__":
    booking_api = ExternalBookingAPI()
    location = "New York"
    check_in = datetime(2024, 11, 1)
    check_out = datetime(2024, 11, 5)
    guests = 2

    try:
        # Search accommodations
        accommodations = booking_api.search_accommodations(location, check_in, check_out, guests)
        print("Available accommodations:", accommodations)

        # Check availability for the first accommodation
        if accommodations:
            accommodation_id = accommodations[0]["id"]
            is_available = booking_api.check_availability(accommodation_id, check_in, check_out)
            print(f"Availability for {accommodation_id}:", is_available)

            # Make a booking if available
            if is_available:
                user_data = {"name": "John Doe", "email": "johndoe@example.com", "phone": "1234567890"}
                booking_confirmation = booking_api.make_booking(accommodation_id, user_data, check_in, check_out)
                print("Booking Confirmation:", booking_confirmation)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
