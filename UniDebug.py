import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
  try:
    r = requests.get(url, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return ""

def fillUnivList(ulist, html):
  soup = BeautifulSoup(html, "html.parser")
  for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
      tds = tr('td')
      ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
  print("{:^10}\t{:^6}\t{:^10}".format("ranking","name","score"))
  # for i in range(num):
  #   u = ulist[i]
  #   print("{:^10}\t{:^6}\t{:^10}".format((str(u[0]), str(u[1]), str(u[2]))))
  for list in ulist:
    #print("{:^10}\t{:^6}\t{:^10}".format((list[0], list[1], list[2])))
    print("{:^10}\t{:^6}\t{:^10}".format((list[0], list[1], list[2]))

def main():
  uinfo = []
  url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2019.html'
  html = getHTMLText(url)
  fillUnivList(uinfo, html)
  printUnivList(uinfo, 20)

if __name__ == '__main__':
    main(
