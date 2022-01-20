from .database import db
from flask_login.mixins import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from menu.login.login import login_manager


class Manager(db.Model, UserMixin):
    __tablename__ = 'managers'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(8), unique=True,
                            nullable=False, index=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def encrypt_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(str(self.hashed_password), password)

    def __init__(self, employee_id, hashed_password):
        self.employee_id = employee_id
        self.hashed_password = hashed_password

    def __repr__(self) -> str:
        return f"Manager('{self.employee_id}')"


class Cashier(db.Model, UserMixin):
    __tablename__ = 'cashiers'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(8), unique=True,
                            nullable=False, index=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def encrypt_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(str(self.hashed_password), password)

    def __init__(self, employee_id, hashed_password):
        self.employee_id = employee_id
        self.hashed_password = hashed_password

    def __repr__(self) -> str:
        return f"Cashier('{self.employee_id}')"


class Chef(db.Model, UserMixin):
    __tablename__ = 'chef'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(8), unique=True,
                            nullable=False, index=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def encrypt_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(str(self.hashed_password), password)

    def __init__(self, employee_id, hashed_password):
        self.employee_id = employee_id
        self.hashed_password = hashed_password

    def __repr__(self) -> str:
        return f"Chef('{self.employee_id}')"


@login_manager.user_loader
def load_user(id):
    return Cashier.query.get(int(id))


@login_manager.user_loader
def load_user(id):
    return Chef.query.get(int(id))


@login_manager.user_loader
def load_user(id):
    return Manager.query.get(int(id))
