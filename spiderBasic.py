import urllib
import re
import socket
import urlparse

def add(num):
    num+=1
    return num

def spiderWeb(url,count):
    if table.has_key(url):
        pass
    else:
        count=add(count)
        table[url]=count
        htmlFile=open((str(count)+'.txt'),'w')
        htmlFile.write(urllib.urlopen(url).read())
        htmlFile.close()
        
        pattern='href="[^(javascript)]\S*[^(#)(css)(js)]\"'
        saveTxt=open('save.txt','w')
        htmlFile=open((str(count)+'.txt'),'r')
        for line in htmlFile:
            ma=re.search(pattern,line)
            #print line
            if ma is not None :
                srcTail=line[ma.start():ma.end()].split('"')[1]            
                src=urlparse.urljoin(url,srcTail)
                saveTxt.write(src)
                #print src
                saveTxt.write('\n')
        htmlFile.close()
        saveTxt.close()
        
        saveTxt=open('save.txt','r')
        for line in saveTxt:
            url=line.strip('\n')
            if table.has_key(url):
                print url+'已爬取，跳过'
            else:
                print url+'》》》》》'
                count=add(count)
                table[url]=count
                htmlFile=open((str(table[url])+'.txt'),'w')
                print str(table[url])+'文件写入中'
                try:
                    htmlFile.write(urllib.urlopen(url).read())
                except:
                    pass
                finally:
                    htmlFile.close()
        saveTxt.close()

    urlMapFile=open('map.txt','w')
    for key in table.keys():
        urlMapFile.write(str(key)+'\t'+str(table[key])+'\n')
    urlMapFile.close()
    
    print '一次爬取结束'


if __name__=='__main__':
    socket.setdefaulttimeout(10)

    entrance='http://www.zju.edu.cn/'
    count=0
    table={}
    spiderWeb(entrance,count)
    



