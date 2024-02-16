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
    return render_template('internal/organisationView.html')