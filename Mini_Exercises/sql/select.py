import pyodbc

conn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}', server = 'JMOORE-P16S\SQLEXPRESS', database = 'PythonTesting')
cursor = conn.cursor()

#cursor.execute("Select * From friends WHERE firstname = 'Edsel'")

#looping over each result in the cursor.execute and printing
#for result in cursor:
    #print(result)

#This gets all results as a list
#print(cursor.fetchall())

#this gets one result
#print(cursor.fetchone())

