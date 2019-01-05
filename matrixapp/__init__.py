import os
from flask import redirect, flash, url_for, Flask, render_template, request
from matrixcalculator import Matrix
#app = Flask(__name__)
#from matrixapp import routes

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'matrixapp.sqlite'),
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    # a simple page that says hello
    @app.route('/')
    @app.route('/index', methods=('GET','POST'))
    def index():
        if request.method == 'POST':
            matrix_rows = request.form['rows']
            matrix_cols = request.form['cols']
            #option = request.form['option']

            if not matrix_rows: 
                error = 'Rows are required'
            elif not matrix_cols:
                error = 'Cols are required'
            else:
                m = Matrix([[0 for i in matrix_cols] for j in matrix_rows])
                print(m)
            flash(error)
        return render_template('index.html', title="Danny's Linear Algebra Calculator")

    from . import ops
    app.register_blueprint(ops.bp)

    #@app.route('/inverse')
    #def inverse():
    #    user = {'username':'Danny'}
    #    return render_template('/ops/inverse.html', title="Danny's Matrix Calculator", user=user)
    
    return app