'''
Created on 2017年12月1日

@author: aprair
'''

import MySQLdb
import datetime

sdate=datetime.date(2017,1,1)
edate=datetime.date(2017,2,1)

def logic(pexpect,field,date):

    cursor.execute("select "+field+" from cqssc where date="+date+" and expect="+str(pexpect)+"")
    
    presults = cursor.fetchall()
    
    for prow in presults:
        pfield=prow[0]
        
    return pfield


conn = MySQLdb.connect(
    host='127.0.0.1',
    port =3306,
    user='root',
    passwd='root',
    db='lottery', 
    charset='utf8'
    )
cursor= conn.cursor()



for i in range((edate - sdate).days+1):  
    day = sdate + datetime.timedelta(days=i)
    day=str(day.strftime('%Y%m%d'))
    sql_select="select * from cqssc where  date="+day+" order by expect asc"

    try:
        cursor.execute(sql_select)
        print (cursor.rowcount)
        results = cursor.fetchall()
     
    except Exception as e:
         
        print (e)
        conn.rollback()
     
     
     
    sizebetting=10
    paritybetting=10
     
    for row in results:
        id = row[0]
        expect = row[2]
        size = row[14]
        parity = row[15]
     
        pexpect=expect-1
     
        if expect ==1:
            continue
         
        psize=logic(pexpect,'size',day)
        pparity=logic(pexpect,'parity',day)
         
     
        if size==psize:
            sizeprofit=sizebetting*0.96
        else:
            sizeprofit=sizebetting-(sizebetting*2)
             
        if parity==pparity:
            parityprofit=paritybetting*0.96
        else:
            parityprofit=paritybetting-(paritybetting*2)
              
     
              
 
         
     
        try:
            aa=cursor.execute("update cqssc set sizebetting="+str(sizebetting)+",sizeprofit="+str(sizeprofit)+" where id="+str(id)+"")
            bb=cursor.execute("update cqssc set paritybetting="+str(paritybetting)+",parityprofit="+str(parityprofit)+" where id="+str(id)+"")
     
        except Exception as e:
            conn.rollback()
             
        if size==psize:
            sizebetting=10
        else:
            sizebetting=sizebetting*2
             
        if parity==pparity:
            paritybetting=10
        else:
            paritybetting=paritybetting*2
    
cursor.close()
conn.close()
