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

        return redirect('login')
    else:
        return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        passw = bytes(request.form['password'], 'utf-8')
        hashed = bcrypt.hashpw(passw, salt)

        sql = '''
        SELECT * FROM User WHERE Email = ? AND Password = ?
        '''
        
        cur = get_db().execute(sql, (request.form["email"], hashed))
        if cur.fetchone() != None:
            return redirect('../company')
        else:
            return render_template('auth/login.html', error=True)
    else:
        return render_template('auth/login.html')


@bp.route('/guestLogin', methods=['GET', 'POST'])
def guestLogin():
    if request.method == 'POST':
        company = request.form['companyName']
        mail = request.form['email']
        telephone = request.form['telephone']
        contact = request.form['contact']
        day = request.form['day']
        tables = request.form['tables']
        chairs = request.form['chairs']
        remarks = request.form['remarks']
        presentationTopic = request.form['presentationTopic']
        presentationDuration = request.form['presentationDuration']

        return render_template(
            'internal/requestConfirm.html',
            company=company,
            mail=mail,
            telephone=telephone,
            contact=contact,
            remarks=remarks,
            day=day,
            tables=tables,
            chairs=chairs,
            presentationDuration=presentationDuration,
            presentationTopic=presentationTopic
        )
    else:
        return render_template('auth/guestLogin.html')


""" @bp.route('/requestEdit', methods=['GET', 'POST'])
def requestEdit():
    if request.method == 'POST':
        day = request.form['day']
        remarks = request.form['remarks']
        tables = request.form['tables']
        chairs = request.form['chairs']
        presentationTopic = request.form['presentationTopic']
        presentationDuration = request.form['presentationDuration']
        return render_template(
            'internal/requestConfirm.html'
            day=day,
            remarks=remarks,
            tables=tables,
            chairs=chairs,
            presentationTopic=presentationTopic,
            presentationDuration=presentationDuration
        )
    else:
        return render_template('') """


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    # if request.method
    # db = get_db()
    # data = db.execute(
    #     "SELECT * from User where Email =" + localStorage.
    # ).fetchall()
    return render_template('auth/edit.html')
