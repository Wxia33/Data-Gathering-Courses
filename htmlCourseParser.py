import re
from bs4 import BeautifulSoup

htmlFile2020 = open('C:/Users/Oracle/Documents/GitHub/Chor/gatechECEcourseDescriptions/ECE2020.html','r')
htmlFile2026 = open('C:/Users/Oracle/Documents/GitHub/Chor/gatechECEcourseDescriptions/ECE2026.html','r')
htmlFile2040 = open('C:/Users/Oracle/Documents/GitHub/Chor/gatechECEcourseDescriptions/ECE2040.html','r')

soup2020 = BeautifulSoup(htmlFile2020, "html.parser")
soup2026 = BeautifulSoup(htmlFile2026, "html.parser")
soup2040 = BeautifulSoup(htmlFile2040, "html.parser")

dataDT2020 = soup2020.find_all('dt')
dataDD2020 = soup2020.find_all('dd')

dataDT2026 = soup2026.find_all('dt')
dataDD2026 = soup2026.find_all('dd')

dataDT2040 = soup2040.find_all('dt')
dataDD2040 = soup2040.find_all('dd')

topOutlineStr = dataDT2020[5]

soupDTList = [dataDT2020, dataDT2026, dataDT2040]
soupDDList = [dataDD2020, dataDD2026, dataDD2040]

#userLearnStr = input('What would you like to learn? ')
userLearnStr = "Fourier Transform"
userLearnList = userLearnStr.lower().split()
print(userLearnList)

for soupDT, soupDD in zip(soupDTList, soupDDList):
	indData = soupDT.index(topOutlineStr)
	stripped = soupDD[indData].getText().strip("\n\t")
	redStr = re.sub(r'\b\w{0,3}\b', '', stripped)
	redStr = re.sub(r'[.,&()/]', '', redStr)
	redStr = re.sub(r'"', '', redStr)

	bagWords = redStr.lower().split()
	bagWords = [soupDT[0].getText()] + bagWords

	if (not set(userLearnList).isdisjoint(bagWords)):
		print(bagWords[0])

