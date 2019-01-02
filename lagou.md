'''py
import requests
from jsonpath import jsonpath
import json

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
response = requests.get(url)

text = response.text
# print(type(text))

# 把字符串转换成python的对象，列表或者字典
text_obj = json.loads(text, encoding="utf-8")

# 第一个参数要传python的字典或者列表对象
# 第二个参数是jsonPath的语法
city_list = jsonpath(text_obj,"$..name")
print(city_list)

# print(type(city_list))
# 转换成字符，才好保存
city_list_str = json.dumps(city_list, ensure_ascii=False)

with open("全国城市.json", "w", encoding="utf-8") as f:
    f.write(city_list_str)
'''
