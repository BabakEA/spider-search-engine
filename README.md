# spider-search-engine
python-based spider search engine

By searching for each item, the spider will provide a list including:

·       Most popular question based on google suggestion: (read and analyze the Google search API)

·       The products’ price on the eBay. (using Beautiful Soup library to extract the data from eBay website and list the items based on the price.

Input:  Any keywords

Output: An excel sheet including all top searches on Google, and top best prices on the eBay 




Objective

Customer satisfaction/feedback is fairly a new feature that can play a critical role. Collecting feedback from customers is easy and very popular.
Today when a customer walks in they have most of the information. For salesperson, the challenge of pitching one new product is now shifted to have a broad knowledge of the pros and cons of each product. 
Employees can increase their knowledge using analytical techniques to have appropriated answer for the client’s questions.  
listen, understands and provides the best suggestion based on the clients’ requirements
To address this feature, I have created a python-based search engine to help the employees.

An example:
Babak is an Employee working at the media department. He wants to know about the most common questions for the canon lens “sigma 70-200” and he wants to have a landscape of this products and the simile's ones prices

the spider will provide following results: 

Most popular question based on google suggestion:
Seller can have estimation about the clients’ questions 
The products’ price from the other companies such as eBay :
Seller will have a comprehensive knowledge about the product’s price and the other simmerers one on the market. 
Using these information's, employee can provide the most accurate consultant for the client and the customers satisfaction would be increased consequently 

How To Run:
Run the Start.bat or Start.Sh to run the Python file,

Installing the python libraries 
pip install pandas, numpy, requests , BeautifulSoup
Call the project file : 
python Start.py

Use Google search API to record the most common search :

url=http://suggestqueries.google.com/complete/search
qserach=input('Please Enter your keywords:  ')
params= {  "client": "chrome", "q" : qserach, "hl" : "en"}
r= req.get(url,params=params)
     print ("the moest resent serach for :",qserach , "are:")
      for j in (r.json()[1]):
        print (j)


Use BeautifulSoup to extract the information , from the  eBay website 

ebayurl="https://www.ebay.ca/sch/i.html?_from=R40&_sacat=0&_nkw={0:s}".format(qserach)
html= urllib.request.urlopen(ebayurl).read()
soup=b(html,"html.parser")
for post in soup.findAll("li",{"class" :"sresult lvresult clearfix li shic"}):
item=post.findAll("a", {"class" : "vip"})[0]
price=re.findall("\d+\.\d+", post.findAll("span",{"calss","bold"})[0].text)[0]
title=item.text
link=item['href']
df.loc[i]=[i,qserach,title, link,price]
df = df.sort_values(by=['price'])     

Conclusion:
All results will be recoded to the excel sheet name results.xlsx
writer = pd.ExcelWriter('Results.xlsx’)
Most common search :
df1.to_excel(writer,'Google suggestion’)
Product’s price on Eaby:
df.to_excel(writer,'ebay -prices’)
writer.save()













