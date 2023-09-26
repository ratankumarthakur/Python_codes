import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')               #enables us to use builtin voices in windows
voices = engine.getProperty('voices')        #there are only two voices inbuilt 0,1 o for male voice and 1 for female voice
print(voices[1].id)                          #this will print the name of inbuilt speaker ie David and Zira
engine.setProperty('voice',voices[0].id)     #choose the one you want

def speak (audio):                           #defining a function which will input text and return audio ie. sound
    engine.say(audio)                        #it is a function of pyttsx3 that takes input and say it verbally,in place 
                                             #of audio in speak function whatever we will write it will speak that
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("good morning ,,,,,,     bhai")  #this will not add pause in speech
    elif hour>=12 and hour<17:
        speak("good afternoon!")
    elif hour>=17 and hour<19:
        speak("good evening!")
    else:
        speak("good night!")

def takeCommand():                             #this function will take audio as input and give text as output of what you said
                                               #this function requires net
    r=sr.Recognizer()                          #creating the object and using it's function Recognizer
    with sr.Microphone() as source:            #choosen microphone as input device
        print("Listening...")                  
        r.pause_threshold=0.6                    #ctrl+click karo jahan pause_threshold likha hai ,you'll get to know why this statement is used
        audio=r.listen(source)                 

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:                        
        print(e)                                   #this will print the error message
        print("Can you say that again please...")
        return "None"
    return query

def sendEmail():                                   #this will send email from email id 1 to the email id 2
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email id 1', 'password of this account')   #you need to enable less secure apps for this account email id 1
    server.sendmail('email id 1',to,content)
    server.close()

if __name__=="__main__":                     #main function like in c++
    speak("My name is jarvis")             #this statement will say ratan is a good boy
    wishMe()                                 #this will wish according to the time in system
    
    while True:                              #it will go on listening and executing
        query=takeCommand().lower()          #so that there is no chance of mismatch 

        if 'wikipedia' in query:                                       #meaning is clear from the statement
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")                        #so that it will search without writing wikipedia a the end
            results=wikipedia.summary(query, sentences=2)                #only 2 sentences will get printed
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:                                  #all clear with the statement itself
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:                                    #the music should be inside a manually created folder 
            music_dir='D:\\My photos and videos\\songs'                #don't mention name of music file,also note that we have used\\
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))           #the first song in the folder will get played

        elif 'the time' in query:                                      #it will tell the time in hour,minute,second format
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
            print(strTime)

        elif 'open vscode' in query:
            codePath="C:\\Users\\RATAN KUMAR\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'send email to' in query:
            try:
                speak("what should I write")
                content=takeCommand()
                to="email id 2"
                sendEmail(to,content)
                speak ("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry unable to send email")