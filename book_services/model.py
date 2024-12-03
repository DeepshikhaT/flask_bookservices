from db import db 

class BookModel(db.model):
    __tablename__ = "books"
    id = db.Column(db.Interger, primary_key = True)
    title = db.Column(db.String(90), nullable= False)
    author = db.Column(db.String(80), nullable=False)