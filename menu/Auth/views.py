"""Views"""
from flask import Blueprint, flash, url_for, redirect, request
from flask import render_template
from menu.db.database import db
from menu.db.models import Manager, Chef, Cashier
from flask_login import login_user, login_required
from .forms import CreateCashierForm, CreateChefForm, CreateManagerForm, LoginManagerForm, LoginChefForm, LoginCashierForm
from sqlalchemy import or_


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route('/managerregister', methods=['GET', 'POST'])
def register_manager():
    """Create a new manager"""
    form = CreateManagerForm()
    if request.method == "POST":
        employee = Manager(employee_id=request.form["employee_id"],)
        employee.encrypt_password(request.form["password"])
        employee.is_admin = False
        print(employee)
        db.session.add(employee)
        db.session.commit()
        flash("Account created successfully", "success")
        return redirect(url_for('auth.manager_login'))
    return render_template("auth/manager_register.html", form=form)


@auth.route('/chefregister', methods=['GET', 'POST'])
def register_chef():
    """Create a new Chef"""
    form = CreateChefForm()
    if request.method == "POST":
        employee = Chef(employee_id=request.form["employee_id"],)
        employee.encrypt_password(request.form["password"])
        employee.is_admin = False
        db.session.add(employee)
        db.session.commit()
        flash("Account created successfully", "success")
        return redirect(url_for('auth.chef_login'))
    return render_template('auth/chef_register.html', form=form)


@auth.route('/cashierregister', methods=['GET', 'POST'])
def register_cashier():
    """Create a new cashier"""
    form = CreateCashierForm()
    if request.method == "POST":
        employee = Cashier(employee_id=request.form["employee_id"],)
        employee.encrypt_password(request.form["password"])
        employee.is_admin = False
        db.session.add(employee)
        db.session.commit()
        flash("Account created successfully", "success")
        return redirect(url_for('auth.cashier_login'))
    return render_template('auth/cashier_register.html', form=form)


@auth.route('/managerlogin', methods=['GET', 'POST'])
def manager_login():
    """Log in manager"""
    form = LoginManagerForm()
    if request.method == "POST":
        employee = db.session.query(Manager).filter(
            or_(Manager.employee_id == request.form["employee_id"])).first()
        if employee and employee.confirm_password(request.form["password"]):
            login_user(employee, remember=True)
            flash("Success")
            return redirect(url_for("auth.manager_portal"))
        flash("Check your login details")
    return render_template('auth/Manager_login.html', form=form)


@auth.route('/cheflogin', methods=['GET', 'POST'])
def chef_login():
    """Log in chef"""
    form = LoginChefForm()
    if request.method == "POST":
        employee = db.session.query(Chef).filter(
            or_(Chef.employee_id == request.form["employee_id"])).first()
        if employee and employee.confirm_password(request.form["password"]):
            login_user(employee, remember=True)
            flash("Success")
            return redirect(url_for("auth.chef_portal"))
        flash("Check your login details")
    return render_template('auth/Chef_login.html', form=form)


@auth.route('/cashierlogin', methods=['GET', 'POST'])
def cashier_login():
    """Log in cashier"""
    form = LoginCashierForm()
    if request.method == "POST":
        employee = db.session.query(Cashier).filter(
            or_(Cashier.employee_id == request.form["employee_id"])).first()
        if employee and employee.confirm_password(request.form["password"]):
            login_user(employee, remember=True)
            flash("Success")
            return redirect(url_for("auth.cashier_portal"))
        flash("Check your login details")
    return render_template('auth/cashier_login.html', form=form)


@auth.route('/managerportal', methods=['GET', 'POST'])
def manager_portal():
    return render_template('manager_view.html')


@auth.route('/chefportal', methods=['GET', 'POST'])
def chef_portal():
    return render_template('chef_portal.html')


@auth.route('/cashierportal', methods=['GET', 'POST'])
def cashier_portal():
    return render_template('cashier_portal.html')
