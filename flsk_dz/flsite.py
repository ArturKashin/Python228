import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase

DATABASE = "/tmp/flsk.db"
DEBUG = True
SECRET_KEY = '1de680d3e308c7735eacfdc3e9a97732240c4be4'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

# menu = [{"name": "Главная", "url": "index"},
#         {"name": "Наши статьи", "url": "articles"},
#         {"name": "Добавить статью", "url": "add_articles"}
#         ]


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('index'))
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/articles")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("articles.html", title="Наши статьи", menu=dbase.get_menu())


@app.route("/add_articles")
def add_articles():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("add_articles.html", title="Добавить статью", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
