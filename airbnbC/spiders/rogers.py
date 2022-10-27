from urllib.request import Request
import scrapy, json

from airbnbC.items import AirbnbcItem


def fetch_amenities(amenities_list):
    amenities = []
    for amenity in amenities_list:
        amen = {amenity["title"]: {}}
        amen[amenity["title"]] = [a["title"] for a in amenity["amenities"]]

        amenities.append(amen)
    return amenities

class RogersSpider(scrapy.Spider):
    name = 'rogers'
    allowed_domains = ['www.airbnb.com']
    start_urls = ['https://www.airbnb.com/s/Rogers--Arkansas--United-States/homes', 'https://www.airbnb.com/s/Fayetteville--Arkansas--United-States/homes', 'https://www.airbnb.com/s/Springdale--Arkansas--United-States/homes']
    base_domain = 'https://www.airbnb.com'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
    }

    def parse(self, response):
        urls = response.css('a.ln2bl2p::attr(href)').getall()
        for url in urls:
            # yield {
            #     "url": self.base_domain + url
            # }
            yield scrapy.Request(
                f"{self.base_domain}{url}", callback=self.parse_single_urls
            )
        next_page = response.css('a._1bfat5l::attr(href)').get()
        if next_page is not None:
            yield response.follow(f"{self.base_domain}{next_page}", callback=self.parse)

    def parse_single_urls(self, response):
        item = AirbnbcItem()
        res = response.xpath('//*[@id="data-deferred-state"]/text()').get()
        res = json.loads(res)
        data = res["niobeMinimalClientData"][0][1]["data"]

        log_context = data["presentation"]["stayProductDetailPage"]["sections"]["metadata"]["loggingContext"]["eventDataLogging"]
        listingLat = log_context["listingLat"]
        listingLng = log_context["listingLng"]
        roomType = log_context["roomType"]
        listingId = log_context["listingId"]
        personCapacity = log_context["personCapacity"]
        accuracyRating = log_context["accuracyRating"]
        checkinRating = log_context["checkinRating"]
        communicationRating = log_context["communicationRating"]
        cleanlinessRating = log_context["cleanlinessRating"]
        locationRating = log_context["locationRating"]
        valueRating = log_context["valueRating"]
        guestSatisfactionOverall = log_context["guestSatisfactionOverall"]
        visibleReviewCount = log_context["visibleReviewCount"]

        title = data["presentation"]["stayProductDetailPage"]["sections"]["metadata"]["sharingConfig"]["title"]

        location = data["presentation"]["stayProductDetailPage"]["sections"]["metadata"]["sharingConfig"]["location"]

        image_url = data["presentation"]["stayProductDetailPage"]["sections"]["metadata"]["sharingConfig"]["imageUrl"]

        sections = data["presentation"]["stayProductDetailPage"]["sections"]["sections"]

        amenities, host_details, host_name, host_id, bedrooms, beds, bathrooms, location_details = [], {}, "", "", "", "", "", []

        for section in sections:
            if section["sectionComponentType"] == "AMENITIES_DEFAULT":
                amenities = fetch_amenities(section["section"]["seeAllAmenitiesGroups"])

            if section["sectionComponentType"] == "OVERVIEW_DEFAULT":
                host_details = section["section"]
                host_name = host_details["title"]
                host_id = host_details["hostAvatar"]["userId"]

                pdt_details = host_details["detailItems"]

                if pdt_details[1]:
                    bedrooms = pdt_details[1]["title"]
                if pdt_details[1]:
                    beds = pdt_details[2]["title"]
                if pdt_details[1]:
                    bathrooms = pdt_details[3]["title"]

            if section["sectionComponentType"] == "LOCATION_PDP" or section["sectionComponentType"] == "LOCATION_DEFAULT":
                if section["section"]["subtitle"]:
                    location_details = section["section"]["subtitle"].split(",")
                elif len(section["section"]["previewLocationDetails"]) > 0:
                    location_details = section["section"]["previewLocationDetails"][0]["title"].split(",")

        item["title"] = title
        item["listingId"] = listingId
        item["listingLat"] = listingLng
        item["listingLng"] = listingLat
        item["city"] = location_details[0]
        item["state"] = location_details[1]
        item["country"] = location_details[2]
        item["listingLng"] = listingLat
        item["listingLng"] = listingLat
        item["bedrooms"] = bedrooms
        item["beds"] = beds
        item["bathrooms"] = bathrooms
        item["host_name"] = host_name
        item["host_id"] = host_id
        # item["homeTier"] = 1
        item["roomType"] = roomType
        item["personCapacity"] = personCapacity
        item["amenities"] = amenities
        item["title"] = title
        item["location"] = location
        item["image_url"] = image_url
        item["ratings"] = {
            "accuracyRating": accuracyRating,
            "checkinRating": checkinRating,
            "cleanlinessRating": cleanlinessRating,
            "communicationRating": communicationRating,
            "locationRating": locationRating,
            "valueRating": valueRating,
            "guestSatisfactionOverall": guestSatisfactionOverall,
            "visibleReviewCount": visibleReviewCount
        }


        yield item
