from flask import Blueprint, request

bp = Blueprint('challenge5', __name__, url_prefix='/challenge5')

@bp.route('/decrypt')
def decrypt():
    if request.args.get('solve') == '1':
        return "FLAG{poodle_attack_cbc_vulnerable}"
    return "Send ?solve=1 to get the flag (simulated TLS POODLE attack)"
