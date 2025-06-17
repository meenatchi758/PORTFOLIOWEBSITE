from flask import Flask, render_template, url_for

app = Flask(__name__)

projects = [
    {
        "title": "Hardware E-Commerce",
        "description": "A full-stack e-commerce platform built using Flask, MySQL, and Bootstrap.",
        "link": "https://hardware-ecommerce-demo.vercel.app"
    },
    {
        "title": "Resume Builder App",
        "description": "Flask app that lets users generate resumes and download as PDFs.",
        "link": "https://resume-builder-demo.vercel.app"
    },
    {
        "title": "Expense Tracker",
        "description": "Track your income and expenses with visual charts using Flask and Chart.js.",
        "link": "#"
    }
]

@app.route('/')
def home():
    return render_template("index.html", projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
