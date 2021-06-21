from flask import (render_template, send_from_directory)

import os
from src import app

# Favicon function
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Handling errors here
@app.errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html'), 404

# Handling routes here
@app.route('/')
@app.route('/intro')
def intro():
    return render_template(
        'hero.html',
        tab_title='Your Flask App'
    )


if __name__ == '__main__':
    app.run(debug=True)