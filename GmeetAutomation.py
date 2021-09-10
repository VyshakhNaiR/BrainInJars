import webbrowser
import time
import schedule
############################
from datetime import datetime
import psutil

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
##############################

#CNTheory,MATHS,IAS,Crypto,Automata,Analytical and Logical Thinking Skills,ITK,IndustrialAutoMAtion
url1 = ["https://meet.google.com/lookup/gvwmmxhuxc?authuser=0&hs=179","https://meet.google.com/lookup/befbaxkk6q?authuser=0&hs=179","https://meet.google.com/lookup/ecfmss7rit?authuser=0&hs=179","https://meet.google.com/lookup/ds5ers2jye?authuser=0&hs=179","https://meet.google.com/lookup/bq6eiddy3e?authuser=0&hs=179","https://meet.google.com/lookup/f42jlppfyy?authuser=0&hs=179","https://meet.google.com/lookup/h4wnhod6j2?authuser=0&hs=179","https://meet.google.com/lookup/ec4au5u6ua?authuser=0&hs=179"]
#CNpractical
url2 = ["https://meet.google.com/lookup/bg42dxk57r?authuser=0&hs=179"]
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('Chrome', None,webbrowser.BackgroundBrowser(chrome_path))




#webbrowser.get('Chrome').open_new_tab(url)


'''if(current_time == "10:04:00"):
    webbrowser.get('Chrome').open_new_tab("www.google.com")
if(current_time == "10:05:00"):
    webbrowser.get('Chrome').open_new_tab("www.google.com")'''


def Dayorder1():
    while True:
        timenow = datetime.now().strftime("%H:%M:%S")
        #print(datetime.now().strftime("%H:%M:%S"), end="\r")
        if(timenow == "09:00:00"):
            webbrowser.get('Chrome').open_new_tab(url1[0])
        if (timenow == "10:50:00"):
            webbrowser.get('Chrome').open_new_tab(url1[4])
        if (timenow == "15:00:00"):
            webbrowser.get('Chrome').open_new_tab(url1[1])
        time.sleep(1)

def Dayorder2():
    while True:
        timenow = datetime.now().strftime("%H:%M:%S")
        #print(datetime.now().strftime("%H:%M:%S"), end="\r")
        if(timenow == "09:00:00"):
            webbrowser.get('Chrome').open_new_tab(url1[2])
        if (timenow == "10:50:00"):
            webbrowser.get('Chrome').open_new_tab(url1[7])
        if (timenow == "13:20:00"):
            webbrowser.get('Chrome').open_new_tab(url1[3])
        if (timenow == "14:10:00"):
            webbrowser.get('Chrome').open_new_tab(url2[0])
        time.sleep(1)

def Dayorder3():
    while True:
        timenow = datetime.now().strftime("%H:%M:%S")
        #print(datetime.now().strftime("%H:%M:%S"), end="\r")
        if (timenow == "10:50:00"):
            webbrowser.get('Chrome').open_new_tab(url1[0])

        if (timenow == "11:40:00"):
            webbrowser.get('Chrome').open_new_tab(url1[6])

        if (timenow == "13:20:00"):
            webbrowser.get('Chrome').open_new_tab(url1[2])

        if (timenow == "14:10:00"):
            webbrowser.get('Chrome').open_new_tab(url1[1])

        time.sleep(1)


def Dayorder4():
    while True:
        timenow = datetime.now().strftime("%H:%M:%S")
        #print(datetime.now().strftime("%H:%M:%S"), end="\r")
        if (timenow == "09:00:00"):
            webbrowser.get('Chrome').open_new_tab(url1[3])

        if (timenow == "10:50:00"):
            webbrowser.get('Chrome').open_new_tab(url1[2])

        '''if (timenow == "11:40:00"):
            webbrowser.get('Chrome').open_new_tab(url2[5])'''

        if (timenow == "13:20:00"):
            webbrowser.get('Chrome').open_new_tab(url1[7])

        time.sleep(1)

def Dayorder5():
    while True:
        timenow = datetime.now().strftime("%H:%M:%S")
        #print(datetime.now().strftime("%H:%M:%S"), end="\r")
        if (timenow == "09:00:00"):
            webbrowser.get('Chrome').open_new_tab(url1[5])

        if (timenow == "10:50:00"):
            webbrowser.get('Chrome').open_new_tab(url1[1])

        if (timenow == "11:40:00"):
            webbrowser.get('Chrome').open_new_tab(url1[4])

        if (timenow == "13:20:00"):
            webbrowser.get('Chrome').open_new_tab(url1[0])

        time.sleep(1)


###################################################
#################CPU & MEMORY USAGE################
print(psutil.cpu_percent())

print(psutil.virtual_memory())

#print(dict(psutil.virtual_memory()._asdict()))

print(psutil.virtual_memory().percent)

print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
###################################################

print("#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#")
print("Nair is the real Owner of this automation project")
print("#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#")

print(current_time)
day_Order = int(input("Today's is Day Order: "))
if(day_Order == 1):
    Dayorder1()
elif(day_Order == 2):
    Dayorder2()
elif(day_Order == 3):
    Dayorder3()
elif(day_Order == 4):
    Dayorder4()
elif(day_Order == 5):
    Dayorder5()
else:
    print("Invalid Input!")


