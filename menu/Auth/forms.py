from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from wtforms.fields import PasswordField, StringField, SubmitField
from menu.db.models import Cashier, Chef, Manager


class CreateManagerForm(FlaskForm):
    """New manager form"""
    employee_id = StringField("Employee_id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")

    def validate_username(self, employee_id):
        """check if employee id exist"""
        employee = Manager.query.filter_by(
            employee_id=employee_id.data).first()
        if employee:
            raise ValidationError("Employee id already exists")


class CreateChefForm(FlaskForm):
    """New chef form"""
    employee_id = StringField("Employee_id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")

    def validate_username(self, employee_id):
        """check if employee id exist"""
        employee = Chef.query.filter_by(
            employee_id=employee_id.data).first()
        if employee:
            raise ValidationError("Employee id already exists")


class CreateCashierForm(FlaskForm):
    """New cashier form"""
    employee_id = StringField("Employee_id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")

    def validate_username(self, employee_id):
        """check if employee id exist"""
        employee = Cashier.query.filter_by(
            employee_id=employee_id.data).first()
        if employee:
            raise ValidationError("Employee id already exists")


class LoginManagerForm(FlaskForm):
    """ Mananger Login Form"""
    employee_id = StringField("Employee_id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8, max=16)])
    submit = SubmitField("LOG IN")


class LoginChefForm(FlaskForm):
    """Chef Login Form"""
    employee_id = StringField("Employee_id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8, max=16)])
    submit = SubmitField("LOG IN")


class LoginCashierForm(FlaskForm):
    """Cashier Login Form"""
    employee_id = StringField("Employee_id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8, max=16)])
    submit = SubmitField("LOG IN")
