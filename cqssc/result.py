'''
Created on 2017年12月2日

@author: aprair
'''

import MySQLdb
import datetime

# date="20171130"
date="20170529"

conn = MySQLdb.connect(
    host='127.0.0.1',
    port =3306,
    user='root',
    passwd='root',
    db='lottery', 
    charset='utf8'
    )
cursor= conn.cursor()


sdate=datetime.date(2017,1,1)
edate=datetime.date(2017,1,10)

for i in range((edate - sdate).days+1):  
    day = sdate + datetime.timedelta(days=i)  
    day=str(day.strftime('%Y%m%d'))

    sql_select="select sum(sizeprofit) as sizeprofit,sum(parityprofit) as parityprofit from cqssc where  date="+day+" order by expect asc"
    
    
    try:
        cursor.execute(sql_select)
        results = cursor.fetchall()
        
        cursor.execute("select  sizebetting from cqssc where date="+date+" and sizebetting>1000")
        risksize = cursor.fetchall()
        
        cursor.execute("select  paritybetting from cqssc where date="+date+" and  paritybetting>1000")
        riskparity = cursor.fetchall()
        
    except Exception as e:
        print (e)
        conn.rollback()
        
    for row in results:
        print(day+"size:总数"+str(row[0]))
        print(day+"parity:总数"+str(row[1]))
     
    
#     for row in risksize:
#         print(day+"size:"+str(row[0]))
#     
#     for row in riskparity:
#         print(day+"parity:"+str(row[0]))

    