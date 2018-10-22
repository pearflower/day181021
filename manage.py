from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from info import create_app,db

def main():
    # 数据库迁移
    app,redis_store = create_app()

    manager = Manager(app)

    Migrate(app, db)
    manager.add_command('db', MigrateCommand)
    manager.run()

if __name__ == '__main__':
    main()