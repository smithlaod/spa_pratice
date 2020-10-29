from flask import Flask, render_template
from api import api_bp
from models import init_db, get_all, insert

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':

    with app.app_context():
        init_db(app)
        if not get_all():
            insert("tom", "noteA")
            insert("Jack", "noteB")
    app.run()
