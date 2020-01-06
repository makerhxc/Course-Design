import os
from app import create_app, db
from app.models import User, Blog,Commits
from flask_script import Manager, Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():#激活上下文变量
    return dict(app=app, db=db, User=User, Blog=Blog, Commits=Commits)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)#激活migrate命令行程序

if __name__ == '__main__':
    manager.run()