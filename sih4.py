def stt():
    x=sr.Recognizer()
    with sr.Microphone() as source:
        audio2=x.listen(source,timeout=4,phrase_time_limit=3)
    return x.recognize_google(audio2)
def smart_agriculture():
        try:
                choice="Are you a Customer or a farmer"
                farmm="welcome to farmers page"
                buy="Can i know your name"
                cust="Welcome to Customer page"
                ss1=gTTS(text=cust,lang='en', slow=False)
                ff=gTTS(text=farmm,lang='en',slow=False)
                k=gTTS(text=buy,lang='en',slow=False)
                ss1.save("ss1.mp3")
                ff.save("ss2.mp3")
                k.save("s.mp3")
                print(" Options \n1.Customer \n2.farmer")
                cc=gTTS(text=choice, lang='en', slow=False)
                cc.save("ccc.mp3")
                playsound("ccc.mp3")
                pq=sr.Recognizer()
                with sr.Microphone() as source:
                        audio1=pq.listen(source, timeout=4,phrase_time_limit=3)
                cccc=pq.recognize_google(audio1)
                print(cccc)
                if pq.recognize_google(audio1)=="customer":
                        playsound("ss1.mp3")
                        playsound("s.mp3")
                        l=sr.Recognizer()
                        with sr.Microphone() as source:
                            audio=l.listen(source, timeout=4,phrase_time_limit=3)
                        name="Hello "+l.recognize_google(audio)+" what would you like to buy"
                        nn=gTTS(text=name,lang='en',slow=False)
                        nn.save("cname.mp3")
                        playsound("cname.mp3")
                        chc=gTTS(text="you would like to buy"+stt()+"How many kg's would you like to buy",lang='en',slow=False)
                        chc.save("chc.mp3")
                        playsound("chc.mp3")
                        xyz="number of kg's="+str(stt())
                        sds=gTTS(text=xyz,lang='en',slow=False)
                        sds.save("kgs.mp3")
                        playsound("kgs.mp3")
                        dddd="your items are available would to like to go and get the orders or you want our employee to get them to you"
                        s1=gTTS(text=stt(),
                elif pq.recognize_google(audio1)=="farmer":
                        playsound("ss2.mp3")
        except:
                print("error")
smart_agriculture()

