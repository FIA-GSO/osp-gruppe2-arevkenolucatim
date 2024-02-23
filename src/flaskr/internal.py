import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('internal', __name__, url_prefix='/')

@bp.route('/company', methods=['GET', 'POST'])
def company_view():
    return render_template('internal/companyView.html')


@bp.route('/requestConfirm', methods=['GET'])
def request_confirm():
    return render_template('internal/requestConfirm.html')


@bp.route('/organisation', methods=['GET', 'POST'])
def organisation_view():
    db = get_db()
    data = db.execute(
        'SELECT r.ID ''RequestID'', u.Company, u.Email, u.Contact, u.Telephone, r.Days, r.Remarks, r.TableCount, r.ChairCount FROM Request r INNER JOIN User u ON r.UserID = u.ID WHERE r.Status = 0'
    ).fetchall()

    return render_template('internal/organisationView.html', data=data)


@bp.route('/accept', methods=["POST"])
def accept_request():
    id = request.form.get("ID")
    db = get_db()
    data = db.execute(
        'UPDATE Request SET Status = 1 WHERE ID = ' + str(id)
    ).fetchall()
    db.commit()

    return "<meta http-equiv=\"refresh\" content=\"0; url=/organisation\">"


@bp.route("/deny", methods=["POST"])
def deny_request():
    id = request.form.get("ID")
    db = get_db()
    data = db.execute(
        'UPDATE Request SET Status = 2 WHERE ID = ' + str(id)
    ).fetchall()
    db.commit()
    
    return "<meta http-equiv=\"refresh\" content=\"0; url=/organisation\">"
