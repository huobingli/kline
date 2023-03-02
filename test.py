import json

f = open('test.json')
data = json.load(f)
# print(data["data"]["klines"])

txt = ""
for item in data["data"]["klines"]:
    ve = item.split(",")
    dataitem = "{date:\"" + ve[0] + "\",open:" + ve[1] + ",close:" + ve[2] + ",high:" + ve[3] + ",low:" + ve[4] + ",volume:" + ve[5] + "},"
    # print(dataitem)
    txt += dataitem

ft = open("data.txt", "w+")
ft.write(txt)