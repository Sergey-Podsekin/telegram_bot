import package.utils.func

# Calculating weight difference
package.utils.func.calculate_dif()

# mycursor.execute('CREATE TABLE Person (name VARCHAR(50), role smallint UNSIGNED, lost_total smallint, '
#                 'balance smallint, best_loss smallint, worst_loss smallint,
#                 person_id int PRIMARY KEY AUTO_INCREMENT)')

# mycursor.execute('INSERT INTO Person (name, role) VALUES (%s,%s)', ("Sergey", 2))

# print(mycursor.execute('SELECT arthur_weight_req FROM weeks_history'))
'''mycursor.execute('SELECT * FROM weeks_history')

mycursor.execute('INSERT INTO arthur_weight_dif VALUE (%s)', (mycursor.execute('SELECT arthur_weight_req FROM weeks_history')))'''

'''mycursor.execute('SELECT * FROM weeks_history')

for i in mycursor.fetchall():
    sql = 'INSERT INTO weeks_history (arthur_weight_dif) VALUES (%s)'
    val = (i[2] * 10 - i[1] * 10) / 10
    mycursor.execute(sql, (val,))
    db.commit()
    print(mycursor.rowcount, "record inserted.")'''

'''mycursor.execute('SELECT arthur_weight_act FROM weeks_history WHERE id = 1')
print(mycursor.fetchone()[0])'''
# print(mycursor.execute('SELECT arthur_weight_act FROM weeks_history WHERE id = 1'))
# print(mycursor.)
# db.commit()
