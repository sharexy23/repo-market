from db import db
from flask import send_file
from io import BytesIO

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(110))
    email = db.Column(db.String(110))
    password = db.Column(db.String(110))
    account_balance = db.Column(db.Float)


    wishlist = db.relationship('Wishlist', lazy='dynamic')
    store = db.relationship('Store',lazy='dynamic')
    cart = db.relationship('Cart', lazy='dynamic')


    def __init__(self,username,email,password,account_balance):
        self.username = username
        self.email = email
        self.password = password
        self.account_balance = account_balance


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'id':self.id,'username':self.username,'email':self.email}
    def jsony(self):
        return {'wishlist':[wishlist.json() for wishlist in self.wishlists.all()]}
    def jsonyo(self):
        return {'cart':[cart.json() for cart in self.carts.all()]}

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_password(cls, password):
        return cls.query.filter_by(password=password).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class Wishlist(db.Model):
    __TableName__ = 'wishlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    price = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )
    user = db.relationship('User')#,# foreign_keys= user_id)


    def __init__(self,name,price, user_id):
        #self.id = _i
        self.name = name
        self.price = price
        self.user_id = user_id

        #self.verification_code = verification_code

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def json(self):
        return {'name':self.name,'price':self.price}

class Cart(db.Model):
    __TableName__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    price = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )
    user = db.relationship('User')#,# foreign_keys= user_id)


    def __init__(self,name,price,user_id):
        #self.id = _i
        self.name = name
        self.price = price
        self.user_id = user_id

        #self.verification_code = verification_code


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    def json(self):
        return {'name':self.name,'price':self.price}




class Store(db.Model):
    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(900))
    description = db.Column(db.String(900))
    store_address = db.Column(db.String(900))
    inventory = db.relationship('Inventory', lazy='dynamic')
    account_balance = db.Column(db.String(110))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )
    user = db.relationship('User')#,# foreign_keys= user_id)


    def __init__(self,name,description,store_address,account_balance,user_id):
        #self.id = _i
        self.name = name
        self.description = description
        self.store_address = store_address
        self.account_balance = account_balance
        self.user_id = user_id



        #self.verification_code = verification_code

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    def json(self):
        return {'name':self.name,'description':self.description,'store_address':self.store_address,'inventory':[inventory.gason() for inventory in self.inventory.all()]}

    def json2(self):
        return {'name':self.name,'description':self.description,'store_address':self.store_address,'inventory':[inventory.json() for inventory in self.inventory.all()]}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()








class Inventory(db.Model):
    __TableName__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    NO_of_products = db.Column(db.Integer,default = None)
    products = db.relationship('Product', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False )
    user = db.relationship('Store')#,# foreign_keys= user_id)


    def __init__(self,name,NO_of_products, user_id):
        #self.id = _i
        self.name = name
        self.NO_of_products = NO_of_products
        self.user_id = user_id

        #self.verification_code = verification_code

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    def json(self):
        return {'products':[product.json() for product in self.products.all()]}
    def gason(self):
        return {'NO_of_products':self.NO_of_products}





class Product(db.Model):
    __TableName__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(900))
    description = db.Column(db.String(900))
    image = db.relationship('Image', lazy='dynamic')
    cost = db.Column(db.Integer)
    Number_available = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False )
    user = db.relationship('Inventory')#,# foreign_keys= user_id)


    def __init__(self,name,description,cost,Number_available,user_id):
        #self.id = _i
        self.name = name
        self.description = description
        self.cost = cost
        self.Number_available = Number_available
        self.user_id = user_id



        #self.verification_code = verification_code

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()


    def json(self):
        return {'name':self.name,'description':self.description,'cost':self.cost,'Number_available':self.Number_available}


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False )
    user = db.relationship('Product')

    def __init__(self,image,name,mimetype,user_id):
        #self.id = _i
        self.image = image
        self.name = name
        self.mimetype = mimetype
        self.user_id = user_id


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
