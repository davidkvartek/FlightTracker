import unittest
import sys
import os

# Add parent directory to path to import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class FlightTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test that the home page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flight Tracker', response.data)

    def test_favicon_link_presence(self):
        """Test that the favicon link is present in the home page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'/static/favicon.svg', response.data)

    def test_get_flight_valid(self):
        """Test retrieving a valid flight."""
        response = self.app.get('/api/flight/AA123')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['flight_number'], 'AA123')
        self.assertEqual(json_data['start_location'], 'New York (JFK)')

    def test_get_flight_invalid(self):
        """Test retrieving a non-existent flight."""
        response = self.app.get('/api/flight/INVALID999')
        self.assertEqual(response.status_code, 404)
        json_data = response.get_json()
        self.assertEqual(json_data['error'], 'Flight not found')

    def test_get_flight_case_insensitive(self):
        """Test that flight number lookup is case-insensitive."""
        response = self.app.get('/api/flight/aa123')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['flight_number'], 'AA123')

if __name__ == '__main__':
    unittest.main()
