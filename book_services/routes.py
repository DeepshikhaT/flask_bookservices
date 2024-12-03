from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields
from db import db
from model import BookModel

book_bp = Blueprint("Books", "books", description="Operations on books")

# Marshmallow Schemas
class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)

# Routes
@book_bp.route("/")
class BookList(MethodView):
    @book_bp.response(200, BookSchema(many=True))
    def get(self):
        """Get all books"""
        return BookModel.query.all()

    @book_bp.arguments(BookSchema)
    @book_bp.response(201, BookSchema)
    def post(self, book_data):
        """Add a new book"""
        book = BookModel(**book_data)
        db.session.add(book)
        db.session.commit()
        return book


@book_bp.route("/<int:book_id>")
class BookDetail(MethodView):
    @book_bp.response(200, BookSchema)
    def get(self, book_id):
        """Get a specific book"""
        book = BookModel.query.get_or_404(book_id)
        return book

    @book_bp.response(200)
    def delete(self, book_id):
        """Delete a specific book"""
        book = BookModel.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted"}
