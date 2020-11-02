from flask import Flask, render_template, json
from api import api_bp
from flask import request, abort,url_for,redirect

# from models import init_db, get_all, insert

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@app.route('/test/<username>')
def test(username):
    print("username", username)
    return "Welcome Here!"


@app.route('/login/laod', methods=['POST', 'GET'])
def do_login():
    if request.method == 'GET':
        return bad_request_data();
    elif request.method == 'POST':
        data = request.get_data()
        data1 = json.loads(data.decode('utf-8'))

        good_data = {
            'name': data1['name'],
            'pwd': data1['pwd']
        }

        return good_data
    else:
        abort(404)


@app.route('/show', methods=['GET'])
def do_show():
    data = {}
    userData = []

    # 数据库取得数据
    userData.append({'name': 'Tom', 'pwd': '123'})
    userData.append({'name': 'Jerry', 'pwd': '123'})

    data['userData'] = userData

    return render_template('index.html', data=data)


def bad_request_data():
    bad_data = {
        'name': 'thief',
        'message': 'Fuck off!'
    }

    return bad_data;


if __name__ == '__main__':
    # with app.app_context():
    #     init_db(app)
    #     if not get_all():
    #         insert("tom", "noteA")
    #         insert("Jack", "noteB")
    app.run()
