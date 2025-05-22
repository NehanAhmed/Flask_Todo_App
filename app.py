from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/todo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    date_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(10), default="Medium")  # New field
    due_date = db.Column(db.DateTime, nullable=True)       # New 

with app.app_context():
    db.create_all()


# 🔹 CREATE + READ
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("home"))

    # Filters
    search_query = request.args.get("search", "")
    date_filter = request.args.get("date", "")

    # Base query
    query = Todo.query

    if search_query:
        query = query.filter(
            (Todo.title.ilike(f"%{search_query}%")) |
            (Todo.desc.ilike(f"%{search_query}%"))
        )

    if date_filter:
        try:
            date_obj = datetime.strptime(date_filter, "%Y-%m-%d").date()
            query = query.filter(db.func.date(Todo.date_created_at) == date_obj)
        except ValueError:
            pass

    todos = query.filter_by(is_completed=False).order_by(Todo.date_created_at.desc()).all()
    completed = query.filter_by(is_completed=True).order_by(Todo.date_created_at.desc()).all()

    return render_template("index.html", todos=todos, completed=completed)

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)

    if request.method == "POST":
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update.html', todo=todo)


# 🔹 DELETE
@app.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/stats")
def stats():
    total = Todo.query.count()
    return render_template("stats.html", total=total)


@app.route("/toggle/<int:id>")
def toggle(id):
    todo = Todo.query.get_or_404(id)
    todo.is_completed = not todo.is_completed
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
