# airbnbC
Scrape accomodation details in some cities in the united states

# How to Use
Create a virtual environment before doing the below.
- <code>pip install -r requirements.txt</code>
- FOR .csv OUTPUT run <code>*scrapy crawl rogers -O rog2.json*</code>
- FOR .json OUTPUT run <code>*scrapy crawl rogers -O rog2.csv*</code>

Running the above runs and saves to atlas mongo db as well as generate a csv or json as the case may be.