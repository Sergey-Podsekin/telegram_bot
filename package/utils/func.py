from package.connectors import *


def calculate_dif():
    mycursor.execute('SELECT * FROM history')
    for i in mycursor.fetchall():
        query = f'UPDATE betting_minion.history SET user_weight_dif = {i[2] - i[3]} WHERE id = {i[-1]}'
        mycursor.execute(query)
        db.commit()
