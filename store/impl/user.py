import json


def CreateUser(body):
    """
    This can only be done by the logged in user.

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "email": "<string>",
        "firstName": "<string>",
        "id": "<int64>",
        "lastName": "<string>",
        "password": "<string>",
        "phone": "<string>",
        "userStatus": "<int32>",
        "username": "<string>",
    }), 200


def CreateUsersWithListInput(body):
    """
    Creates list of users with given input array

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "email": "<string>",
        "firstName": "<string>",
        "id": "<int64>",
        "lastName": "<string>",
        "password": "<string>",
        "phone": "<string>",
        "userStatus": "<int32>",
        "username": "<string>",
    }), 200


def LoginUser(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["password"]: The password for login in clear text
        options["username"]: The user name for login

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps("<string>"), 200


def LogoutUser():
    """

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return '', 200


def GetUserByName(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["username"]: The name that needs to be fetched. Use user1 for testing. 

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "email": "<string>",
        "firstName": "<string>",
        "id": "<int64>",
        "lastName": "<string>",
        "password": "<string>",
        "phone": "<string>",
        "userStatus": "<int32>",
        "username": "<string>",
    }), 200


def UpdateUser(options, body):
    """
    This can only be done by the logged in user.
    :param options: A dictionary containing all the paramters for the Operations
        options["username"]: name that need to be deleted

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return '', 200


def DeleteUser(options):
    """
    This can only be done by the logged in user.
    :param options: A dictionary containing all the paramters for the Operations
        options["username"]: The name that needs to be deleted

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return '', 400



