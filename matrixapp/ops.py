import functools
from flask import (
    Blueprint, redirect, render_template, request, session, url_for, flash, Flask
)
from matrixapp.forms import EnterMatrixForm
from matrixcalculator import Matrix

bp = Blueprint('operations', __name__, url_prefix='/operations')

@bp.route('/inverse')
def inverse():
    form = EnterMatrixForm()
    if form.validate_on_submit():
        entry = form.entry.data.splitlines()
        entry = [i.split() for i in entry]
        entry = [[int(x) for x in y] for y in entry]
        #for j in range(len(entry)):
        #    for k in range(len(entry[0])):  
        #        entry[j][k] = int(entry[j][k])
        mat = Matrix(entry)
        flash(str(mat))
    return render_template('/ops/inverse.html', title="Danny's Linear Algebra Calculator", form=form)
    
@bp.route('/eigen')
def eigen():
    form = EnterMatrixForm()
    if form.validate_on_submit():
        entry = form.entry.data.splitlines()
        entry = [i.split() for i in entry]
        entry = [[int(x) for x in y] for y in entry]
        #for j in range(len(entry)):
        #    for k in range(len(entry[0])):  
        #        entry[j][k] = int(entry[j][k])
        mat = Matrix(entry)
        flash(str(mat))
    return render_template('/ops/eigen.html', title="Eigenvalues and Eigenvectors", form=form)
    
@bp.route('/gaussianelimination')
def gaussianelimination():
    form = EnterMatrixForm()
    if form.validate_on_submit():
        entry = form.entry.data.splitlines()
        entry = [i.split() for i in entry]
        entry = [[int(x) for x in y] for y in entry]
        #for j in range(len(entry)):
        #    for k in range(len(entry[0])):  
        #        entry[j][k] = int(entry[j][k])
        mat = Matrix(entry)
        flash(str(mat))
    return render_template('/ops/gaussianelimination.html', title="Gaussian Elimination", form=form)
    
@bp.route('/orthogonalprojection')
def orthogonalprojection():
    form = EnterMatrixForm()
    if form.validate_on_submit():
        entry = form.entry.data.splitlines()
        entry = [i.split() for i in entry]
        entry = [[int(x) for x in y] for y in entry]
        #for j in range(len(entry)):
        #    for k in range(len(entry[0])):  
        #        entry[j][k] = int(entry[j][k])
        mat = Matrix(entry)
        flash(str(mat))
    return render_template('/ops/orthogonalprojection.html', title="Orthogonal Projections", form=form)

@bp.route('/basicoperations')
def basicoperations():
    form = EnterMatrixForm()
    if form.validate_on_submit():
        entry = form.entry.data.splitlines()
        entry = [i.split() for i in entry]
        entry = [[int(x) for x in y] for y in entry]
        #for j in range(len(entry)):
        #    for k in range(len(entry[0])):  
        #        entry[j][k] = int(entry[j][k])
        mat = Matrix(entry)
        flash(str(mat))
    return render_template('/ops/basicoperations.html', title="Orthogonal Projections", form=form)