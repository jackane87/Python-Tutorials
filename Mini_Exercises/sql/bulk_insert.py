import pyodbc

conn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}', server = 'JMOORE-P16S\SQLEXPRESS', database = 'PythonTesting')
cursor = conn.cursor()

people = [('Roald', 'Amundsen'),
          ('Rosa', 'Parks'),
          ('Henry', 'Hudson'),
          ('Edsel', 'Ford'),
          ('Neil', 'Armstrong')]

#this will insert all in at once
#cursor.executemany('INSERT INTO friends VALUES (?,?)', people)

#this is a loop that will insert each person in people. This way allows you to run additional code for each person.
for person in people:
    cursor.execute('INSERT INTO friends VALUES (?,?)', person)
    print('Inserting now.')




conn.commit()
conn.close()