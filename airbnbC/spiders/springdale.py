import scrapy


class SpringdaleSpider(scrapy.Spider):
    name = 'springdale'
    allowed_domains = ['www.airbnb.com']
    start_urls = ['https://www.airbnb.com/s/Springdale--Arkansas--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&date_picker_type=flexible_dates&flexible_trip_dates%5B%5D=december&source=structured_search_input_header&search_type=search_query']

    def parse(self, response):
        pass
