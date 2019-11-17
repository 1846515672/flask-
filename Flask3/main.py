"""
控制文件
"""

from flask_migrate import Migrate, MigrateCommand
from blup import create_app, db
from flask_script import Manager #命令管理器
from flask_script import Command #命令定义的父类

app = create_app()
manager = Manager(app)

migrate = Migrate(app, db) #创建数据库管理实例

manager.add_command("db", MigrateCommand)


class Hello(Command):
    def run(self):        #自定义命令需要继承Command
        print("hello")   #命令的功能,是通过重写run方法实现

class Runserver(Command):
    def run(self):
        app.run(host="0.0.0.0", port=8000, debug=True, use_reloader=True)


manager.add_command("hello", Hello)
manager.add_command("runserver", Runserver)


if __name__ == '__main__':
    manager.run()