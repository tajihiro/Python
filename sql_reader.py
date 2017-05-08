sql = 'select id, name, email from sys_table A left join sys_user B on A.id = B.id'

sql_strings = sql.split(' ')

select_flg = False
from_flg = False
join_flg = False

for str in sql_strings:
    # SELECT判定
    if select_flg and (str.upper() != 'FROM'):
        print('COLUMN : ' + str)

    # FROM判定
    if from_flg:
        print('TABLE : ' + str)
        from_flg = False
    # JOIN判定
    if join_flg:
        print('TABLE : ' + str)
        join_flg = False

    if str.upper() == 'SELECT':
        select_flg = True
    if str.upper() == 'FROM':
        from_flg = True
        select_flg = False
    if str.upper() == 'JOIN':
        join_flg = True
