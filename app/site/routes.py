# creates a way for flask to route from one page to another. uses blueaprint alongside 
# __name__ to link files to each other
# This is an object oriented program (blueprint before building)

from flask import Blueprint, render_template

# this links all files defined together, makes route folder/file locating easier, hence the templates_folder
site = Blueprint('site', __name__, template_folder='site_templates') 

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')