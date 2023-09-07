import pyodbc

conn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}', server = 'JMOORE-P16S\SQLEXPRESS', database = 'PythonTesting')
cursor = conn.cursor()

#creating a table
#cursor.execute('CREATE TABLE friends (firstname varchar(40), lastname varchar(40))')

#inserting into a table hardcoded
#insert_query = '''INSERT INTO friends 
                    #Values ('Merriwether', 'Lewis');'''

#This is bad. Don't do this!!
#Inserting into sql using variables that were passed in. This can lead to SQL Injection.
'''form_first = 'Dana'
form_last = 'Carvery'
query = f"INSERT INTO friends VALUES ('{form_first}', '{form_last}')"'''


#Correct way using the ? marks. This helps protect us from SQL injection.
'''form_first = 'Wilbur'
form_last = 'Wildcat'
query = f"INSERT INTO friends VALUES (?,?)"
cursor.execute(query, (form_first, form_last))'''

#More realistic example of above.
data = ('Wilma', 'Wildcat')
query = f"INSERT INTO friends VALUES (?,?)"
cursor.execute(query, (data))

conn.commit()
conn.close()