from flask import Blueprint, render_template_string

bp = Blueprint('challenge1', __name__, url_prefix='/challenge1')

@bp.route('/')
def index():
    html = '''
    <html>
    <head><title>Alexander Watson - Hubble</title></head>
    <body>
        <h1>Welcome to Hubble Partner Portal</h1>
        <p>Find the flag in the page source.</p>
        <script>
            __meteor_runtime_config__ = {
                "PUBLIC_SETTINGS": {
                    "googleMapsApiKey": "FLAG{AIzaSyCTF_FAKE_google_maps_key_123456}"
                },
                "galaxyUrl": "https://hubble-check-dev-au.ap.galaxycloud.app",
                "gitCommitHash": "b95844f94cf0428f51647d4a8d78b86b60e10790"
            };
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)
