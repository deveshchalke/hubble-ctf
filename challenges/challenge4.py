from flask import Blueprint, jsonify

bp = Blueprint('challenge4', __name__, url_prefix='/challenge4')

LOGS = [
    {"timestamp": "2026-06-10T10:00:01", "method": "GET", "path": "/api/user", "query": "api_key=real_splunk_key_123"},
    {"timestamp": "2026-06-10T10:00:02", "method": "GET", "path": "/api/data", "query": "api_key=FLAG{splunk_logs_leak_tokens}"}
]

@bp.route('/logs')
def logs():
    return jsonify(LOGS)
