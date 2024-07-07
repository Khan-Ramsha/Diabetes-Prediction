# tests/test_invalid_input.py
import requests

def test_invalid_input():
    # Test handling of invalid input data
    url = 'http://localhost:5000/'
    invalid_data = {
        'Pregnancies': -1,  # Invalid value
        'Glucose': 'abc',   # Invalid type
        # Add more cases as needed
    }
    response = requests.post(url, data=invalid_data)
    assert response.status_code == 400  # Expected HTTP 400 Bad Request
