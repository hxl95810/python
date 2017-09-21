# -*- coding: utf-8 -*-
import datetime
import time
from datetime import date

begin=("2017-09-01")
end=("2017-09-17")




# beginArray = time.strptime(begin, "%Y-%m-%d")
# beginStamp = int(time.mktime(beginArray))
# begin = date.fromtimestamp(beginStamp)
# 
# endArray = time.strptime(end, "%Y-%m-%d")
# endStamp = int(time.mktime(endArray))
# end = date.fromtimestamp(endStamp)



begin = date.fromtimestamp(int(time.mktime(time.strptime(begin, "%Y-%m-%d"))))
 


end = date.today()

for i in range((end - begin).days+1):
    x_day = begin + datetime.timedelta(days=i)  
    urls='http://score.nowscore.com/data/score.aspx?date=%s' % x_day
    print (urls)



#     