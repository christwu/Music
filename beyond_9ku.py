import requests
import re
import time
import json
from lxml import etree
from urllib import request


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

#page=int(input("请输入获取网页数量："))
songID=[] #列表存放歌曲编号
songName=[]  #列表存放歌曲名字
songID1=[] #列表存放歌曲编号
#构造url
for i in range(0,1):
	url="http://www.9ku.com/geshou/1019.htm"    # 许巍
	url="http://www.9ku.com/geshou/1075.htm"    #beyond
	req=request.Request(url,headers=header)
	data_html=request.urlopen(req).read().decode()
	print(data_html)

	html=etree.HTML(data_html)
	# pat1='//div[@class="singerMusic clearfix"]/ol[@id="fg"]//div[@class="songName"]/a/@href'
	# pat2='//div[@class="singerMusic clearfix"]/ol[@id="fg"]//div[@class="songName"]/a//text()'
	pat1='//div[@class="singerMusic clearfix"]//div[@class="songName"]/a/@href'
	pat2='//div[@class="singerMusic clearfix"]//div[@class="songName"]/a//text()'

	idlist=html.xpath(pat1)
	titlelist=html.xpath(pat2)
     #从网页中获取所有歌曲名字
	songID1.extend(idlist)   #把多个列表合成一个列表
	songName.extend(titlelist)
	# print(songID1)
	pat4='/play/(.*?).htm'
	for j in range(0,len(songID1)):
	    idlist2=re.findall(pat4,songID1[j])   #从网页中获取所有歌曲ID
	    songID.extend(idlist2)

print(songName)
print(songID)
print(len(songName))
print(len(songID))


#http://www.9ku.com/html/playjs/894/893142.js
#http://www.9ku.com/html/playjs/878/877683.js

for i in range(0,len(songID)):
	# songurl="http://mp32.9ku.com/upload/2016/03/22/62878.m4a"   #构造歌曲url
	# songurl="http://mp3.9ku.com/hot/2004/07-13/12697.mp3"
	num=int(songID[i][0:2])+1
	songurl="http://www.9ku.com/html/playjs/"+str(num)+"/"+str(songID[i])+".js"
	songname=songName[i]

	data2=requests.get(songurl).text  #二进
	# print(data2)

	pat3='"wma":"(.*?)","m4a"'
	url2=re.findall(pat3,data2)   #从网页中获取所有歌曲ID
	url3=url2[0]
	result_url = eval(repr(url3).replace('\\', ''))
	print(result_url)
	data=requests.get(result_url).content

	print("正在下载第",i+1,"首")
	with open("E:\\music6\\{}.mp3".format(songname),"wb") as f:
		f.write(data)
	time.sleep(0.5)
