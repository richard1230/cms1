from flask import Flask
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
import config
from exts import db



def create_app():
    app = Flask(__name__)
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(common_bp)
    app.config.from_object(config)

    db.init_app(app)

    return app



#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app= create_app()
    app.run()

    
    
    """
    代码流程:
    mysql> create databases zlbbs charset utf8;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'databases zlbbs charset utf8' at line 1
mysql> create database zlbbs charset utf8;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+-----------------------+
| Database              |
+-----------------------+
| information_schema    |
| alembic_demo          |
| flask_alembic_demo    |
| flask_migrate_demo    |
| flask_restful_demo    |
| flask_script_demo     |
| flask_sqlalchemy_demo |
| icbc_demo             |
| mysql                 |
| performance_schema    |
| sys                   |
| zlbbs                 |
+-----------------------+
12 rows in set (0.00 sec)

mysql> use zlbbs
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------+
| Tables_in_zlbbs |
+-----------------+
| alembic_version |
| cms_user        |
+-----------------+
2 rows in set (0.00 sec)

虚拟环境中迁移脚本:
(my_env) $python3 manage.py db init
  Creating directory /Users/mac/PycharmProjects/bbc/migrations ...  done
  Creating directory /Users/mac/PycharmProjects/bbc/migrations/versions ...  done
  Generating /Users/mac/PycharmProjects/bbc/migrations/script.py.mako ...  done
  Generating /Users/mac/PycharmProjects/bbc/migrations/env.py ...  done
  Generating /Users/mac/PycharmProjects/bbc/migrations/README ...  done
  Generating /Users/mac/PycharmProjects/bbc/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in
  '/Users/mac/PycharmProjects/bbc/migrations/alembic.ini' before proceeding.
(my_env) $python3 manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
(my_env) $python3 manage.py db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'cms_user'
  Generating /Users/mac/PycharmProjects/bbc/migrations/versions/6f5a8c020ab4_.py
  ...  done
(my_env) $python3 manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 6f5a8c020ab4, empty message
(my_env) $python3 manage.py create_cms_user -u richard -p 123456 -e 123456@qq.com
cms用户添加成功


mysql中:
mysql> select * from cms_user
    -> ;
+----+----------+----------+---------------+---------------------+
| id | username | password | email         | join_time           |
+----+----------+----------+---------------+---------------------+
|  1 | richard  | 123456   | 123456@qq.com | 2019-12-19 13:50:49 |
+----+----------+----------+---------------+---------------------+
1 row in set (0.00 sec)


发现是明文的，后面改成了现在的样子;
迁移脚本:
(my_env) $python3 manage.py db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'cms_user._password'
INFO  [alembic.autogenerate.compare] Detected removed column 'cms_user.password'
  Generating /Users/mac/PycharmProjects/bbc/migrations/versions/08504da615b9_.py
  ...  done
(my_env) $python3 manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 6f5a8c020ab4 -> 08504da615b9, empty message
(my_env) $python3 manage.py create_cms_user -u richard -p 123456 -e xxx@qq.com
cms用户添加成功

mysql中:

mysql> select * from cms_user;
+----+----------+---------------+---------------------+------------------------------------------------------------------------------------------------+
| id | username | email         | join_time           | _password                                                                                      |
+----+----------+---------------+---------------------+------------------------------------------------------------------------------------------------+
|  1 | richard  | 123456@qq.com | 2019-12-19 13:50:49 |                                                                                                |
|  2 | richard  | xxx@qq.com    | 2019-12-19 14:15:59 | pbkdf2:sha256:150000$59zHwBdv$878eeb2b1e8f94cb834f6ef67a023917692bc339fd2dcffafbc30883fc8ade89 |
+----+----------+---------------+---------------------+------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

    
    """
