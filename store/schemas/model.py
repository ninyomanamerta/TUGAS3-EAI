from marshmallow import Schema, fields


class Address(Schema):
    city = fields.String()
    state = fields.String()
    street = fields.String()
    zip = fields.String()


class ApiResponse(Schema):
    code = fields.Int()
    message = fields.String()
    type = fields.String()


class Category(Schema):
    id = fields.Int()
    name = fields.String()


class Customer(Schema):
    address = Address(many=True)

    id = fields.Int()
    username = fields.String()


class GetInventoryInlineResp(Schema):
    pass


class LoginUserInlineResp(Schema):
    pass


class Order(Schema):
    complete = fields.Boolean()
    id = fields.Int()
    petId = fields.Int()
    quantity = fields.Int()
    shipDate = fields.DateTime()

    status = fields.String()


class Pet(Schema):
    category = fields.Raw()

    id = fields.Int()
    name = fields.String(required=True,)
    photoUrls = fields.String(many=True)

    status = fields.String()
    tags = fields.String(many=True)



class Tag(Schema):
    id = fields.Int()
    name = fields.String()


class User(Schema):
    email = fields.String()
    firstName = fields.String()
    id = fields.Int()
    lastName = fields.String()
    password = fields.String()
    phone = fields.String()
    userStatus = fields.Int()
    username = fields.String()


class CreateUsersWithListInputInlineReqJson(User):
    pass


class FindPetsByStatusInlineResp(Pet):
    pass


class FindPetsByTagsInlineResp(Pet):
    pass
