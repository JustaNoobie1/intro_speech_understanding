import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()
    time_string = now.strftime("The time is %I:%M %p")
    gtts.gTTS(text=time_string, lang=lang).save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "Why did the bicycle fall over? Because it was two-tired."
    ]
    joke = random.choice(jokes)
    gtts.gTTS(text=joke, lang=lang).save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    now = datetime.datetime.now()
    date_string = now.strftime("Today is %A, %B %d, %Y.")
    gtts.gTTS(text=date_string, lang=lang).save(audiofile)
    return f"https://www.timeanddate.com/calendar/?year={now.year}&month={now.month}"

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        if "time" in command:
            what_time_is_it(lang, filename)
        elif "day" in command:
            what_day_is_it(lang, filename)
        elif "joke" in command:
            tell_me_a_joke(lang, filename)
        else:
            gtts.gTTS(text="Sorry, I did not understand that.", lang=lang).save(filename)
    except:
        gtts.gTTS(text="Sorry, I could not hear you.", lang=lang).save(filename)
