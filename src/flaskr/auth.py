import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
import bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth')
salt = bcrypt.gensalt()

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        sql = '''
            INSERT INTO User (Company,Password,Email,Contact,Telephone) VALUES (?, ?, ?, ?, ?)
        '''

        company = request.form['companyName']
        mail = request.form['email']
        contact = request.form['contact']
        passw = bytes(request.form['password'], 'utf-8')
        telephone = request.form['telephone']

        hashed = bcrypt.hashpw(passw, salt)

        db = get_db()
        db.execute(sql, (company,hashed,mail,contact,telephone))
        db.commit()

        return redirect('register')
    else:
        return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')


@bp.route('/guestLogin', methods=['GET', 'POST'])
def guestLogin():
    return render_template('auth/guestLogin.html')


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('auth/edit.html')
