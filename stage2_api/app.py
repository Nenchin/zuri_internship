from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zuri_task.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "custom key"
db = SQLAlchemy(app)
app.app_context().push()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name):
        self.name = name

class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    get_user = Users.query.get(id)
    if not get_user:
        return make_response(jsonify({"error": "User not found"}), 404)

    user_schema = UsersSchema()
    user = user_schema.dump(get_user)
    return make_response(jsonify({"user": user}), 200)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.get_json()
    get_user = Users.query.get(id)
    
    if not get_user:
        return make_response(jsonify({"error": "User not found"}), 404)
    
    if 'name' in data:
        get_user.name = data['name']
    
    db.session.commit()
    user_schema = UsersSchema()
    user = user_schema.dump(get_user)
    return make_response(jsonify({"user": user}), 200)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    get_user = Users.query.get(id)
    if not get_user:
        return make_response(jsonify({"error": "User not found"}), 404)
    
    db.session.delete(get_user)
    db.session.commit()
    return make_response("", 204)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_schema = UsersSchema()
    
    try:
        user = user_schema.load(data)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)
    
    result = user_schema.dump(user)
    return make_response(jsonify({"user": result}), 201)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=5000)
