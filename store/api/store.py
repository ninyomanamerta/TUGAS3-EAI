from flask import Blueprint, request
from webargs.flaskparser import parser
from marshmallow import Schema, fields
from ..schemas import model
from .. import impl

bp = Blueprint('store', __name__)


@bp.route('/store/inventory', methods=['get'])
def GetInventory():
    """
    Returns a map of status codes to quantities
    """

    return impl.store.GetInventory()


@bp.route('/store/order', methods=['post'])
def PlaceOrder():
    """
    Place a new order in the store
    """

    schema = model.Order()

    body = parser.parse(schema, request, location='json')
    schema = model.Order()

    body = parser.parse(schema, request, location='form'
    )

    return impl.store.PlaceOrder(body)


@bp.route('/store/order/<orderId>', methods=['get'])
def GetOrderById(orderId):
    """
    For valid response try integer IDs with value &lt;= 5 or &gt; 10. Other values will generate exceptions.
    """

    options = {}
    options["orderId"] = orderId

    return impl.store.GetOrderById(options)


@bp.route('/store/order/<orderId>', methods=['delete'])
def DeleteOrder(orderId):
    """
    For valid response try integer IDs with value &lt; 1000. Anything above 1000 or nonintegers will generate API errors
    """

    options = {}
    options["orderId"] = orderId

    return impl.store.DeleteOrder(options)
