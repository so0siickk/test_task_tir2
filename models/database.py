import sqlalchemy as db

engine = db.create_engine('sqlite:///users.db')
conn = engine.connect()
metadata = db.MetaData()
users = db.Table('users', metadata,
                 db.Column('user_id', db.Integer, primary_key=True),
                 db.Column('email', db.Text),
                 db.Column('password', db.Integer),
                 db.Column('twitter', db.Text),
                 db.Column('wallet', db.Text),
                 db.Column('balance', db.Integer),
                 db.Column('status', db.Text))
metadata.create_all(engine)