from flask import Blueprint, request, jsonify

bp = Blueprint('challenge6', __name__, url_prefix='/challenge6')

@bp.route('/send', methods=['POST'])
def send_email():
    data = request.get_json()
    if not data:
        return jsonify({"error": "send JSON with 'from' field"}), 400
    from_domain = data.get('from', '').split('@')[-1]
    if from_domain == 'hubble.sh':
        return jsonify({"status": "sent", "flag": "FLAG{no_spf_means_spoofing}"})
    return jsonify({"status": "rejected", "reason": "SPF check would fail"}), 403
