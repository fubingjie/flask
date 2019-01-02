import requests from jsonpath
import jsonpath
import json

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
response = requests.get(url)
text = response.text
text_obj = json.loads(text, encoding="utf-8")
city_list = jsonpath(text_obj,"$..name") print(city_list)
city_list_str = json.dumps(city_list, ensure_ascii=False)
with open("全国城市.json", "w", encoding="utf-8") as f:
    f.write(city_list_str)
