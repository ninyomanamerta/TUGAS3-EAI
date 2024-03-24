import json


def GetInventory():
    """
    Returns a map of status codes to quantities

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps("<map>"), 200


def PlaceOrder(body):
    """
    Place a new order in the store

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "complete": "<boolean>",
        "id": "<int64>",
        "petId": "<int64>",
        "quantity": "<int32>",
        "shipDate": "<date-time>",
        "status": "<string>",
    }), 200


def GetOrderById(options):
    """
    For valid response try integer IDs with value &lt;= 5 or &gt; 10. Other values will generate exceptions.
    :param options: A dictionary containing all the paramters for the Operations
        options["orderId"]: ID of order that needs to be fetched

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "complete": "<boolean>",
        "id": "<int64>",
        "petId": "<int64>",
        "quantity": "<int32>",
        "shipDate": "<date-time>",
        "status": "<string>",
    }), 200


def DeleteOrder(options):
    """
    For valid response try integer IDs with value &lt; 1000. Anything above 1000 or nonintegers will generate API errors
    :param options: A dictionary containing all the paramters for the Operations
        options["orderId"]: ID of the order that needs to be deleted

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return '', 400



