'''
Created on 2017年11月30日

@author: aprair
'''



from urllib import request

import MySQLdb
from builtins import int, str
from ctypes.wintypes import INT
from pyquery import PyQuery as pq
import re
import time
from lxml.doctestcompare import strip
import datetime


conn = MySQLdb.connect(
    host='127.0.0.1',
    port =3306,
    user='root',
    passwd='root',
    db='lottery', 
    charset='utf8'
    )
cursor= conn.cursor()

# 20161216
# date="20171128"

# date="20171201"

# URL="http://kaijiang.500.com/static/public/ssc/xml/qihaoxml/"+date+".xml"
# datetime.date(2014,6,1)  
sdate=datetime.date(2017,1,1)
edate=datetime.date(2017,2,1)


for i in range((edate - sdate).days+1):  
    day = sdate + datetime.timedelta(days=i)  
    
    URL="https://www.uni199.com/cqssc_result.php?sdate="+str(day)+"&sdate1="+str(day.strftime('%Y%m%d'))
    
    with request.urlopen(URL, timeout=4) as f:
        data = f.read()#.decode('utf-8')
     
    #     print(data)
    doc=pq(data)
     
    table=doc(".table_2 tr")
     
     
    for item in table.items():
     
     
        if item("th").eq(0).text() =="开奖期号":
            continue
     
         
        expect=item("td").eq(0).text()
        date=expect[0:8] 
        expect=expect[-3:] 
         
     
          
        opentime=item("td").eq(1).text()
          
    #     print(opentime)
        opencode_list=item("td").eq(2).text().replace(' ', '')
     
    #     print(opencode_list)
        opencode_arr=re.split(',',opencode_list)
         
         
          
        myriabit=opencode_arr[0]
        thousands=opencode_arr[1]
        hundredsdigit=opencode_arr[2]
        tensdigit=opencode_arr[3]
        singledigit=opencode_arr[4]
        #组合代码
        opencode=myriabit+thousands+hundredsdigit+tensdigit+singledigit
          
        codesum=item("td").eq(3).text()
        parity=item("td").eq(4).text()
        size=item("td").eq(5).text()
          
      
        sql_insert="""   
         insert into cqssc(date,expect,opencode,opentime,myriabit,thousands,hundredsdigit,tensdigit,singledigit,size,parity,codesum) 
         values 
        ("""+date+""",'"""+expect+"""','"""+opencode+"""','"""+opentime+"""',"""+myriabit+""","""+thousands+""","""+hundredsdigit+""","""+tensdigit+""","""+singledigit+""",'"""+size+"""','"""+parity+"""',"""+codesum+""")
        """
       
        try:
            cursor.execute(sql_insert)
            print (cursor.rowcount)
            conn.commit()
               
        except Exception as e:
            print (e)
            conn.rollback()
        
    
cursor.close()
conn.close()















