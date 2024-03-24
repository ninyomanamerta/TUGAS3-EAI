from flask import Blueprint, request
from webargs.flaskparser import parser
from marshmallow import Schema, fields
from ..schemas import model
from .. import impl

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['post'])
def CreateUser():
    """
    This can only be done by the logged in user.
    """

    schema = model.User()

    body = parser.parse(schema, request, location='json')
    schema = model.User()

    body = parser.parse(schema, request, location='form'
    )

    return impl.user.CreateUser(body)


@bp.route('/user/createWithList', methods=['post'])
def CreateUsersWithListInput():
    """
    Creates list of users with given input array
    """

    schema = model.CreateUsersWithListInputInlineReqJson(many=True)

    body = parser.parse(schema, request, location='json')

    return impl.user.CreateUsersWithListInput(body)


@bp.route('/user/login', methods=['get'])
def LoginUser():

    options = {}
    options["password"] = request.args.get("password")
    options["username"] = request.args.get("username")

    return impl.user.LoginUser(options)


@bp.route('/user/logout', methods=['get'])
def LogoutUser():

    return impl.user.LogoutUser()


@bp.route('/user/<username>', methods=['get'])
def GetUserByName(username):

    options = {}
    options["username"] = username

    return impl.user.GetUserByName(options)


@bp.route('/user/<username>', methods=['put'])
def UpdateUser(username):
    """
    This can only be done by the logged in user.
    """

    options = {}
    options["username"] = username

    schema = model.User()

    body = parser.parse(schema, request, location='json')
    schema = model.User()

    body = parser.parse(schema, request, location='form'
    )

    return impl.user.UpdateUser(options, body)


@bp.route('/user/<username>', methods=['delete'])
def DeleteUser(username):
    """
    This can only be done by the logged in user.
    """

    options = {}
    options["username"] = username

    return impl.user.DeleteUser(options)
