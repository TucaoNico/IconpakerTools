import json as JS
from urllib.request import urlopen
from urllib.request import quote
from pprint import pprint
import _thread
import config as CF

f = open('getAppfilter.xml','w')
def writeFile(theString):
	f.write(theString)
	f.write('\n')
def getInfo(appName):

	# appName = input('请输入应用名')
	# appNameLink = 'http://nano.by-syk.com:8083/code/' + appName
	quotedAppName = quote(appName)
	print(quotedAppName)
	appNameLink = 'http://gxicon.e123.pw/code/' + quotedAppName
	appNameURL = urlopen(appNameLink)
	apiResponsed = JS.loads(appNameURL.read().decode('utf-8'))

	num = 0
	for i in apiResponsed['result']:
		# 搜索结果上限
		if num >= CF.maxResults:
			break
		print('第',num+1,'个结果：')
		print('应用名称 ',apiResponsed['result'][num]['label'])
		print('英文名称 ',apiResponsed['result'][num]['labelEn'])
		print('应用包名 ',apiResponsed['result'][num]['pkg'])
		print('启动项名 ',apiResponsed['result'][num]['launcher'])
		print('申请数量 ',apiResponsed['result'][num]['sum'])
		appfilterCode = '''应用代码  <item component="ComponentInfo{'''
		appfilterCode += apiResponsed['result'][num]['pkg']
		appfilterCode += '/'
		appfilterCode += apiResponsed['result'][num]['launcher']
		appfilterCode += '''}" drawable="'''
		appfilterCode += appName
		appfilterCode += '''" />'''
		print(appfilterCode,'\n')
		writeFile(appfilterCode[6:])
		num += 1

if CF.infiniteLoop:
	cnt = 1
	while True:
		getName = input('请输入应用名/包名(输入#停止):')
		if getName == '#':
			break
		getInfo(getName)
else:
	getName = input('请输入应用名/包名:')
	getInfo(getName)

print('所有代码已经保存在getAppfilter.xml文件里，程序退出')