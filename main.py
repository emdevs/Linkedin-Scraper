import requests
from apify_client import ApifyClient
from config import API_KEY

#init client
client = ApifyClient(API_KEY)

run_input = {
  "keywords": "data scientist",
  "location": "Belgium",
  "page_number": 1,
  "limit": 1
}

run = client.actor("apimaestro/linkedin-jobs-scraper-api").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
#print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)