# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst




class Win007SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TakeFirstItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()


class Win007MatchItem(scrapy.Item):
    
    date=scrapy.Field()
    matchId=scrapy.Field()
    cnHome=scrapy.Field()
    hkHome=scrapy.Field()
    enHome=scrapy.Field()
    cnGuest=scrapy.Field()
    hkGuest=scrapy.Field()
    enGuest=scrapy.Field()
    matchTime=scrapy.Field()
#     matchStatus=scrapy.Field()
    homeGoal=scrapy.Field()
    guestGoal=scrapy.Field()
    matchHandicap=scrapy.Field()
    matchClass=scrapy.Field()
    homeRanking=scrapy.Field()
    guestRanking=scrapy.Field()
#     matchScroll=scrapy.Field()
    def get_insert_sql(self):
        
        insert_sql="""
            insert into think_match(date,matchId,matchHandicap,matchTime,matchClass,cnHome,hkHome,enHome,cnGuest,hkGuest,enGuest,homeGoal,guestGoal,homeRanking,guestRanking)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        params = (self["date"], self["matchId"], self["matchHandicap"], self["matchTime"], self["matchClass"], self["cnHome"], self["hkHome"], self["enHome"], self["cnGuest"], self["hkGuest"], self["enGuest"], self["homeGoal"], self["guestGoal"], self["homeRanking"], self["guestRanking"])
        
        return insert_sql, params
    
class Win007HandicapSbItem(scrapy.Item) :
    matchid=scrapy.Field()
    company=scrapy.Field()
    asian_homestartodds=scrapy.Field()
    asian_gueststartodds=scrapy.Field()
    asian_starthandicap=scrapy.Field()
    asian_homeoverodds=scrapy.Field()
    asian_guestoverodds=scrapy.Field()
    asian_overhandicap=scrapy.Field()
    size_homestartodds=scrapy.Field()
    size_gueststartodds=scrapy.Field()
    size_starthandicap=scrapy.Field()
    size_homeoverodds=scrapy.Field()
    size_guestoverodds=scrapy.Field()
    size_overhandicap=scrapy.Field()
     
    def get_insert_sql(self):
        insert_sql="""
            insert into think_handicap_sb(matchid,company,asian_homestartodds,asian_gueststartodds,asian_starthandicap,asian_homeoverodds,asian_guestoverodds,asian_overhandicap,size_homestartodds,size_gueststartodds,size_starthandicap,size_homeoverodds,size_guestoverodds,size_overhandicap)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        params = (self["matchid"], self["company"], self["asian_homestartodds"], self["asian_gueststartodds"], self["asian_starthandicap"], self["asian_homeoverodds"], self["asian_guestoverodds"], self["asian_overhandicap"], self["size_homestartodds"], self["size_gueststartodds"], self["size_starthandicap"], self["size_homeoverodds"], self["size_guestoverodds"], self["size_overhandicap"])
        
        return insert_sql, params
    
class Win007HandicapBet365Item(scrapy.Item) :
    matchid=scrapy.Field()
    company=scrapy.Field()
    asian_homestartodds=scrapy.Field()
    asian_gueststartodds=scrapy.Field()
    asian_starthandicap=scrapy.Field()
    asian_homeoverodds=scrapy.Field()
    asian_guestoverodds=scrapy.Field()
    asian_overhandicap=scrapy.Field()
    size_homestartodds=scrapy.Field()
    size_gueststartodds=scrapy.Field()
    size_starthandicap=scrapy.Field()
    size_homeoverodds=scrapy.Field()
    size_guestoverodds=scrapy.Field()
    size_overhandicap=scrapy.Field()
      
    def get_insert_sql(self):
        insert_sql="""
            insert into think_handicap_bet365(matchid,company,asian_homestartodds,asian_gueststartodds,asian_starthandicap,asian_homeoverodds,asian_guestoverodds,asian_overhandicap,size_homestartodds,size_gueststartodds,size_starthandicap,size_homeoverodds,size_guestoverodds,size_overhandicap)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        params = (self["matchid"], self["company"], self["asian_homestartodds"], self["asian_gueststartodds"], self["asian_starthandicap"], self["asian_homeoverodds"], self["asian_guestoverodds"], self["asian_overhandicap"], self["size_homestartodds"], self["size_gueststartodds"], self["size_starthandicap"], self["size_homeoverodds"], self["size_guestoverodds"], self["size_overhandicap"])
        
        return insert_sql, params

class Win007HandicapLadbrokesItem(scrapy.Item) :
    matchid=scrapy.Field()
    company=scrapy.Field()
    asian_homestartodds=scrapy.Field()
    asian_gueststartodds=scrapy.Field()
    asian_starthandicap=scrapy.Field()
    asian_homeoverodds=scrapy.Field()
    asian_guestoverodds=scrapy.Field()
    asian_overhandicap=scrapy.Field()
    size_homestartodds=scrapy.Field()
    size_gueststartodds=scrapy.Field()
    size_starthandicap=scrapy.Field()
    size_homeoverodds=scrapy.Field()
    size_guestoverodds=scrapy.Field()
    size_overhandicap=scrapy.Field()
      
    def get_insert_sql(self):
        insert_sql="""
            insert into think_handicap_ladbrokes(matchid,company,asian_homestartodds,asian_gueststartodds,asian_starthandicap,asian_homeoverodds,asian_guestoverodds,asian_overhandicap,size_homestartodds,size_gueststartodds,size_starthandicap,size_homeoverodds,size_guestoverodds,size_overhandicap)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        params = (self["matchid"], self["company"], self["asian_homestartodds"], self["asian_gueststartodds"], self["asian_starthandicap"], self["asian_homeoverodds"], self["asian_guestoverodds"], self["asian_overhandicap"], self["size_homestartodds"], self["size_gueststartodds"], self["size_starthandicap"], self["size_homeoverodds"], self["size_guestoverodds"], self["size_overhandicap"])
        
        return insert_sql, params
    
class Win007HandicapBetvictorItem(scrapy.Item) :
    matchid=scrapy.Field()
    company=scrapy.Field()
    asian_homestartodds=scrapy.Field()
    asian_gueststartodds=scrapy.Field()
    asian_starthandicap=scrapy.Field()
    asian_homeoverodds=scrapy.Field()
    asian_guestoverodds=scrapy.Field()
    asian_overhandicap=scrapy.Field()
    size_homestartodds=scrapy.Field()
    size_gueststartodds=scrapy.Field()
    size_starthandicap=scrapy.Field()
    size_homeoverodds=scrapy.Field()
    size_guestoverodds=scrapy.Field()
    size_overhandicap=scrapy.Field()
      
    def get_insert_sql(self):
        insert_sql="""
            insert into think_handicap_betvictor(matchid,company,asian_homestartodds,asian_gueststartodds,asian_starthandicap,asian_homeoverodds,asian_guestoverodds,asian_overhandicap,size_homestartodds,size_gueststartodds,size_starthandicap,size_homeoverodds,size_guestoverodds,size_overhandicap)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        params = (self["matchid"], self["company"], self["asian_homestartodds"], self["asian_gueststartodds"], self["asian_starthandicap"], self["asian_homeoverodds"], self["asian_guestoverodds"], self["asian_overhandicap"], self["size_homestartodds"], self["size_gueststartodds"], self["size_starthandicap"], self["size_homeoverodds"], self["size_guestoverodds"], self["size_overhandicap"])
        
        return insert_sql, params
    
    