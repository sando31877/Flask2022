from flask import (
    Flask,
    Response,
    render_template,
    request,
    make_response,
    redirect,
    abort,
    render_template_string,
)
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    username = request.form.get('id', '')
    return render_template('index.html', name=username)


@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form.get('id', '')
        password = request.form.get('pwd', '')

        if username == 'admin':
            return redirect(f"/?id={username}")
        else:
            error_temp_1 = '''
            <script>alert('{username}은 존재하지 않는 id입니다.')</script>
            '''.format(username=username)
            return render_template_string(error_temp_1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
