import os
from flask import redirect, flash, url_for, Flask, render_template, request
from matrixcalculator import Matrix
from configObj import Config
from matrixapp.forms import EnterMatrixForm, EnterMatrixForm2


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    @app.route('/', methods=('GET', 'POST'))
    @app.route('/index', methods=('GET', 'POST'))
    def index():
        form = EnterMatrixForm()
        if form.validate_on_submit():
            entry = form.entry.data.splitlines()
            entry = [i.split() for i in entry]
            try:
                entry = [[int(x) for x in y] for y in entry]
                mat = Matrix(entry)
                #flash(str(mat))
            except ValueError:
                flash("Oops! Enter valid matrix data.  Try again...")
            if form.options.data == 'g':
                k = mat.gaussianelimination()
                if form.detailed_solution.data:
                    flash(k[0])
                else:
                    flash(k[1])
        return render_template('index.html', title="Danny's Linear Algebra Calculator", form=form)
   
    from . import ops
    app.register_blueprint(ops.bp)
    return app
