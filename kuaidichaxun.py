import json,requests

packageNum = input('请输入快递单号:')
url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='+packageNum
compangName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
url2 = 'http://www.kuaidi100.com/query?type=' + compangName + '&postid=' + packageNum
for item in json.loads(requests.get(url2).text)['data']:
    print(item['time'],item['context'])
top = Tkinter.Tk()
top.mainloop()