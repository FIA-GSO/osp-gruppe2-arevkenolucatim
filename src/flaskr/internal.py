import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('internal', __name__, url_prefix='/')

@bp.route('/company', methods=['GET', 'POST'])
def company_view():
    return render_template('internal/companyView.html')


@bp.route('/requestConfirm', methods=['GET','POST'])
def request_confirm():
    if request.method == 'POST':
        company = request.form['company']
        mail = request.form['email']
        telephone = request.form['telephone']
        remarks = request.form['remarks']
        contact = request.form['contact']
        day = request.form['day']
        tables = request.form['tables']
        chairs = request.form['chairs']
        presentationTopic = request.form['presentationTopic']
        presentationDuration = request.form['presentationDuration']

        sql = '''
        INSERT INTO GuestRequest (
            Company,Email,Telephone,Contact,Remarks,Days,TableCount,ChairCount,LectureTopic,LectureLength,Status
        ) 
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        '''

        db = get_db()
        db.execute(sql, (company,mail,telephone,contact,remarks,day,tables,chairs,presentationTopic,presentationDuration,0))
        db.commit()

        return redirect('/')
    else:
        return render_template('internal/requestConfirm.html')


@bp.route('/organisation', methods=['GET', 'POST'])
def organisation_view():
    db = get_db()
    data = db.execute(
        "SELECT r.ID RequestID, u.Company, u.Email, u.Contact, u.Telephone, r.Days, r.Remarks, r.TableCount, r.ChairCount, r.Status, CASE r.Status WHEN 0 THEN 'Ausstehend' WHEN 1 THEN 'Akzeptiert' WHEN 2 THEN 'Abgelehnt' ELSE 'Invalide' END StatusText FROM Request r INNER JOIN User u ON r.UserID = u.ID"
    ).fetchall()

    return render_template('internal/organisationView.html', data=data)


@bp.route('/approval', methods=["POST"])
def accept_request():
    data = request.form.get("ID").split(":")
    choice = data[0] # Either 'accept' or 'deny'
    id = data[1]

    print(f"Record {id} was set to {choice}")

    db = get_db()
    data = db.execute(
        f'UPDATE Request SET Status = {str(1 if choice == "accept" else 2)} WHERE ID = ' + str(id)
    ).fetchall()
    db.commit()

    return "<meta http-equiv=\"refresh\" content=\"0; url=/organisation\">"


