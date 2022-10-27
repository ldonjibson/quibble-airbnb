# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


class AirbnbcItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    listingId = scrapy.Field()
    listingLat = scrapy.Field()
    listingLng = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    listingLng = scrapy.Field()
    listingLng = scrapy.Field()
    bedrooms = scrapy.Field()
    beds = scrapy.Field()
    bathrooms = scrapy.Field()
    host_name = scrapy.Field()
    host_id = scrapy.Field()
    roomType = scrapy.Field()
    personCapacity = scrapy.Field()
    amenities = scrapy.Field()
    # title = scrapy.Field()
    location = scrapy.Field()
    image_url = scrapy.Field()
    ratings = scrapy.Field()
    
    # {
    #     accuracyRating = accuracyRating,
    #     checkinRating = checkinRating,
    #     cleanlinessRating = cleanlinessRating,
    #     communicationRating = communicationRating,
    #     locationRating = locationRating,
    #     valueRating = valueRating,
    #     guestSatisfactionOverall = guestSatisfactionOverall,
    #     visibleReviewCount = visibleReviewCount
    # }
