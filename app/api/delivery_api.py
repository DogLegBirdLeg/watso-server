from app.api.Store.Presentation.store import store_ns
from app.api.Post.Presentation.post import post_ns
from app.api.Order.Presentation.order import order_ns
from app.api.History.Presentation.history import history_ns

from flask import Blueprint
from flask_restx import Api

from app.util.error_handling import error_handler

authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

delivery_bp = Blueprint('delivery', __name__, url_prefix='/api/delivery')
delivery_api = Api(delivery_bp, authorizations=authorizations, title='delivery', description='배달 기능과 관련된 api', doc='/docs')
error_handler(delivery_api)

delivery_api.add_namespace(store_ns, path='/store')
delivery_api.add_namespace(post_ns, path='/post')
delivery_api.add_namespace(order_ns, path='/order')
delivery_api.add_namespace(history_ns, path='/history')