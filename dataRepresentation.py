import re
from bs4 import BeautifulSoup

htmlFile2020 = open('C:/Users/Oracle/Documents/GitHub/Chor/gatechECEcourseDescriptions/ECE3084.html','r')

soup2020 = BeautifulSoup(htmlFile2020, "html.parser")

dataDT2020 = soup2020.find_all('dt')
dataDD2020 = soup2020.find_all('dd')

topOutlineStr = dataDT2020[5]
prereqStr = dataDT2020[1]

prereqInd = dataDT2020.index(prereqStr)
prereqData = dataDD2020[prereqInd].getText()

findStrList = ['CS','MATH','PHYS','ECE']
findMinStr = 'min'

prereqData = re.sub('[^a-zA-Z0-9 \n\.]', '', prereqData)

splitPreq = prereqData.split()

print(splitPreq)

strOccur = []
for subjStr in findStrList:
	strOccur = [i for i, w in enumerate(splitPreq) if w == subjStr] \
	+ strOccur

minStr = [i for i, w in enumerate(splitPreq) if w == findMinStr]

strOccur.sort()

print(strOccur)
print(minStr)

indOccur = 0
for ind in strOccur:	
	crsNumber = splitPreq[ind+1]
	if len(crsNumber) > 4:
		newCrsNumber = ''
		for i in range(int(len(crsNumber)/4)):
			newCrsNumber = newCrsNumber + crsNumber[4*(i):4*(i+1)] + '/'
		newCrsNumber = newCrsNumber[:len(newCrsNumber)-1]
		print(splitPreq[ind] + ' ' + newCrsNumber)
	else:
		print(splitPreq[ind] + ' ' + crsNumber)

