from flask import Blueprint, request, make_response

bp = Blueprint('challenge3', __name__, url_prefix='/challenge3')

def check_auth(username, password):
    return username == 'admin' and password == 'Hubble2026'

def authenticate():
    return make_response('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Admin"'})

@bp.route('/admin')
def admin():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return "FLAG{basic_auth_is_not_enough}"
