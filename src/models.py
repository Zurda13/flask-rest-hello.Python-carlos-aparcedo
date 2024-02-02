from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Person (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    eyes_color =  db.Column(db.String(50), nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(20), nullable=False)
    favorites = db.relationship('Favorites', backref='person', lazy=True)

    def __repr__(self):
        return '<Person  %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "age": self.age,
            "gender": self.gender,
            "eyes_color": self.eyes_color,
            "hair_color": self.hair_color,
            "height": self.height
        } 
    
class Planets (db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    climate = db.Column(db.String(50),nullable=False)
    terrain= db.Column(db.String(250),nullable=False)
    rotation= db.Column(db.String(250),nullable=False)
    population= db.Column(db.String(250),nullable=False)
    orbital_period= db.Column(db.String(250),nullable=False)
    diameter= db.Column(db.String(250),nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "clima": self.climate,
            "terreno": self.terrain,
            "rotacion": self.rotation,
            "poblacion": self.population,
            "periodo_orbital": self.orbital_period,
            "diametro": self.diameter
            # do not serialize the password, its a security breach
        }

class Vehicles (db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name_Vehicles = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)
    favorites = db.relationship('Favorites', backref='vehicles', lazy=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name_Vehicles": self.name_Vehicles,
            "model": self.model
            # do not serialize the password, its a security breach
        }
    
class Favorites (db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    id_person = db.Column(db.Integer, db.ForeignKey('person.id'))


    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            # do not serialize the password, its a security breach
        }