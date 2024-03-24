import json


def AddPet(body):
    """
    Add a new pet to the store

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "category": "<Category>",
        "id": "<int64>",
        "name": "<string>",
        "photoUrls": "<array>",
        "status": "<string>",
        "tags": "<array>",
    }), 200


def UpdatePet(body):
    """
    Update an existing pet by Id

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "category": "<Category>",
        "id": "<int64>",
        "name": "<string>",
        "photoUrls": "<array>",
        "status": "<string>",
        "tags": "<array>",
    }), 200


def FindPetsByStatus(options):
    """
    Multiple status values can be provided with comma separated strings
    :param options: A dictionary containing all the paramters for the Operations
        options["status"]: Status values that need to be considered for filter

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps([{
        "category": "<Category>",
        "id": "<int64>",
        "name": "<string>",
        "photoUrls": "<array>",
        "status": "<string>",
        "tags": "<array>",
    }]), 200


def FindPetsByTags(options):
    """
    Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
    :param options: A dictionary containing all the paramters for the Operations
        options["tags"]: Tags to filter by

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps([{
        "category": "<Category>",
        "id": "<int64>",
        "name": "<string>",
        "photoUrls": "<array>",
        "status": "<string>",
        "tags": "<array>",
    }]), 200


def GetPetById(options):
    """
    Returns a single pet
    :param options: A dictionary containing all the paramters for the Operations
        options["petId"]: ID of pet to return

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "category": "<Category>",
        "id": "<int64>",
        "name": "<string>",
        "photoUrls": "<array>",
        "status": "<string>",
        "tags": "<array>",
    }), 200


def UpdatePetWithForm(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["petId"]: ID of pet that needs to be updated
        options["name"]: Name of pet that needs to be updated
        options["status"]: Status of pet that needs to be updated

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return '', 400


def DeletePet(options):
    """
    delete a pet
    :param options: A dictionary containing all the paramters for the Operations
        options["api_key"]
        options["petId"]: Pet id to delete

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return '', 400


def UploadFile(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["petId"]: ID of pet to update
        options["additionalMetadata"]: Additional Metadata

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "code": "<int32>",
        "message": "<string>",
        "type": "<string>",
    }), 200



