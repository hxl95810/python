'''
Created on 2017年11月30日

@author: aprair
'''



from urllib import request
from lxml import etree
import MySQLdb
from builtins import int, str
from ctypes.wintypes import INT


conn = MySQLdb.connect(
    host='127.0.0.1',
    port =3306,
    user='root',
    passwd='root',
    db='lottery', 
    charset='utf8'
    )
cursor= conn.cursor()

date="20171128"

# date="20171201"

URL="http://kaijiang.500.com/static/public/ssc/xml/qihaoxml/"+date+".xml"

with request.urlopen(URL, timeout=4) as f:
    data = f.read()#.decode('utf-8')
 
html = etree.HTML(data)
result = etree.tostring(html)
 
 
result=html.xpath('//row')
 
for row in result:
    expect=row.xpath('@expect')
    expect=" ".join(expect)  
    
    date=expect[0:8] 
    expect=expect[-3:] 
    
    opencode_list=row.xpath('@opencode')
    
    
    myriabit=opencode_list[0][0]
    thousands=opencode_list[0][2]
    hundredsdigit=opencode_list[0][4]
    tensdigit=opencode_list[0][6]
    singledigit=opencode_list[0][8]
    
    #组合代码
    opencode=myriabit+thousands+hundredsdigit+tensdigit+singledigit
    
    #计算奇偶大小
    codesum=int(myriabit)+int(thousands)+int(hundredsdigit)+int(tensdigit)+int(singledigit)
    


    
    if codesum>=23:
        size="大"
    else:
        size="小"
    
    if (codesum % 2) == 0:
        parity="双"
    else:
        parity="单"
    
    codesum=str(codesum)
    
    opentime=row.xpath('@opentime')
    opentime=" ".join(opentime)  
    
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















