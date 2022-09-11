
#from selenium import webdriver
import time,requests,bs4

'''browser = webdriver.Chrome()
browser.get('https://in.indeed.com/?r=india')

search_bar = browser.find_element_by_id('text-input-what')
search_bar.send_keys('Marketing')

location_bar = browser.find_element_by_name('l')
location_bar.send_keys('Delhi')

search_bar.submit()'''

#1.Digital Marketing Executive

res = requests.get('https://in.indeed.com/viewjob?jk=fcde6d077e5c04e9&q=marketing+&l=delhi&tk=1fonotajr3nnq000&from=web&advn=2036109558103323&adid=381151938&ad=-6NYlbfkN0CCNbDyDe_Jra1AfH4xp1MzeX2DWApzDrRAjvddhsrE8YWpmLLNbcrXxtZ15ZSTRNccsgxuGN_gR--nRV5e8c_Jfp3Rt_vbMjCZIXr-GqrFpe8dlpCF-X6Aqnj7tbBglsTD-xCZgRUQSeFDxQ1d45AMpWP3xovK9loX0TPTeBHgqF5Qz4rxhh7Agnv0ZW6KTDwQAu0YadWncv2mt9SJw0FZ5br-6PB3N-4oCHe-PvfV3qqGHqZAeOLu1mfeRdGLotgwX2xUA7eiHDRxudQSoDYQKlG-vh15VvQsaWnWdELTI0QkO32oIfuGukLk-UDPPARj5yI3t3NBVZp0DkM-0zHzwTQfUwXLnd_SgyZjyaqim0RoF3Z99AXt&pub=4a1b367933fd867b19b072952f68dceb&vjs=3')
res.raise_for_status()
print('1.Digital Marketing Executive\n')
exampleSoup = bs4.BeautifulSoup(res.text,'html.parser')
job = exampleSoup.select('.icl-u-xs-mb--xs')
print(job[0].getText())
salary=exampleSoup.select('div >span')
print(salary[1].getText())
elems=exampleSoup.select('#jobDescriptionText')
#print(elems[0].getText())
print('\n')

#2.Marketing Strategist

res1 = requests.get('https://in.indeed.com/viewjob?cmp=OroPocket&t=Marketing+Strategist&jk=30ae0946f025d4ef&q=marketing&vjs=3')
res1.raise_for_status()
print('2.Marketing Strategist\n')
exampleSoup1 = bs4.BeautifulSoup(res1.text,'html.parser')
job1 = exampleSoup1.select('.icl-u-xs-mb--xs')
print(job1[0].getText())
salary1=exampleSoup1.select('div>span')
print(salary1[1].getText())
elems1=exampleSoup1.select('#jobDescriptionText')
#print(elems1[0].getText())
print('\n')

#3.Marketing research Internship

res2 = requests.get('https://in.indeed.com/viewjob?jk=6951a3a40fac573b&tk=1foqa8hccttvp801&from=serp&vjs=3')
res2.raise_for_status()
print('3.Marketing research Internship\n')
exampleSoup2 = bs4.BeautifulSoup(res2.text,'html.parser')
job2 = exampleSoup2.select('.icl-u-xs-mb--xs')
print(job2[0].getText())
salary2 = "NULL"
print(salary2)
elems2=exampleSoup2.select('#jobDescriptionText')
#print(elems2[0].getText())





