import datetime
import speak
import webbrowser
import os
import weather
import pyjokes
import news
import wikipedia
import random

# To create database run this command
# Don't run this command twice if database has been created once

'''import pymysql as ms
myobj = ms.connect(host = "localhost", user = "root", password="")
cursorobj = myobj.cursor()

try:
    db="create database Project1"
    cursorobj.execute(db)
    print("Database created")
except:
    print("Database error...")'''

# Comment above code till here

# To create table run this command, don,t run this again

'''import pymysql as ms
myobj = ms.connect(host = "localhost", user = "root", password="",database="Project1")
mysqlc = myobj.cursor()

# create table

ct = "create table Data(ME varchar(255),BOT varchar(255))"
mysqlc.execute(ct)  # Here, ME and BOT are fields names'''

# Delete table

# mysqlc.execute("DROP TABLE data")
# myobj.commit()

# Delete column

# mysqlc.execute("ALTER TABLE data DROP COLUMN BOT")
# myobj.commit()

def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
        speak.speak("My name is Virtual AI Assistant")  
        return "My name is Virtual AI Assistant"

    
    elif '1' in data_btn:
        speak.speak("The Clever Crow: On a hot day, a thirsty crow found a pot with little water. It dropped pebbles into the pot until the water rose high enough to drink. The crow's cleverness saved it from thirst.")
        return "The Clever Crow: On a hot day, a thirsty crow found a pot with little water. It dropped pebbles into the pot until the water rose high enough to drink. The crow's cleverness saved it from thirst."
    elif '2' in data_btn:
        speak.speak("The Honest Woodcutter: A woodcutter lost his axe in a river. When a fairy offered gold and silver axes, he refused, claiming they weren't his. Impressed by his honesty, the fairy gifted him all three axes.")
        return "The Honest Woodcutter: A woodcutter lost his axe in a river. When a fairy offered gold and silver axes, he refused, claiming they weren't his. Impressed by his honesty, the fairy gifted him all three axes."
    elif '3' in data_btn:
        speak.speak("The Lion and the Mouse: A lion spared a mouse's life. Later, when the lion was trapped in a net, the mouse gnawed through the ropes and set the lion free, proving even small creatures can help.")
        return "The Lion and the Mouse: A lion spared a mouse's life. Later, when the lion was trapped in a net, the mouse gnawed through the ropes and set the lion free, proving even small creatures can help."
    elif '4' in data_btn:
        speak.speak("The Fox and the Grapes: A hungry fox tried to reach grapes hanging high on a vine. After many attempts, it gave up, saying the grapes were probably sour, showing how we often belittle what we cannot achieve.")
        return "The Fox and the Grapes: A hungry fox tried to reach grapes hanging high on a vine. After many attempts, it gave up, saying the grapes were probably sour, showing how we often belittle what we cannot achieve."
    elif '5' in data_btn:
        speak.speak("The Hare and the Tortoise: The hare mocked the slow tortoise for a race. The hare napped, thinking he would easily win, but the steady tortoise won the race, teaching that slow and steady wins the race.")
        return "The Hare and the Tortoise: The hare mocked the slow tortoise for a race. The hare napped, thinking he would easily win, but the steady tortoise won the race, teaching that slow and steady wins the race."
    elif '6' in data_btn:
        speak.speak("The Ant and the Grasshopper: The hardworking ant stored food for winter while the lazy grasshopper sang. When winter came, the grasshopper begged for food, but the ant reminded it of the importance of hard work and preparation.")
        return "The Ant and the Grasshopper: The hardworking ant stored food for winter while the lazy grasshopper sang. When winter came, the grasshopper begged for food, but the ant reminded it of the importance of hard work and preparation."
    elif '7' in data_btn:
        speak.speak("The Thirsty Ant: An ant fell into the water and was struggling. A dove dropped a leaf to save it. Later, when a hunter aimed at the dove, the ant bit him, saving the dove's life, highlighting the value of kindness.")
        return "The Thirsty Ant: An ant fell into the water and was struggling. A dove dropped a leaf to save it. Later, when a hunter aimed at the dove, the ant bit him, saving the dove's life, highlighting the value of kindness."
    elif '8' in data_btn:
        speak.speak("The Greedy Dog: A dog with a bone saw its reflection in the water. Thinking it was another dog with a bigger bone, it barked and dropped its own bone into the water, losing it all due to greed.")
        return "The Greedy Dog: A dog with a bone saw its reflection in the water. Thinking it was another dog with a bigger bone, it barked and dropped its own bone into the water, losing it all due to greed."
    elif '9' in data_btn:
        speak.speak("The Golden Egg: A farmer had a goose that laid a golden egg daily. Greedy for more, he killed the goose to get all the gold at once, but found nothing, losing his source of wealth.")
        return "The Golden Egg: A farmer had a goose that laid a golden egg daily. Greedy for more, he killed the goose to get all the gold at once, but found nothing, losing his source of wealth."
    elif '10' in data_btn:
        speak.speak("The Boy Who Cried Wolf: A shepherd boy falsely shouted about a wolf to fool villagers. When a wolf actually came, no one believed him, and the wolf ate his sheep, showing the consequences of lying.")
        return "The Boy Who Cried Wolf: A shepherd boy falsely shouted about a wolf to fool villagers. When a wolf actually came, no one believed him, and the wolf ate his sheep, showing the consequences of lying."    

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn or "hi" in data_btn : 
        speak.speak("Hey sir, How can I help you ?")  
        return "Hey sir, How can I help you ?" 

    elif "how are you" in data_btn or "how r you" in data_btn:
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   
    
    elif "what can you do" in data_btn :
            speak.speak("I can answer questions, give you weather information, play songs, search for news, tell jokes, stories, date, time, open google, chat G P T, youtube")
            return "I can answer questions, give you weather information, play songs, search for news, tell jokes, stories, date, time, open google, chatGPT, youtube" 

    elif "thanks" in data_btn or "thank" in data_btn or "thankyou" in data_btn:
           speak.speak("It's my pleasure sir to stay with you")
           return "It's my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, I think you might need some help")
           return "Good morning sir, I think you might need some help"   

    elif "time now" in data_btn or "time" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour) + " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "date" in data_btn or "today date" in data_btn:
        today_date = datetime.datetime.now().strftime("%d %B, %Y")
        speak.speak(f"Today's date is {today_date}")
        return f"Today's date is {today_date}"


    elif "shutdown" in data_btn or "quit" in data_btn or "exit" in data_btn or "bye" in data_btn:
            speak.speak("Ok sir")
            return "Ok sir"  

    elif "play music" in data_btn or "song" in data_btn or "music" in data_btn or "play song" in data_btn:
        webbrowser.open("https://jiosaavn.com/")   
        speak.speak("jiosaavn.com is now ready for you, enjoy your music")                   
        return "jiosaavn.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"
    
    elif 'open chatgpt' in data_btn or 'chatgpt'  in data_btn or 'gpt'  in data_btn:
        url = 'https://chatgpt.com/?oai-dm=1'
        webbrowser.get().open(url)
        speak.speak("chatGPT open")  
        return "chatGPT open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    

    elif 'weather' in data_btn:
        city = 'Kanpur'
        weather_info = weather.get_weather(city)
        speak.speak(weather_info)
        return weather_info
    
    elif 'tell me a joke' in data_btn or 'joke' in data_btn or 'tell a joke' in data_btn:
        joke = pyjokes.get_joke()
        speak.speak(joke)
        return joke

    elif "news" in data_btn or "headlines" in data_btn:
        news_info = news.get_news()
        speak.speak(news_info)
        return news_info

    elif 'search' in data_btn:
        query = data_btn.replace('search', '').strip()
        result = wikipedia.summary(query, sentences=2)
        speak.speak(result)
        return result
    
    elif 'story' in data_btn:
        speak.speak("Please write any number from 1 to 10")
        return "Please write any number from 1 to 10"
    
    else :
        speak.speak( "i'm not able to understand! Do you want to open google or chat G P T ?")
        return "i'm not able to understand! Do you want to open google or chatGPT ?"       