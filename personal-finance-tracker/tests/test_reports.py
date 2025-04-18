import unittest
from routes.report_routes import generate_report  # Import your report generation function
from flask import Flask

class TestReportGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Flask app for testing
        cls.app = Flask(__name__)
        cls.client = cls.app.test_client()

    def test_generate_report(self):
        """
        Test the report generation functionality
        """
        # Example data for generating the report
        report_data = {
            "start_date": "2022-01-01",
            "end_date": "2022-12-31",
            "user_id": 1
        }

        # Call the function that generates the report
        result = generate_report(report_data['start_date'], report_data['end_date'], report_data['user_id'])

        # Assert that the result is a valid report (e.g., a dictionary or list with correct data)
        self.assertIsInstance(result, dict)  # Assuming the result is a dictionary
        self.assertIn("total_expenses", result)  # Assuming the report contains total expenses

    def test_generate_report_with_invalid_data(self):
        """
        Test report generation with invalid data
        """
        report_data = {
            "start_date": "2022-01-01",
            "end_date": "invalid-date",  # Invalid date
            "user_id": 1
        }

        # Call the function that generates the report with invalid data
        result = generate_report(report_data['start_date'], report_data['end_date'], report_data['user_id'])

        # Assert that the result is an error message
        self.assertEqual(result, "Invalid date format")

if __name__ == '__main__':
    unittest.main()
