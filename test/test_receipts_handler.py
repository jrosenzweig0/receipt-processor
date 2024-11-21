from app.receipts_handler import process_receipt, calculate_points, get_points
from unittest.mock import patch

EXAMPLE_RECEIPT_1 = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}

EXAMPLE_RECEIPT_2 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "15:13",
    "total": "1.00",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
    ]
}

# Tests rules 1, 4, 5, 6
def test_calculate_points():
    points = calculate_points(EXAMPLE_RECEIPT_1)
    assert points == 28  

# Tests rules 1, 2, 3, 7
def test_calculate_points():
    points = calculate_points(EXAMPLE_RECEIPT_2)
    assert points == 91

def test_process_receipt():
    with patch("app.receipts_handler.receipts_data", {}) as mock_storage:
        response, status_code = process_receipt(EXAMPLE_RECEIPT_1)
        assert status_code == 200
        assert "id" in response
        assert len(mock_storage) == 1  # Check the mocked storage was used

def test_get_points():
    with patch("app.receipts_handler.receipts_data", {"5caf01b9-7021-4235-8dbf-d647992e764a": 28}):
        response, status_code = get_points("5caf01b9-7021-4235-8dbf-d647992e764a") #ID of the mocked data
        assert status_code == 200
        assert response == {"points": 28}

