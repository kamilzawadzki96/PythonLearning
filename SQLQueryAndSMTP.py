import pyodbc
import smtplib
import datetime
import pandas as pd
import xlsxwriter

#execute SQL Query
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=server_name;'
    r'DATABASE=db_name;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)

cursor=cnxn.cursor()
cursor.execute("sql query")

result = []
xlsx = []

while 1:
    row = cursor.fetchone()
    if not row:
        break
    xlsx.append(row)
    result.append(str(row))

cursor.close()
cnxn.close()

df = pd.DataFrame(xlsx)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()

#build message
headers = {
    'Content-Type': 'text/html; charset=utf-8',
    'Content-Disposition': 'inline',
    'Content-Transfer-Encoding': '8bit',
    'From': 'sender e-mail',
    'To': 'recipent e-mail',
    'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
    'X-Mailer': 'python',
    'Subject': 'Python MsSQL'
}

msg = ''
for key, value in headers.items():
    msg += "%s: %s\n" % (key, value)

msg += "\n%s\n" % (result)

#send e-mail
smtp = smtplib.SMTP('smtp.office365.com', 587)
smtp.starttls()
smtp.login('login', 'pass') 

smtp.sendmail(headers['From'],headers["To"], msg.encode("utf8"))

smtp.quit()