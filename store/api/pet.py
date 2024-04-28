from flask import Blueprint, request
from webargs.flaskparser import parser
from marshmallow import Schema, fields
from flask import jsonify
from ..schemas import model
from .. import impl

bp = Blueprint('pet', __name__)


@bp.route('/pet', methods=['post'])
def AddPet():
    """
    Add a new pet to the store
    """

    schema = model.Pet()

    body = parser.parse(schema, request, location='json')
    schema = model.Pet()

    body = parser.parse(schema, request, location='form'
    )

    return impl.pet.AddPet(body)


@bp.route('/pet', methods=['put'])
def UpdatePet():
    """
    Update an existing pet by Id
    """

    schema = model.Pet()

    body = parser.parse(schema, request, location='json')
    schema = model.Pet()

    body = parser.parse(schema, request, location='form'
    )

    return impl.pet.UpdatePet(body)


@bp.route('/pet/findByStatus', methods=['get'])
def FindPetsByStatus():
    """
    Multiple status values can be provided with comma separated strings
    """

    options = {}
    options["status"] = request.args.get("status")

    return impl.pet.FindPetsByStatus(options)


@bp.route('/pet/findByTags', methods=['get'])
def FindPetsByTags():
    """
    Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
    """

    options = {}
    options["tags"] = request.args.get("tags")

    # return impl.pet.FindPetsByTags(options)
    
    # Mendapatkan nilai tags dari parameter query
    tags = request.args.get("tags")

    # Implementasi logika bisnis untuk mengembalikan data berdasarkan tags
    if tags == "kucing":
        pets = [{
            "category": "Kucing",
            "id": 100,
            "name": "Meow",
            "photoUrls": ["url_ke_foto"],
            "status": "Tersedia",
            "tags": ["kucing"]
        }]
    else:
        pets = []

    # Mengembalikan response dalam format JSON
    return jsonify(pets), 200


@bp.route('/pet/<petId>', methods=['get'])
def GetPetById(petId):
    """
    Returns a single pet
    """

    options = {}
    options["petId"] = petId

    return impl.pet.GetPetById(options)


@bp.route('/pet/<petId>', methods=['post'])
def UpdatePetWithForm(petId, ):

    options = {}
    options["petId"] = petId
    options["name"] = request.args.get("name")
    options["status"] = request.args.get("status")

    return impl.pet.UpdatePetWithForm(options)


@bp.route('/pet/<petId>', methods=['delete'])
def DeletePet(petId):
    """
    delete a pet
    """

    options = {}
    options["api_key"] = request.headers.get("api_key")
    options["petId"] = petId

    return impl.pet.DeletePet(options)


@bp.route('/pet/<petId>/uploadImage', methods=['post'])
def UploadFile(petId, ):

    options = {}
    options["petId"] = petId
    options["additionalMetadata"] = request.args.get("additionalMetadata")

    return impl.pet.UploadFile(options)
