from flask_login import LoginManager, login_manager
from flask_login.utils import login_user


login_manager = LoginManager()
login_manager.login_message = "You must login to see this"
login_manager.login_view = "auth.manager_login"
login_manager.login_view = "auth.chef_login"
login_manager.login_view = "auth.cashier_login"
login_manager.login_message_category = "info"
