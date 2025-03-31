from flask import Flask
from flask import render_template

from database import  Book, Genre, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    fairy_tale = Genre(name="Сказки")
    db.session.add(fairy_tale)
    poem = Genre(name="Поэзия")
    db.session.add(poem)

    winter_morning = Book(title="Зимнее утро", genre=poem)
    db.session.add(winter_morning)
    babysitter = Book(title="Няне", genre=poem)
    db.session.add(babysitter)
    groom = Book(title="Жених", genre=fairy_tale)
    db.session.add(groom)
    fish = Book(title="Сказка о рыбаке и рыбке", genre=fairy_tale)
    db.session.add(fish)

    db.session.commit()


@app.route("/")
def all_books():
    books = Book.query.all()
    return render_template("all_books.html", books=books)

@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )


if __name__ == '__main__':
    app.run(debug=True)