from models.database import conn, users

data_base = users


def insert_data_db(user):
    insertion_query = data_base.insert().values({'email': user.get_email(),
                                                 'password': user.get_password(),
                                                 'twitter': user.get_twitter(),
                                                 'wallet': user.get_wallet(),
                                                 'balance': user.get_balance(),
                                                 'status': "Created"})
    conn.execute(insertion_query)
    conn.commit()


def get_data_db():
    select_all_query = data_base.select([data_base])
    select_all_results = conn.execute(select_all_query)
    return select_all_results.fetchall()

# def update_status(user, status):
