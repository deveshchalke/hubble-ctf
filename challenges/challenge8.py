from flask import Blueprint, send_file, abort
import os

bp = Blueprint('challenge8', __name__, url_prefix='/challenge8')

@bp.route('/repo')
def repo():
    repo_path = 'fake_repo.tar.gz'
    if not os.path.exists(repo_path):
        import tarfile
        with tarfile.open(repo_path, 'w:gz') as tar:
            info = tarfile.TarInfo('README.txt')
            content = b"This is a simulated Git repository.\n\nFlag is: FLAG{git_history_leaks_secrets}\nBut you would find it by running 'git log -p' on a real repo.\n"
            info.size = len(content)
            tar.addfile(info, fileobj=content)
    return send_file(repo_path, as_attachment=True)
