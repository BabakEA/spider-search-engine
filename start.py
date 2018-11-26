import pandas as pd
import numpy as np
import sys
import re
import requests as req
import bs4
import urllib
from urllib import request
from bs4 import BeautifulSoup as b

df=pd.DataFrame(columns=['id','item','title','link','price'])
df1=pd.DataFrame(columns=['id','item','suggestions'])
url="http://suggestqueries.google.com/complete/search"
i=k=0
qserach= "emami.babak@gmail.com"
while qserach != 'eof':
  qserach=input('Please Enter your keywords:  ')
  if len(qserach)>1 :
      params= {
        "client": "chrome",
        "q" : qserach,
        "hl" : "en"}
      r= req.get(url,params=params)

      
      print ("the moest resent serach for :",qserach , "are:")
      for j in (r.json()[1]):
        print (j)
        k +=1
        
        df1.loc[k]=[k,qserach,j] 

      qserach=qserach.replace(" ","-")
      
      print ("*****************ebay search ***********************")
      ebayurl="https://www.ebay.ca/sch/i.html?_from=R40&_sacat=0&_nkw={0:s}".format(qserach)
      html= urllib.request.urlopen(ebayurl).read()
      soup=b(html,"html.parser")
      for post in soup.findAll("li",{"class" :"sresult lvresult clearfix li shic"}):
        i += 1
        item=post.findAll("a", {"class" : "vip"})[0]
        price=re.findall("\d+\.\d+", post.findAll("span",{"calss","bold"})[0].text)[0]
        title=item.text
        link=item['href']
        df.loc[i]=[i,qserach,title, link,price]
      df = df.sort_values(by=['price'])      
      print (df[['item','price']])
      writer = pd.ExcelWriter('Results1.xlsx')
      df1.to_excel(writer,'Google suggestion')
      df.to_excel(writer,'ebay -prices')
      writer.save()
      

