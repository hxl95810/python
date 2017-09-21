# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import response

import time
import datetime
from datetime import date

from urllib import parse
import re
from win007spider.items import Win007MatchItem, TakeFirstItemLoader,\
    Win007HandicapSbItem
    

from scrapy.http import Request
import sys

class Win007Spider(scrapy.Spider):
    name = 'win007'
    allowed_domains = ['www.win007.com']
#     start_urls = ['http://score.nowscore.com/data/score.aspx?date=2017/9/1']
    start_urls = []
    #获取全部翻页链接

    begin = date.fromtimestamp(int(time.mktime(time.strptime("2017-09-03", "%Y-%m-%d"))))    
    end = date.fromtimestamp(int(time.mktime(time.strptime("2017-09-03", "%Y-%m-%d"))))    

#     end = date.today()
    
    for i in range((end - begin).days+1):
        x_day = begin + datetime.timedelta(days=i)  
        urls='http://score.nowscore.com/data/score.aspx?date=%s' % x_day
        start_urls.append(urls)
        
    
    
#matchStatus  0为未开场，-1为完场，-11为待定,12为腰斩,14为推迟


    headers = {
        "HOST": "www.310win.com",
        
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }
    
    handle_httpstatus_list = [404]

    def parse(self, response):
        
        tdate=parse.urlparse(response.url).query.split("=")[1]
        
        jbscore=response.text
        jbscore=jbscore.replace('\r\n','')
        jbarr=jbscore.split(";")

        matchcount=int(re.sub("\D","",jbarr[3]))+5
        sclasscount=int(re.sub("\D","",jbarr[4]))+matchcount

        
        jbmatch= jbarr[5:matchcount]    #获取比赛信息
        jbsclass= jbarr[matchcount:sclasscount] #获取比赛分类

        a=[]
        for matchrow in jbmatch:
           
            matchdata=re.sub('<[^>]+>','',matchrow).split("=")
            matchdata[1]=matchdata[1].replace('[','')
            matchdata[1]=matchdata[1].replace(']','')
            matchdata[1]=matchdata[1].replace('\'','')

            newmatchdata = matchdata[1].split(',')
            a.append(newmatchdata)
        b=[]
        for sclassrow in jbsclass:
           
            sclassdata=re.sub('<[^>]+>','',sclassrow).split("=")
            sclassdata[1]=sclassdata[1].replace('[','')
            sclassdata[1]=sclassdata[1].replace(']','')
            sclassdata[1]=sclassdata[1].replace('\'','')

            newsclassdata = sclassdata[1].split(',')
            b.append(newsclassdata)

        for row in a:
            
            matchId = row[0] #比赛id
            cnHome = row[4] #主队名称
            hkHome = row[5] #主队繁体名称
            enHome = row[6] #主队英文名称
            
            cnGuest = row[7] #客队名称
            hkGuest = row[8] #客队繁体名称
            enGuest=row[9]#客队英文名称
            
            matchTime = row[10] #比赛时间
            matchStatus = row[12] #比赛状态 -1为完场 z
            
            homeGoal = row[13] #主队得分
            guestGoal = row[14] #队客得分
            matchHandicap = row[25] #比赛盘口
            matchClass = b[int(row[1])][1] #联赛分类
            homeRanking = row[21] #主队排名
            guestRanking = row[22] #客队排名
            
            matchScroll=row[24] #True sb为滚 z
            matchTime = matchTime[0:8]+' '+matchTime[-5:]
            
            
            if matchHandicap =='' or  matchStatus!='-1' or matchScroll!="True":
                continue
            


            get_url = 'http://www.310win.com/handicap/' + matchId + '.html' #采集盘口水位地址
#             print (get_url)
#             print (cnHome)
#             print (matchClass)
            item_loader = Win007MatchItem()
            item_loader["date"]=tdate
            item_loader["matchId"]=matchId
            item_loader["cnHome"]=cnHome
            item_loader["hkHome"]=hkHome
            item_loader["enHome"]=enHome
            item_loader["cnGuest"]=cnGuest
             
            item_loader["hkGuest"]=hkGuest
            item_loader["enGuest"]=enGuest
            item_loader["matchTime"]=matchTime
            item_loader["homeGoal"]=homeGoal
             
            item_loader["guestGoal"]=guestGoal
            item_loader["matchHandicap"]=matchHandicap
            item_loader["matchClass"]=matchClass
            item_loader["homeRanking"]=homeRanking
            item_loader["guestRanking"]=guestRanking
            
#             item_loader = TakeFirstItemLoader(item=Win007MatchItem(), response=response)
#             item_loader = Win007MatchItem()
# 
#             item_loader.add_value("date", tdate)
#             item_loader.add_value("matchId", matchId)
#             item_loader.add_value("cnHome", cnHome)
#             item_loader.add_value("hkHome", hkHome)
#             item_loader.add_value("enHome", enHome)
#             item_loader.add_value("cnGuest", cnGuest)
#             item_loader.add_value("hkGuest", hkGuest)
#             item_loader.add_value("enGuest", enGuest)
#             item_loader.add_value("matchTime", matchTime)
#             item_loader.add_value("homeGoal", homeGoal)
#             item_loader.add_value("guestGoal", guestGoal)
#             item_loader.add_value("matchHandicap", matchHandicap)
#             item_loader.add_value("matchClass", matchClass)
#             item_loader.add_value("homeRanking", homeRanking)
#             item_loader.add_value("guestRanking", guestRanking)
#             item_loader = item_loader.load_item()

            yield scrapy.Request(get_url, headers=self.headers,callback=self.parse_detail,dont_filter=True)
            yield item_loader
            
#             yield Request(url=post_url, callback=self.parse_detail,dont_filter=True)



    def parse_detail(self, response):
        handicapUrl=parse.urlparse(response.url)
        
        i = len(handicapUrl.path) - 1
        while i > 0:
            if handicapUrl.path[i] == '/':
                break
            i = i - 1
        
        matchId=handicapUrl.path[i+1:len(handicapUrl.path)].split('.')[0]
        
        
        

        #初盘
        sb_starthandicap=response.css("#odds > table > tr:nth-child(3) > td:nth-child(3) ::text").extract()[0]#sb
        bet365_starthandicap = response.css("#odds > table > tr:nth-child(4) > td:nth-child(3) ::text").extract()[0] #365
        ladbrokes_starthandicap = response.css("#odds > table > tr:nth-child(6) > td:nth-child(3) ::text").extract()[0] #立博
        betvictor_starthandicap = response.css("#odds > table > tr:nth-child(7) > td:nth-child(3) ::text").extract()[0] #韦德

        #终盘
        sb_overhandicap=response.css("#odds > table > tr:nth-child(3) > td:nth-child(6) ::text").extract()[0]#sb
        bet365_overhandicap=response.css("#odds > table > tr:nth-child(4) > td:nth-child(6) ::text").extract()[0]#sb
        ladbrokes_overhandicap=response.css("#odds > table > tr:nth-child(6) > td:nth-child(6) ::text").extract()[0]#sb
        betvictor_overhandicap=response.css("#odds > table > tr:nth-child(7) > td:nth-child(6) ::text").extract()[0]#sb
        
        #初盘水位
        sb_homestartodds=response.css("#odds > table > tr:nth-child(3) > td:nth-child(2) ::text").extract()[0].strip() #sb水位(主队初盘)
        sb_gueststartodds=response.css("#odds > table > tr:nth-child(3) > td:nth-child(4) ::text").extract()[0].strip()  #sb水位(客队初盘)
        bet365_homestartodds=response.css("#odds > table > tr:nth-child(4) > td:nth-child(2) ::text").extract()[0].strip()  #365水位(主队初盘)
        bet365_gueststartodds=response.css("#odds > table > tr:nth-child(4) > td:nth-child(4) ::text").extract()[0].strip()  #365水位(客队初盘)
        ladbrokes_homestartodds=response.css("#odds > table > tr:nth-child(6) > td:nth-child(2) ::text").extract()[0].strip()  #立博水位(主队初盘)
        ladbrokes_gueststartodds=response.css("#odds > table > tr:nth-child(6) > td:nth-child(4) ::text").extract()[0].strip()  #立博水位(客队初盘)
        betvictor_homestartodds=response.css("#odds > table > tr:nth-child(7) > td:nth-child(2) ::text").extract()[0].strip()  #韦德水位(主队初盘)
        betvictor_gueststartodds=response.css("#odds > table > tr:nth-child(7) > td:nth-child(4) ::text").extract()[0].strip() #韦德水位(客队初盘)
        
        sb_homestartodds=float(sb_homestartodds or 0) *1000
        sb_gueststartodds=float(sb_gueststartodds or 0) *1000
        bet365_homestartodds=float(bet365_homestartodds or 0) *1000
        bet365_gueststartodds=float(bet365_gueststartodds or 0) *1000
        ladbrokes_homestartodds=float(ladbrokes_homestartodds or 0) *1000
        ladbrokes_gueststartodds=float(ladbrokes_gueststartodds or 0) *1000
        betvictor_homestartodds=float(betvictor_homestartodds or 0) *1000
        betvictor_gueststartodds=float(betvictor_gueststartodds or 0) *1000
        
        
        #终盘水位
        sb_homeoverodds=response.css("#odds > table > tr:nth-child(3) > td:nth-child(5) ::text").extract()[0].strip()  #sb水位(主队终盘)
        sb_guestoverodds=response.css("#odds > table > tr:nth-child(3) > td:nth-child(7) ::text").extract()[0].strip() #sb水位(客队终盘)
        bet365_homeoverodds=response.css("#odds > table > tr:nth-child(4) > td:nth-child(5) ::text").extract()[0].strip()  #365水位(主队终盘)
        bet365_guestoverodds=response.css("#odds > table > tr:nth-child(4) > td:nth-child(7) ::text").extract()[0].strip()  #365水位(客队终盘)
        ladbrokes_homeoverodds=response.css("#odds > table > tr:nth-child(6) > td:nth-child(5) ::text").extract()[0].strip()  #立博水位(主队终盘)
        ladbrokes_guestoverodds=response.css("#odds > table > tr:nth-child(6) > td:nth-child(7) ::text").extract()[0].strip()  #立博水位(客队终盘)
        betvictor_homeoverodds=response.css("#odds > table > tr:nth-child(7) > td:nth-child(5) ::text").extract()[0].strip()  #韦德水位(主队终盘)
        betvictor_guestoverodds=response.css("#odds > table > tr:nth-child(7) > td:nth-child(7) ::text").extract()[0].strip()  #韦德水位(客队终盘)
        
        sb_homeoverodds=float(sb_homeoverodds or 0) *1000
        sb_guestoverodds=float(sb_guestoverodds or 0) *1000
        bet365_homeoverodds=float(bet365_homeoverodds or 0) *1000
        bet365_guestoverodds=float(bet365_guestoverodds or 0) *1000
        ladbrokes_homeoverodds=float(ladbrokes_homeoverodds or 0) *1000
        ladbrokes_guestoverodds=float(ladbrokes_guestoverodds or 0) *1000
        betvictor_homeoverodds=float(betvictor_homeoverodds or 0) *1000
        betvictor_guestoverodds=float(betvictor_guestoverodds or 0) *1000

        sb_company=response.css("#odds > table > tr:nth-child(3) > td:nth-child(1) ::text").extract()[0].replace('走地','').strip()
        bet365_company=response.css("#odds > table > tr:nth-child(4) > td:nth-child(1) ::text").extract()[0].replace('走地','').strip()
        ladbrokes_company=response.css("#odds > table > tr:nth-child(6) > td:nth-child(1) ::text").extract()[0].replace('走地','').strip()
        betvictor_company=response.css("#odds > table > tr:nth-child(7) > td:nth-child(1) ::text").extract()[0].replace('走地','').strip()
        
        #采集判断水位
#         if bet365_homestartodds+bet365_gueststartodds==1900:
#             pass
#         else:
#             continue;
        
        size_url ='http://www.310win.com/overunder/'+matchId+'.html' #大小
        
        SbItem = Win007HandicapSbItem()
        SbItem["matchid"]=int(matchId)
        SbItem["company"]=sb_company
        SbItem["asian_homestartodds"]=sb_homestartodds
        SbItem["asian_gueststartodds"]=sb_gueststartodds
        SbItem["asian_starthandicap"]=sb_starthandicap
        SbItem["asian_homeoverodds"]=sb_homeoverodds
        SbItem["asian_guestoverodds"]=sb_guestoverodds
        SbItem["asian_overhandicap"]=sb_overhandicap
        
#         SbItem["size_homestartodds"]=sb_homestarsize
#         SbItem["size_gueststartodds"]=sb_gueststarsize
#         SbItem["size_starthandicap"]=sb_startsize
#         SbItem["size_homeoverodds"]=sb_homeoversize
#         SbItem["size_guestoverodds"]=sb_guestoversize
#         SbItem["size_overhandicap"]=sb_oversize



        
        request = scrapy.Request(size_url,headers=self.headers,callback=self.parse_size,dont_filter=True)
        request.meta['SbItem'] = SbItem
        yield request
        
#         yield scrapy.Request(get_url, headers=self.headers,callback=self.parse_detail,dont_filter=True)
        
        
        

        
    def parse_size(self,response):
        
        sb_startsize=response.css("#td_22::text").extract()[0]
        bet365_startsize=response.css("#td_42::text").extract()[0]
        ladbrokes_startsize=response.css("#td_32::text").extract()[0]
        betvictor_startsize=response.css("#td_62::text").extract()[0]
        
        sb_oversize=response.css("#td_25::text").extract()[0]
        bet365_oversize=response.css("#td_45::text").extract()[0]
        ladbrokes_oversize=response.css("#td_35::text").extract()[0]
        betvictor_oversize=response.css("#td_65::text").extract()[0]

        sb_homestarsize=response.css("#td_21::text").extract()[0]
        sb_gueststarsize=response.css("#td_23::text").extract()[0]
        bet365_homestarsize=response.css("#td_41::text").extract()[0]
        bet365_gueststarsize=response.css("#td_43::text").extract()[0]
        ladbrokes_homestarsize=response.css("#td_31::text").extract()[0]
        ladbrokes_gueststarsize=response.css("#td_33::text").extract()[0]
        betvictor_homestarsize=response.css("#td_61::text").extract()[0]
        betvictor_gueststarsize=response.css("#td_63::text").extract()[0]
        
        sb_homeoversize=response.css("#td_24::text").extract()[0]
        sb_guestoversize=response.css("#td_26::text").extract()[0]
        bet365_homeoversize=response.css("#td_44::text").extract()[0]
        bet365_guestoversize=response.css("#td_46::text").extract()[0]
        ladbrokes_homeoversize=response.css("#td_34::text").extract()[0]
        ladbrokes_guestoversize=response.css("#td_36::text").extract()[0]
        betvictor_homeoversize=response.css("#td_64::text").extract()[0]
        betvictor_guestoversize=response.css("#td_66::text").extract()[0]
        
        
#                 $sb_homeoversize = pq("#odds tr:eq(3) td:eq(4)")->text() * 1000; 
#                 $sb_guestoversize = pq("#odds tr:eq(3) td:eq(6)")->text() * 1000; 
#                 $bet365_homeoversize = pq("#odds tr:eq(5) td:eq(4)")->text() * 1000; 
#                 $bet365_guestoversize = pq("#odds tr:eq(5) td:eq(6)")->text() * 1000; 
#                 $ladbrokes_homeoversize = pq("#odds tr:eq(4) td:eq(4)")->text() * 1000; 
#                 $ladbrokes_guestoversize = pq("#odds tr:eq(4) td:eq(6)")->text() * 1000; 
#                 $betvictor_homeoversize = pq("#odds tr:eq(7) td:eq(4)")->text() * 1000; 
#                 $betvictor_guestoversize = pq("#odds tr:eq(7) td:eq(6)")->text() * 1000; 


        
        SbItem = response.meta['SbItem']
        SbItem["size_homestartodds"]=sb_homestarsize
        SbItem["size_gueststartodds"]=sb_gueststarsize
        SbItem["size_starthandicap"]=sb_startsize
        SbItem["size_homeoverodds"]=sb_homeoversize
        SbItem["size_guestoverodds"]=sb_guestoversize
        SbItem["size_overhandicap"]=sb_oversize
        
        yield SbItem
        
        


    

    
    


