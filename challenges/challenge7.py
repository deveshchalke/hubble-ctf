from flask import Blueprint, request

bp = Blueprint('challenge7', __name__, url_prefix='/challenge7')

@bp.route('/install')
def install():
    version = request.headers.get('X-Package-Version', '0.0.0')
    try:
        if version > '1.0.0':
            return "FLAG{dependency_confusion_ci_pwn}"
    except:
        pass
    return "Using safe version 1.0.0 from private registry. Try setting X-Package-Version: 2.0.0"
