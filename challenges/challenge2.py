from flask import Blueprint, request

bp = Blueprint('challenge2', __name__, url_prefix='/challenge2')

cache = {}

@bp.route('/api/secret')
def secret():
    cache_control = request.headers.get('Cache-Control', '')
    user_ip = request.remote_addr

    if 'only-if-cached' in cache_control:
        if 'cached_response' in cache:
            return cache['cached_response']
        else:
            return "No cached data", 404

    if user_ip == '127.0.0.1':
        data = "FLAG{ktor_cache_leak_2026}"
    else:
        data = "You are not admin"

    cache['cached_response'] = data
    return data
