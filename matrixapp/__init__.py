import os
from flask import redirect, flash, url_for, Flask, render_template, request
from matrixcalculator import Matrix
from configObj import Config
from matrixapp.forms import CreateMatrixForm, MatrixListForm


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    @app.route('/', methods=('GET', 'POST'))
    @app.route('/index', methods=('GET', 'POST'))
    def index():
        submitted = request.args.get('submitted')
        form = CreateMatrixForm()
        if submitted:
            form = MatrixListForm(int(request.args.get('cols')))
        if form.validate_on_submit():
            if not submitted:
                return redirect(url_for('index', submitted=True, rows=form.rows.data, cols=form.cols.data))
            else:
                m = Matrix([[0 for i in range(int(request.args.get('cols')))] for j in range(int(request.args.get('rows')))])
                flash('Creating a matrix ' + str(m))
        return render_template('index.html', title="Danny's Linear Algebra Calculator", form=form, submitted=submitted)
    
    from . import ops
    app.register_blueprint(ops.bp)
    return app
