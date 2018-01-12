#-*- coding:utf-8 -*-

import os, win32com.client

pastaAtual = os.listdir(os.getcwd())
i = 0

for arquivo in pastaAtual:    #para todo arquivo na pasta atual
    if arquivo.endswith(".webloc"):        #com extensão webloc
        #print(os.path.join(os.getcwd(), arquivo)) #path completo do arquivo encontrado
        
        in_file = open(arquivo, "rt")      #abre o arquivo e coloca na string contents
        contents = in_file.read()           
        in_file.close()
        
        beginIndex = contents.find("<string>") + len("<string>")    #adquire a URL
        endIndex = contents.find("</string>")
        url = contents[beginIndex:endIndex]



        #print url, "\n"     #cria o atalho para abrir no windows
        bmurl = unicode(url,"utf8")

        if i == 0:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink0.url","utf8")
        elif i == 1:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink1.url","utf8")
        elif i == 2:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink2.url","utf8")
        elif i == 3:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink3.url","utf8")
        elif i == 4:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink4.url","utf8")
        elif i == 5:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink5.url","utf8")
        elif i == 6:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink6.url","utf8")
        elif i == 7:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink7.url","utf8")
        elif i == 8:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink8.url","utf8")
        elif i == 9:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink9.url","utf8")
        elif i == 10:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink10.url","utf8")
        elif i == 11:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink11.url","utf8")
        elif i == 12:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink12.url","utf8")
        elif i == 13:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink13.url","utf8")
        elif i == 14:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink14.url","utf8")
        elif i == 15:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink15.url","utf8")
        elif i == 16:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink16.url","utf8")
        elif i == 17:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink17.url","utf8")
        elif i == 18:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink18.url","utf8")
        elif i == 19:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink19.url","utf8")
        elif i == 20:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink20.url","utf8")
        elif i == 21:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink21.url","utf8")
        elif i == 22:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink22.url","utf8")
        elif i == 23:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink23.url","utf8")
        elif i == 24:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink24.url","utf8")
        elif i == 25:
            bmpath = unicode(r"C:\Users\vhayashi\Desktop\windowsLink25.url","utf8")

        ws = win32com.client.Dispatch("wscript.shell")
        scut = ws.CreateShortcut(bmpath)
        scut.TargetPath=bmurl  
        scut.save()

        print "windowsLink"+str(i), arquivo
        i = i + 1

userinput = raw_input (" ")
