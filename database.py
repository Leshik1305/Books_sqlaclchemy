from email.policy import default

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    added = db.Column(db.DateTime, nullable=False, default=func.now())
    is_read = db.Column(db.Boolean, default=False)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"Book(title={self.title!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = relationship(
        "Book", back_populates="genre"
    )