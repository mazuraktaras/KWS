from kwsapp import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from kwsapp.models import User, Role

manager = Manager(app)
migrate = Migrate(app, db, render_as_batch=True)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


# @app.shell_context_processor
# def make_shell_context():
    # return dict(app=app, db=db, User=User, Role=Role)
