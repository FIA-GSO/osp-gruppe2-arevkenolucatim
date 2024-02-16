import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        sql = '''
            INSERT INTO User (Company,Password,Email,Contact,Telephone) VALUES (?, ?, ?, ?, ?)
        '''

        company = request.form['companyName']
        mail = request.form['email']
        contact = request.form['contact']
        passw = request.form['password']
        telephone = request.form['telephone']

        db = get_db()
        db.execute(sql, (company,passw,mail,contact,telephone))
        db.commit()

        return redirect('register')
    else:
        return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        # TODO: This should be a more sophisticated check, instead of just checking whether they're empty.
        if request.form["email"] != "" and request.form["password"] != "":
            sql = '''
            SELECT * FROM User WHERE
            Email = ? AND
            Password = ?
            '''

            cur = get_db().execute(sql, (request.form["email"], request.form["password"]))
            if cur.fetchone() != None:
                return redirect('../company') # '..' required to step out of 'auth/'
        
    return "Error" # TODO: Replace with error page
            


@bp.route('/guestLogin', methods=['GET', 'POST'])
def guestLogin():
    return render_template('auth/guestLogin.html')


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('auth/edit.html')
