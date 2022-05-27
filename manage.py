from re import S
from app import create_app, db
from app.models import Subscriber, User, Admin, Article, Comment
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Subscriber=Subscriber, User=User, Admin=Admin, Article=Article, Comment=Comment)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
