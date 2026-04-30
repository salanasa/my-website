from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/magazine')
def magazine():
    return render_template('magazine.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/brochures')
def brochures():
    return render_template('brochures.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

# Optional: catch-all or error handler if templates are missing
@app.errorhandler(404)
def page_not_found(e):
    return "الصفحة غير موجودة", 404

if __name__ == '__main__':
    app.run(debug=True)