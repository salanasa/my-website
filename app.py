import os
from flask import Flask, render_template

app = Flask(__name__)

# Database Structure: Digital Library Data
library_data = [
    {
        "id": 1, 
        "title": "مجلة المدرسة - العدد الثالث", 
        "category": "Magazine", 
        "cover_image": "/static/gallery/mag3.jpg", 
        "file_path": "https://t.me/aljawadin313/877", 
        "type": "pdf"
    },
    {
        "id": 2, 
        "title": "أرشيف فعاليات المدرسة", 
        "category": "Photo", 
        "cover_image": "https://i.ibb.co/xpsrvh5/DSC0004.jpg", 
        "file_path": "https://i.ibb.co/xpsrvh5/DSC0004.jpg", 
        "type": "image"
    },
    {
        "id": 3, 
        "title": "منهاج الصالحين - العبادات", 
        "category": "Book", 
        "cover_image": "https://i.ibb.co/8v1WMCg/logo-png.jpg", 
        "file_path": "#", 
        "type": "pdf"
    }
]

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

@app.route('/library')
def library():
    events_images = os.listdir('static/gallery/events') if os.path.exists('static/gallery/events') else []
    building_images = os.listdir('static/gallery/building') if os.path.exists('static/gallery/building') else []
    
    return render_template('library.html', library_data=library_data, 
                           events_images=events_images, building_images=building_images)

# Optional: catch-all or error handler if templates are missing
@app.errorhandler(404)
def page_not_found(e):
    return "الصفحة غير موجودة", 404

if __name__ == '__main__':
    app.run(debug=True)