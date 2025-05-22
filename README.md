# 📝 Flask Todo App

A beautifully styled, full-featured **Todo List application** built using **Flask**, **SQLAlchemy**, and **Bootstrap 5**. It includes everything you need to manage tasks efficiently: filters, priorities, status toggles, live search, dark mode, charts, and more — all in a modern UI.

---

## 🚀 Live Demo

> Not deployed yet — run it locally by following the instructions below.

---

## 📸 Preview

![Light Mode Screenshot](screenshots/light-mode.png)
![Dark Mode Screenshot](screenshots/dark-mode.png)

---

## 🧰 Features

- ✅ Add, edit, delete tasks
- 📌 Mark tasks as complete/incomplete
- 🔍 Live search functionality
- 🎯 Filter by completion status, priority, and date
- 🌓 Dark mode toggle
- 🧭 Sticky sidebar with collapsible filter panel
- 📊 Stats page with Chart.js for visual summaries
- 💅 Responsive UI with Bootstrap 5
- 🔄 AJAX toggle for task status *(coming soon)*
- 📦 Drag & drop to reorder tasks *(planned)*
- 🔐 User authentication *(planned)*

---

## 📂 Project Structure

Flask/
├── static/
│ ├── css/
│ ├── js/
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── stats.html
│ └── ...
├── app.py
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/your-github-username/your-todo-app.git
cd your-todo-app
Create virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install flask flask_sqlalchemy pymysql
Setup MySQL database

Make sure MySQL is running, then create the database:

sql
Copy
Edit
CREATE DATABASE todo;
Configure the connection in app.py

python
Copy
Edit
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<your_password>@localhost/todo"
Run the app

bash
Copy
Edit
python app.py
Visit: http://localhost:5000

📦 Requirements
Python 3.10+

MySQL

Flask

Flask SQLAlchemy

PyMySQL

Bootstrap 5 (via CDN)

Chart.js (for stats)

You can generate a requirements.txt file by running:

bash
Copy
Edit
pip freeze > requirements.txt
📈 Statistics Page
Visit /stats to view:

Total tasks

Completed vs Incomplete

Charts rendered with Chart.js

💡 Upcoming Features
AJAX-based inline updates (mark complete without reload)

Drag & drop reordering of tasks

Export to CSV/PDF

User registration & login system

Deployment to Render or Vercel

🙋‍♂️ Author
Made with ❤️ by nehan-dev

Star ⭐ the project if you find it useful. Contributions welcome!

📜 License
This project is open-source and available under the MIT License.

markdown
Copy
Edit

---

✅ Let me know if you want me to:
- Add `screenshots/` folder or placeholder images
- Auto-generate a `requirements.txt`
- Write deployment instructions for **Render** or **Vercel**
- Export this file as a downloadable `.md`

Would you like a `LICENSE` file too?






