import os
import pyttsx3
import webbrowser
import random

service = ""
special_service = ""
pyttsx3.speak("welcome user")
while True: #infinite loop to make the program continuous
    pyttsx3.speak("do you want windows service , or IIEC connect service , or special features , orexit")
    print("service : ",end=" ")
    service = input().lower() #service input
    if "windows" in service:
        pyttsx3.speak("you are now in windows service , please tell me what do you want")
    elif "iiec" in service:
        pyttsx3.speak("you are now in IIEC services ")
        pyttsx3.speak("i know about the mentor , if you want i can get you there ")
        pyttsx3.speak("if you want to knowmore type keywords like  , mentor , IIEC youtube , IIEC linkedin , IIEC facebook , IIEC instagram ")
    elif "special" in service:
        pyttsx3.speak("you want to play a guessing game ? , or you want to roast your friend")
        print("service : " , end=" ")
        special_service=input().lower()
    elif "exit" in service:
        print("you have successfully terminated the program")
        break
    else:
        pyttsx3.speak("dont recognize , try again")
    #IIEC sevices
    while "iiec" in service:    
        print("type here \U0001F642 : " , end = " ")
        inp = input().lower() # input the requirement from IIEC
        if "mentor" in inp:
            webbrowser.open("https://www.linkedin.com/in/vimaldaga/?originalSubdomain=in")
            pyttsx3.speak("let me show you the linked in profile of , VIMAL DAGA")
        elif "youtube" in inp:
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query=iiec")
            pyttsx3.speak("youtube opened")
        elif "linkedin" in inp:
            webbrowser.open_new_tab("https://www.linkedin.com/company/iiec-rise/")
            pyttsx3.speak("linkedin profile opened")
        elif "facebook" in inp:
            webbrowser.open("https://www.facebook.com/IIECconnect/")
            pyttsx3.speak("welcome to the iiec connect facebook page ..")
        elif "instagram" in inp:
            webbrowser.open("https://www.instagram.com/iiec_connect/?hl=en")
            pyttsx3.speak("i am showing you the instagram page on web browser.. take a look")
        elif "no" in inp or "exit" in inp or "quit" in inp:
            pyttsx3.speak("you are out of IIEC service")
            break
        pyttsx3.speak("want anything else ?")
    #WINDOWS services
    while "windows" in service:     
        print("type here \U0001F642 : ", end =" ")
        inp = input().lower() # input the programs you want to run
        if ("run" in inp or "open" in inp or "execute" in inp) and  ("donot" not in inp and "dont" not in inp and "not" not in inp):
            if "chrome" in inp:
                os.system("chrome")
                pyttsx3.speak("chrome closed")
            elif ("notepad" in inp )or "editor" in inp:
                os.system("notepad")
                pyttsx3.speak("notepad closed")
            elif "visual studio code" in inp or "vscode" in inp or "code" in inp:
                os.system("Code")
                pyttsx3.speak("code")
            elif "vlc" in inp:
                os.system("vlc")
                pyttsx3.speak("vlc opened")
            elif "unity" in inp:
                os.system("Unity")
                pyttsx3.speak("unity opened")
            elif "virtual" in inp or "virtualbox" in inp or "oraclevm" in inp:
                os.system("VirtualBox")
                pyttsx3.speak("virtual box closed")
            elif "discord" in inp:
                os.system("discord")
                pyttsx3.speak("discord")
            elif "steam" in inp:
                os.system("steam opened")
                pyttsx3.speak("steam")
            elif "android studio" in inp:
                os.system("studio64")
                pyttsx3.speak("studeio64")
            elif "you tube" in inp or "youtube" in inp:
                webbrowser.open_new_tab("https://www.youtube.com/")
                pyttsx3.speak("youtube opened")
            else:
                print("try again")
        if "donot" in inp or "do not" in inp or"dont" in inp:
            print("ok program not opened")
        if "exit" in inp or "quit" in inp or "no" in inp:
            pyttsx3.speak("bye bye , you are out of windows service")
            break
        pyttsx3.speak("want to search again ?")
    #GUESSING GAME
    flag = True
    while flag and ("game" in special_service or "guessing" in special_service):       
        n=random.randint(1,100) # randomizing the number
        count = fail = 0 # for checking and feedback purpose
        pyttsx3.speak("please guess a number between 1 and 100 , or type 0 , if you want to leave")
        while True:
            print("guess : ",end=" ")
            guess_num=int(input()) # input the guess number
            if guess_num ==0:
                flag = False
                if count ==  1:
                    pyttsx3.speak("go now , but, you can not guess it next time ")
                else:
                    pyttsx3.speak("come again")
                break
            if  guess_num == n:
                pyttsx3.speak("well that was easy , anybody would have done that")
                count = 1 #to change the feedback voice based on count
            elif fail >= 4: #after 5 inputs the program itself gives the answer
                pyttsx3.speak(f"just leave , you are a noob , the number is {n}")
                break
            else:
                fail += 1 #counting number of wrong inputs
                if guess_num > n:
                    pyttsx3.speak("uhh ohhh!! , the number is too high , try again")
                else:
                    pyttsx3.speak("uhh ohhh!! , the number is too low , try again")
    # Roasting
    while"roast" in special_service:
        n=random.randint(1,11)
        pyttsx3.speak("whom do you want to roast , type the name , or type exit to leave , ")
        print("name : " , end = " ")
        roast = input()
        if "exit" not in roast:
            pyttsx3.speak(f"ok i have to roast {roast} , let me think , !!")
            if n == 1:
                pyttsx3.speak("someday you will go far.. , and I hope you , stay there , ")
            elif n == 2:
                pyttsx3.speak("I’m betting your keyboard is filthy, now from all that Cheeto-dust finger typing, you goddamn weaboo shut in. , ")
            elif n == 3:
                pyttsx3.speak("mirror can't talk , lucky for you they can't laugh either , ")
            elif n == 4:
                pyttsx3.speak("you are the reason , the gene pool needs a lifeguard , ")
            elif n == 5:
                pyttsx3.speak("If I had a face like yours , I would sue my parents , ")
            elif n == 6:
                pyttsx3.speak("you must have born on a highway ,cause that's where most accidents happen , ")
            elif n == 7:
                pyttsx3.speak("If laughter is the best medicine , I bet your face is the only cure , ")
            elif n == 8:
                pyttsx3.speak("I am glad to see , you are not letting your education get in the way of your, ignorance , ")
            elif n == 9:
                pyttsx3.speak("So a thought crossed your mind ? , must have been a long and lonely journey , ")
            elif n == 10:
                pyttsx3.speak("If I wanted to kill myself , I would climb your ego , and jump to your IQ , ")
        elif "exit" in roast:
            pyttsx3.speak("I knew , you could not take it , bye ,  ")
            break
    pyttsx3.speak(" now you are in main menu") # in main menu and main loop continious
