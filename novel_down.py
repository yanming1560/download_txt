import time,random,requests,multiprocessing,os
from bs4 import BeautifulSoup as bs

allhead=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
         'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
         ]

def get_menu(url):
    menu=[]
    link=[]
    aa = requests.get(url, headers={'user-agent': random.choice(allhead)})
    bb = bs(aa.content, 'lxml')
    cc=bb.find_all(class_='box_con')
    dd=cc[1].find_all('dd')
    for i in dd:
        menu.append(i.text)
        link.append(url+i.a['href'])
    return menu,link

def get_content(i,lin,name,tar):
    try:
        aa1 = requests.get(lin, headers={'user-agent': random.choice(allhead)})
        bb1 = bs(aa1.content, 'lxml')
        cc1 = bb1.find(id='content')
        with open(tar+'/'+str(i)+'.txt','a') as f:
            time.sleep(random.uniform(0.5,1))
            f.write(name+'\n')
            f.write(cc1.text.replace('\xa0',''))
            f.write( '\n')
    except:
        print('')


def multi_work(menu,link):
    tar=os.getcwd() + str(url).split('/')[-1]
    os.makedirs(tar)
    p = multiprocessing.Pool(processes=10)
    for i,lin in enumerate(link):
        p.apply_async(get_content, args=(i,lin,menu[i],tar,))
    p.close()
    p.join()


if __name__=='__main__':
    url='http://www.biquge.jp/275193_41/'
    menu,link=get_menu(url)
    time.sleep(random.uniform(0.5,1))
    multi_work(menu,link)
