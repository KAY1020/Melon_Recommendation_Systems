#!/usr/bin/env python
# coding: utf-8

# In[311]:


# import selenium for automatic test
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime as dt
import requests
import numpy as np
import pandas as pd


# In[312]:


#set path of the Chrome web driver
driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver')

#Access to melon login webpage using Chrome
#driver.get('https://member.melon.com/muid/web/login/login_inform.htm')

#driver.find_element_by_xpath('//*[@id="conts_section"]/div/div/div[1]/button').click()

#Enter the User ID and password(wait for 0.5s each)

driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DmKzaPWr6tQ%2540OGJOvAySTa5R5SBDdTczwfeDkz7ahV7W6kLpno0nj28PNd7wPg5F38gdOoqFJLvzZDJ%2540hkGafCg%253D%253D%26encode_state%3Dtrue')

#handle= driver.getWindowHandle()

sleep(0.5)

driver.find_element_by_id("id_email_2").send_keys('qlqlwns1997@gmail.com')

sleep(0.5)

driver.find_element_by_id('id_password_3').send_keys('1116137671dk')

sleep(0.5)

#log in automatically through Xpath
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click()

sleep(0.5)
    
#for x in range(len(handles)):
 #  driver.switch_to.window(handles[x])
  # print(driver.title)
    
driver.get('https://www.melon.com/')

sleep(0.5)

handles = driver.window_handles

if len(handles) == 2:
    driver.switch_to.window(handles[1])

login_click = driver.find_element_by_css_selector('#gnbLoginDiv > div > button').click()

sleep(0.5)

kakao_login_click = driver.find_element_by_css_selector('#conts_section > div > div > div:nth-child(1) > button').click()

sleep(0.5)

handles = driver.window_handles
size = len(handles);
print(size)

driver.get('https://www.melon.com/')

sleep(0.5)

mypage_click = driver.find_element_by_css_selector('#gnb_menu > ul.sub_gnb > li:nth-child(1) > a > span.menu_bg.menu10').click()

sleep(0.5)

driver.get('https://www.melon.com/mymusic/top/mymusictopmanysong_list.htm?memberKey=49030935')

most_often_listened_click = driver.find_element_by_css_selector('#conts > div.wrap_tab03.type09 > ul > li:nth-child(5) > a').click()

three_month_click = driver.find_element_by_css_selector('#conts > div.data_sort.type01 > div > a:nth-child(4) > span.icon').click()


# In[444]:


def crawl():

     driver.implicitly_wait(10)
     soup = BeautifulSoup(driver.page_source, 'html.parser')
    
     divs = soup.findAll('', {"class": "fc_mgray"})
     ArtistDetailLink = []
     for div in divs:
            links = div.get('href')
          #  print(links)
            if "goArtistDetail" in links:
                ArtistDetailLink.append(links)
                
     print(ArtistDetailLink[0])  
                #java = links.split('javascript:')[1]
                #print(java)
     for i in range(len(ArtistDetailLink)):     
          driver.find_element_by_css_selector("a[href*='+str(ArtistDetailLink[i])+']")).click();
                
                #for link in links:
                        
                    #print(links)
                 # ArtistDetailLink.append(links)
                
                
                
           # for link in links:
           #     print(link)
           #     if "goArtistDetail" in link:
           #         print('yay')
            #        ArtistDetailLink.append(link.text)
                    
    # for i in range(len(ArtistDetailLink)):
     #     print(ArtistDetailLink[i])
    
                    
                    
         
       
   #  divs = soup.findAll('div', {"class": "ellipsis"})
     #print(divs)
   #  for div in divs:
    #    links = div.findAll('a')
     #   print(links)'''
        #links.find_element_by_class('fc_mgray')
        #for link in links:
         #   final = link.findAll('fc_mgray')
          #  print(final)
        
     totalArtist = soup.select('#dpCount')[0].text
    
     if int(totalArtist) > 50 :
            syllable = totalArtist/50
            
     else:  
        sleep(0.5)
            
        Artist_name = soup.select('#frm > div > table > tbody > * > td:nth-child(4) > div')
        print(len(Artist_name))
        
        artistName = []
    
        for i in range(len(Artist_name)):
           #print(Artist_name[i].text)
           if ',' in Artist_name[i].text:
               NumOfArtist = len(Artist_name[i].text.split(","))
               if NumOfArtist > 3:
                  for j in range(0,3):
                       artistName.append(Artist_name[i].text.split(",")[j])
               else:
                  for k in range(NumOfArtist):
                       artistName.append(Artist_name[i].text.split(",")[k])
                    
           else:                       
               artistName.append(Artist_name[i].text)
               #artist_click = driver.find_element_by_css_selector('#frm > div > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(4)')
               #artist_click.click()
           
        
        
            #artistName > a:nth-child(1)
            #artistName > a:nth-child(2)
            #frm > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > div
            #artistName > a:nth-child(1)
            
            
            #frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div
    
     #  for a in as
      #      print(a.text)
        

#        for m in range(len(artistName)):
 #           print(artistName[m])
       # print('태연 (Tae Yeon) - 페이지 이동')
        #id = artistName[0]+(' - 페이지 이동')
        #print(id)

        
        #artist_click = driver.find_element_by_xpath('//*[@id="+str(i)+"]/a').click()
        #driver.find_element_by_css_selector("[title*='+str(artistName[0])+']").click()

        #driver.find_element_by_id('artistName')
            #artistName > a
             #'//*[@title="Havai 30"]'
                #artistName > a//*[@id="artistName"]/a
         #   sep = '아티스트 더보기'
          # artistName = Artist_name[i].split(sep, 1)[0]
          #print(artistName.text)
        #//*[@id="artistName"]/a
        #artistName > a
        #<a href="javascript:melon.link.goArtistDetail('236797');" title="태연 (TAEYEON) - 페이지 이동" class="fc_mgray">태연 (TAEYEON)</a>
        
     '''   for i in range(1,51):
            artistName = Artist_name[i].text.split(', ')
            for j in range(0,artistName.size()+1)
                id = artistName[j] + ' - 페이지 이동'
                print(id)
            
            artist_click = driver.find_element_by_id(id)
            
           # artist_click = driver.find_element_by_css_selector('#frm > div > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(4)')
            artist_click.click()

            
            sleep(0.5)
            #frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div
            #frm > div > table > tbody > tr:nth-child(2) > td:nth-child(4)
            
            datailed_info_click = driver.find_element_by_css_selector('#conts > div.wrap_tab_atist.type9 > ul > li:nth-child(2) > a > span')
            datailed_info_click.click()
            #conts > div.wrap_tab_atist > ul > li.on > a > span
            #conts > div.wrap_tab_atist > ul > li.on > a
            #conts > div.wrap_tab_atist > ul > li.on > a > span
            #conts > div.wrap_tab_atist.type9 > ul > li:nth-child(2) > a > span
            #conts > div.wrap_tab_atist.type9 > ul > li:nth-child(2) > a > span
            sleep(0.5)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            artist = soup.select('#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > p')
            features_dt = soup.select('#conts > div.section_atistinfo03 > dl > dt')
            features = soup.select('#conts > div.section_atistinfo03 > dl > dd')

            artistproc1 = artist[0].text.strip().replace("아티스트명","")
            artistproc2 = artistproc1.replace(u"\xa0", u" ")
            artarr[i, 0] = artistproc2

            j = 1
            if features_dt[0].text.strip() == "데뷔":
                if features_dt[2].text.strip() == "결성일":
                    for k in [1, 3, 4]:
                        feature = features[k].text.strip().split('\n')

                        artarr[i, j] = ''.join(feature).replace("\t", "")
                        j = j + 1
                else:
                    for k in range(1, 4):
                        feature = features[k].text.strip().split('\n')
                        artarr[i, j] = ''.join(feature).replace("\t", "")
                        j = j + 1
            elif features_dt[0].text.strip() == "활동년대":
                 for k in range(0, 3):
                    feature = features[k].text.strip().split('\n')
                    artarr[i, j] = ''.join(feature).replace("\t", "")
                    j = j + 1
            driver.back()
            driver.back()
            three_month_click = driver.find_element_by_css_selector('#conts > div.data_sort.type01 > div > a:nth-child(4) > span.icon').click()

    '''   
    


def ArtistInfoCrawlerOfUser():
    """Crawl Artists' name, year, type and genre for each most often listening songs"""
    res = requests.get(driver.current_url, headers={"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0 rv:11.0) like Gecko"})
    res.raise_for_status()
    crawl()
    print("well done")
   # driver.quit()




ArtistInfoCrawlerOfUser() 


# In[426]:


artarr = np.zeros((210, 4), dtype='>U60')


# In[ ]:


artarr


# In[ ]:





# In[ ]:




