# receipt-processor
This is basic API server made as a submissionm for this [programming chalange](https://github.com/fetch-rewards/receipt-processor-challenge/tree/main)

# Run Instructions
from the app directory run
```
docker build -t receipts-api ./ 
docker run -p 5000:5000 receipts-api 
```

Here is an example of me calling the API server 

```
jonathan@DESKTOP-FC8VOH2:~$ curl -X POST http://localhost:5000/receipts/process      -H "Content-Type: application/json"      -d '{
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
}'

{
  "id": "5caf01b9-7021-4235-8dbf-d647992e764a"
}

jonathan@DESKTOP-FC8VOH2:~$ curl -X GET http://localhost:5000/receipts/5caf01b9-7021-4235-8dbf-d647992e764a/points
{
  "points": 28
}
```
# Test Instructions
To run the unit tests you can run: 

`pytest test/test_receipts_handler.py`

If you run the tests locally you will need to pip install pytest as well as the dependencies in requirements.txt
