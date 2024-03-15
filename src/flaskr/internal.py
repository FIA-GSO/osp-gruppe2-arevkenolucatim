import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('internal', __name__, url_prefix='/')

@bp.route('/company/<id>', defaults={'id': None}, methods=['GET'])
@bp.route('/company/<id>', methods=['GET'])
def company_view(id):
    return render_template('internal/companyView.html', id=id)


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


@bp.route('/requestEdit', methods=['GET', 'POST'])
def request_edit():
    if request.method == 'POST':
        mail = request.form['mail']
        day = request.form['day']
        tables = request.form['tables']
        chairs = request.form['chairs']
        remarks = request.form['remarks']
        presentationTopic = request.form['presentationTopic']
        presentationDuration = request.form['presentationDuration']
        db = get_db()
        data = db.execute("SELECT Company, telephone, Contact FROM User WHERE Email= ?", (mail,)).fetchone()
        
        if data == None:
            return redirect("../error")
        
        company = data[0]
        telephone = data[1]
        contact = data[2]
        
        return render_template('internal/requestConfirmRegistered.html',
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
        
        # Email abfangen
        # SQl daten auslesen
        # Felder mit daten füllen       
        return render_template('internal/requestEdit.html')


@bp.route('/organisation', methods=['GET', 'POST'])
def organisation_view():
    db = get_db()
    data = db.execute(
        "SELECT r.ID RequestID, u.Company, u.Email, u.Contact, u.Telephone, r.Days, r.Remarks, r.TableCount, r.ChairCount, r.Status, CASE r.Status WHEN 0 THEN 'Ausstehend' WHEN 1 THEN 'Akzeptiert' WHEN 2 THEN 'Abgelehnt' ELSE 'Invalide' END StatusText FROM Request r INNER JOIN User u ON r.UserID = u.ID WHERE u.Company <> 'ORGA'"
    ).fetchall()
    data2 = db.execute("SELECT r.ID RequestID, r.Company, r.Email, r.Contact, r.Telephone, r.Days, r.Remarks, r.TableCount, r.ChairCount, r.Status, CASE r.Status WHEN 0 THEN 'Ausstehend' WHEN 1 THEN 'Akzeptiert' WHEN 2 THEN 'Abgelehnt' ELSE 'Invalide' END StatusText FROM GuestRequest r").fetchall()
    for d in data2:
        data.append(d)
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

@bp.route('/requestConfirmRegistered', methods=['GET','POST'])
def request_confirm_registered():
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
        
        s = "SELECT ID FROM User WHERE Company = ? AND Email = ?"
        r = "SELECT ID FROM Request WHERE UserID = ?"

        sql = '''
        INSERT INTO Request (
            UserID,Remarks,Days,TableCount,ChairCount,LectureTopic,LectureLength,Status
        ) 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        '''

        sql2 = '''
        UPDATE Request
        SET Remarks = ?,
            Days = ?,
            TableCount = ?,
            ChairCount = ?,
            LectureTopic = ?,
            LectureLength = ?,
            Status = ?
        WHERE ID = ?
        '''

        db = get_db()

        uid = db.execute(s, (company, mail)).fetchone()[0] # UserID
        rid = db.execute(r, (str(uid),)).fetchone()[0] # RequestID

        if rid != None:
            # Update instead of insert
            db.execute(sql2, (remarks, day, tables, chairs, presentationTopic, presentationDuration, 0, rid))
        else:
            # Insert instead of update
            db.execute(sql, (str(uid), remarks, day, tables, chairs, presentationTopic, presentationDuration, 0))

        db.commit()

        return redirect(url_for('internal.company_view'))
    else:
        return render_template('internal/requestConfirmRegistered.html')