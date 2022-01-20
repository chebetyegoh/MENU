from flask import render_template
from flask import Blueprint
from flask_login import login_required

home = Blueprint("home", __name__)


@home.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@home.route('/about-us')
def about_us():
    return render_template('about_us.html')


@home.route('/contactus')
def contact_us():
    return render_template('contact_us.html')


