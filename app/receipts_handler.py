import uuid
from math import ceil

# In-memory storage for receipts
receipts_data = {}

def calculate_points(receipt):
    """
    Calculate points based on receipt data.
    """
    points = 0

    # Rule 1: 1 point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in receipt["retailer"])

    # Rule 2: 50 points if the total is a round dollar amount with no cents
    if float(receipt["total"]).is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if float(receipt["total"]) % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt
    points += len(receipt["items"])//2 * 5

    # Rule 5: If the trimmed length of the item description is a multiple of 3, 
    # multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in receipt["items"]:
        if (len(item["shortDescription"].strip()) % 3 == 0):
            points += ceil(float(item["price"]) * 0.2)

    # Rule 6: 6 points if the day in the purchase date is odd
    day = int(receipt["purchaseDate"][-2:])
    if (day % 2 == 1):
        points += 6

    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm
    hour = int(receipt["purchaseTime"][:2])
    if (hour >= 14 and hour < 16):
        points += 10


    return points

def process_receipt(body):
    """
    Handles POST /receipts/process.
    """
    receipt = body
    # Generate a unique ID for the receipt
    receipt_id = str(uuid.uuid4())

    # Calculate points and store them
    points = calculate_points(receipt)
    receipts_data[receipt_id] = points

    return {"id": receipt_id}, 200

def get_points(id):
    """
    Handles GET /receipts/{id}/points.
    """
    points = receipts_data[id]
    if points is None:
        return {"error": "Receipt ID not found"}, 404

    return {"points": points}, 200