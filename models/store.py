from db import db

class StoreModel(db.Model):

    __tablename__ = 'store'

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)

    items = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self,name):
        self.name = name

    @classmethod
    def find_by_name(cls,name):

        return(StoreModel.query.filter_by(name = name).first())

    @classmethod
    def find_all(cls):
        return (StoreModel.query.all())

    def delete (self):

        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def json(self):

        return(self.name, [item.json() for item in self.items.all()])







