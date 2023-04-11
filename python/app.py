from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_bcrypt import Bcrypt
from forms import RegistrationForm,LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

pg_user="postgres"
pg_pwd="password"
pg_port ="5432"
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://{username}:{password}@localhost:{port}/flaskk'.format(username=pg_user,password=pg_pwd,port=pg_port)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)


class RegisteredUsers(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(340),nullable=False)
@app.route('/register', methods=['POST'])
def register():
    
    username = request.json['username']
    email=request.json['email']
    password = request.json['password']
    form=RegistrationForm(request.form)
    # if not form.validate():
    #    return jsonify({'mesaage':'invalid registration'})
    user = RegisteredUsers.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'User already exists!'})

    else:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = RegisteredUsers(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def login():
    
    email = request.json['email']
    password = request.json['password']
    #form = LoginForm(request.form)
    #if not form.validate():
    #    return jsonify({'mesaage':'invalid login'})
    user = RegisteredUsers.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'User logged in successfully!'})
    else:
        return jsonify({'message': 'Invalid credentials!'})

       
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0',port=5002,debug=True)