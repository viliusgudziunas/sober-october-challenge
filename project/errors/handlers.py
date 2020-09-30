from flask import Blueprint, render_template
from project import db

bp = Blueprint("errors", __name__)


@bp.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


@bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("errors/500.html"), 500
