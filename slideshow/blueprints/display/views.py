from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user

from .models import Display
from .forms import DisplayForm, EditDisplayForm

bp = Blueprint('display', __name__, template_folder='templates', url_prefix='/display/')


@bp.get('/')
@login_required
def display_list():
    displays = Display.query.all()
    return render_template('display/display_list.html', displays=displays)


@bp.get('create_display')
@login_required
def create_display():
    display = Display(location='Default')
    display.save()
    return redirect(url_for('display.display_list'))


@bp.get('/deactivate_display/<public_id>')
@login_required
def deactivate_display(public_id):
    display = Display.query.filter_by(public_id=public_id).first()
    display.deactivate()
    return redirect(url_for('display.display_list'))


@bp.get('/activate_display/<public_id>')
@login_required
def activate_display(public_id):
    display = Display.query.filter_by(public_id=public_id).first()
    display.activate()
    return redirect(url_for('display.display_list'))


@bp.get('/delete_display/<public_id>')
@login_required
def delete_display(public_id):
    display = Display.query.filter_by(public_id=public_id).first()
    display.delete()
    return redirect(url_for('display.display_list'))
