import functools
from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)

bp = Blueprint('operations', __name__, url_prefix='/operations')

@bp.route('/inverse')
def inverse():
    user = {'username':'Danny'}
    return render_template('/ops/inverse.html', title="Inverse of a Matrix", user=user)
      
@bp.route('/determinant')
def determinant():
    user = {'username':'Danny'}
    return render_template('/ops/determinant.html', title="Determinant of a Matrix", user=user)
    
@bp.route('/eigen')
def eigen():
    user = {'username':'Danny'}
    return render_template('/ops/eigen.html', title="Eigenvalues and Eigenvectors", user=user)
    
@bp.route('/gaussianelimination')
def gaussianelimination():
    user = {'username':'Danny'}
    return render_template('/ops/gaussianelimination.html', title="Gaussian Elimination", user=user)
    
@bp.route('/gramschmidt')
def gramschmidt():
    user = {'username':'Danny'}
    return render_template('/ops/gramschmidt.html', title="Gram Schmidt Process", user=user)
    
@bp.route('/orthogonalprojection')
def orthogonalprojection():
    user = {'username':'Danny'}
    return render_template('/ops/orthogonalprojection.html', title="Orthogonal Projections", user=user)
    
@bp.route('/QR')
def QR():
    user = {'username':'Danny'}
    return render_template('/ops/QR.html', title="QR Factorization", user=user)
    
@bp.route('/transpose')
def transpose():
    user = {'username':'Danny'}
    return render_template('/ops/transpose.html', title="Transpose", user=user)
    
