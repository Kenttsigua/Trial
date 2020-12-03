import urllib.request #for downloading image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time #for waiting
import tkinter
from tkinter import *
#top = tkinter.Tk()
options = Options()
#prefs = {"download.default_directory" : "C:\\Users\\jm\\Downloads\\intelligencia\\Asiayogies\\downloads"}
#options.add_experimental_option("prefs",prefs)
#options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'/Users/kennethsigua/Downloads/chromedriver')
urls=[]
# Code to add widgets will go here...
lnkcnt=0
msg='''
Be part of the Restart and Rebound of our economy--join L'ATTITUDE 2020

With the first partial list of participants confirmed to be part of L’ATTITUDE 2020, September 24- 27, this event has emerged as a critical national forum on the restart and rebound of our New Mainstream Economy. Among those who will be talking about the essential role of U.S. Latinos in leading our country’s economic recovery are:
Larry Fink – Chairman & CEO BlackRock, Inc.
Brian Moynihan – Chairman of the Board & CEO Bank of America
John Donahoe – President & CEO Nike, Inc.
Almar Latour – CEO Dow Jones & Publisher Wall Strimpeet Journal
Hans Vestberg – CEO Verizon
Oscar Munoz – Executive Chairman United Airlines
Tony Vinciquerra – Chairman & CEO Sony Pictures Entertainment
Jose Cil – CEO Restaurant Brands International
John Furner – President & CEO Walmart U.S.
Ryan Marshall – President and CEO PulteGroup, Inc.
Ryan Schneider – CEO and President Realogy
Roger Crandall – Chairman, President & CEO MassMutual
Maria Teresa Kumar – President and CEO Voto Latino
Rick Gomez – Executive Vice President, Chief Marketing, Digital and Strategy Officer Target Corporation
Diego Scotti – Chief Marketing Officer Verizon
Fernando Machado – Global Chief Marketing Officer Burger King
Leila Cobo – VP/Latin Industry Lead, Billboard
Eva Longoria – Actress/Entrepreneur/Philanthropist
Jose Andres – James Beard Award Winning Chef and Humanitarian
 
L’ATTITUDE is likely the only opportunity you’ll have to engage with this line-up of renowned leaders from across the American landscape up close and personal, and be able to ask questions during this live-cast event, streamed to you wherever you are and on whatever device. Every U.S. Latino business person who cares about our economy, as well as their own business or organization, can learn from these leaders, gain insight into their business strategies for economic growth, and be inspired with new thinking about your own business or career.

L’ATTITUDE a must-attend event for every U.S. Latino business professional, business owner, entrepreneur, media and entertainment professional, and political influencer. The agenda and all details are available at www.lattitude.net. You must be registered to attend. If you miss a session, all sessions will be available on demand after they are carried live. So you’re guaranteed not to miss a thing.

https://bit.ly/2ZOKPjf
Use Registration Code: LAT20PA upon check out. This will automatically add you to a pool of soon to be announced exclusive giveaways. We look forward to seeing you soon!
'''
name="Sol Trujillo"
email="sol@lattitude.net"

def collectd():
 global urls
 driver.get('https://www.tucsonhispanicchamber.org/directory.html')
 cnt = 0
 while 1==1:
  time.sleep(2)
  elems=driver.find_elements_by_xpath("//*[@id='results']/*/div/div[3]/a[*]")
  for elem in elems:
   if elem.text=='EMAIL':
    urls.append(elem.get_attribute('href'))
  try:
   driver.find_element_by_xpath("//*[@id='nextValue']").click()
  except:
   print("Stale")
  cnt=cnt+1
  if cnt>2: #73
   break

def fnext():
 global urls
 driver.get(urls[0])
 #name
 driver.find_element_by_xpath("//*[@id='form-table']/tbody/tr[1]/td[2]/input").send_keys(name)
 #mail
 driver.find_element_by_xpath("//*[@id='form-table']/tbody/tr[4]/td[2]/input").send_keys(email)
 #subjectline
 driver.find_element_by_xpath("//*[@id='form-table']/tbody/tr[6]/td[2]/textarea").send_keys(msg)



def fsubmit():
 print("test")
root=Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

# L1 = Label(frame, text="Start With:")
# L1.pack( side = LEFT)
# E1 = Entry(frame, bd =5)
# E1.pack(side = RIGHT)
B1 = tkinter.Button(frame, text ="Next", command = fnext)
B1.pack(side = LEFT)
B2 = tkinter.Button(frame, text ="Submit", command = fsubmit)
B2.pack(side = RIGHT)
B = tkinter.Button(bottomframe, text ="Start collecting", command = collectd)
B.pack(side = BOTTOM)



frame.mainloop()
