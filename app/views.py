"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from .forms import NewPropertyForm
from app.models import Property
from .config import Config
from flask.helpers import send_from_directory
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Real Estate")


@app.route('/property', methods=['GET', 'POST'])
def property():
    """Render the website's property page."""
    form = NewPropertyForm()    
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            rooms = form.totalRooms.data
            bathrooms = form.totalBathrooms.data
            price = form.price.data
            propertyType = form.propertyType.data
            location = form.location.data
            photo = form.photo.data
            photo_name = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_name))
            newProperty = Property(title, description, rooms, bathrooms, price, propertyType, location, photo_name)
            db.session.add(newProperty)
            db.session.commit()

            flash('Property was successfully added', 'success')
            return redirect(url_for('properties'))
        flash_errors(form)
    return render_template('form.html', form=form)

@app.route('/properties/')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

#gets image file
@app.route('/properties/<filename>')
def get_Image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']),filename)

#gets imagebased on id
@app.route('/property/<pid>')
def propertyid(pid):
    _property = Property.query.get(int(pid))
    return render_template('view_property.html', _property=_property)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")