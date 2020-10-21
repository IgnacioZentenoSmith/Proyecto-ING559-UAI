import requests
import json
import urllib.request

"""
Get Commander legal cards ordered by price (descending). This should have enough assorted cards with no alphabetical
relation or uniform borders. These are the first three page results, 525 cards (175*3). The testing dataset is fairly 
intuitive, as you could simply make this same request but order the price in an ascending fashion
"""

image_urls = []
for i in range(1, 3):
    with open(f'json_data/data{i}.json') as json_file:
        data = json.load(json_file)
        for j in range(175):
            try:
                image_urls.append(data['data'][j]['image_uris']['normal'])
            except:
                pass
print(image_urls)
itr = 0
for i in image_urls:
    urllib.request.urlretrieve(i, f"img/mtg_{itr}.jpg")
    itr += 1
