import os
from flask import Flask, render_template
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
    @app.route('/index')
    def index():
        user = {'username':'Danny'}
        return render_template('index.html', title="Danny's Linear Algebra Calculator", user=user)

    from . import ops
    app.register_blueprint(ops.bp)

    #@app.route('/inverse')
    #def inverse():
    #    user = {'username':'Danny'}
    #    return render_template('/ops/inverse.html', title="Danny's Matrix Calculator", user=user)
    
    return app