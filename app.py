from flask import Flask, render_template_string
from challenges import challenge1, challenge2, challenge3, challenge4, challenge5, challenge6, challenge7, challenge8

app = Flask(__name__)

app.register_blueprint(challenge1.bp)
app.register_blueprint(challenge2.bp)
app.register_blueprint(challenge3.bp)
app.register_blueprint(challenge4.bp)
app.register_blueprint(challenge5.bp)
app.register_blueprint(challenge6.bp)
app.register_blueprint(challenge7.bp)
app.register_blueprint(challenge8.bp)

@app.route('/')
def index():
    return render_template_string('''
    <h1>Hubble CTF - 8 Challenges</h1>
    <ul>
        <li><a href="/challenge1">1. Meteor Leak</a></li>
        <li><a href="/challenge2">2. No WAF, No Cry</a></li>
        <li><a href="/challenge3">3. Basic Brute</a></li>
        <li><a href="/challenge4">4. Splunkd Sneak</a></li>
        <li><a href="/challenge5">5. TLS Time Machine</a></li>
        <li><a href="/challenge6">6. Email Spoof</a></li>
        <li><a href="/challenge7">7. Dependency Confusion</a></li>
        <li><a href="/challenge8">8. Git History Ghost</a></li>
    </ul>
    <p>Flags are shown directly on each challenge page (training CTF).</p>
    ''')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
