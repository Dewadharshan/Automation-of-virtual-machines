import random
import time
import pyautogui
import subprocess
import numpy as np
import json

def generate_random_word(): 
   
    queries = [
        "Weather forecast karur",
        "How to tie a tie",
        "Best pizza places near me",
        "Symptoms of rabies",
        "How to cook spaghetti carbonara",
        "Currency exchange rate int to dollars",
        "DIY home decor ideas",
        "What is the capital of indoa",
        "How to meditate for beginners",
        "Top 10 movies of [specific year]",
        "Historical events on jan first",
        "Healthy breakfast recipes",
        "How to change a tire",
        "Famous quotes by elon musk",
        "How does cryptocurrency work?",
        "How to grow tomatoes in a garden",
        "How to play guitar chords",
        "Best hiking trails in india",
        "How to create a budget spreadsheet",
        "What is the meaning of extravanza",
        "Home workout routines without equipment",
        "Quick dinner recipes for busy weeknights",
        "How to improve sleep quality",
        "Symptoms of food poisoning",
        "How to start a small business",
        "Famous landmarks in delhi",
        "How does the stock market work?",
        "How to write a resume",
        "good books",
        "How to knit a scarf for beginners",
        "What is climate change and its effects",
        "How to make a classic martini cocktail",
        "Tips for improving concentration and focus",
        "How to say hello in different languages",
        "How to build a birdhouse",
        "Best budget-friendly travel destinations",
        "How to make homemade ice cream",
        "What are the benefits of mindfulness meditation?",
        "How to start a vegetable garden",
        "Symptoms of anxiety disorders",
        "How to make a paper airplane",
        "What are the symptoms of the common cold?",
        "How to invest in real estate",
        "Best podcasts",
        "How to write a cover letter",
        "What are the signs of a heart attack?",
        "How to build a website from scratch",
        "Famous paintings by Davinci",
        "How to make sushi at home",
        "Tips for improving time management skills",
        "How to relieve stress and anxiety",
        "Best hiking boots for beginners",
        "How to start a YouTube channel",
        "What are the benefits of drinking green tea?",
        "How to fix a leaky faucet",
        "How to tie a fishing knot",
        "What are the symptoms of depression?",
        "How to make a budget travel itinerary",
        "How to do a basic car maintenance check",
        "Best educational apps for kids",
        "Weather forcast Tiruppur",
        "How to tie a tie step by step",
        "Best pizza places near me",
        "Symptons of stomache flu",
        "How to cook spagetti carbonera",
        "Currancy exchange rate for dollars to euros",
        "DIY home decoration ideas",
        "Capital of france",
        "How to meditate for beginers",
        "Top 10 movies of 2023,",
        "Historical events on Februrary 27th",
        "Healthy brekfast ideas",
        "How to change a tire on a car",
        "Famous quotes from Willian Shakespear",
        "How does crytocurrency work?",
        "How to grow tomatos in a garden",
        "How to play guitar cords",
        "Best hiking trals near Los Angeles",
        "How to create a budjet spreadsheet",
        "What is the meaning of love?",
        'panther', 'serene', 'have', 'kiwi', 'impressionism', 'idyllic', 'suspense', 'can', 'treehouse', 'graceful', 'memoir', 'love', 'were', 'flute', 'efflorescent',
                    'go', 'historical', 'lighthouse', 'jubilee', 'did', 'elegant', 'hugged', 'blossom', 'celery', 'zeppelin', 'psychoanalysis', 'marimba', 'squash', 'musical', 'expressionism',
                    'help', 'creek', 'up', 'notebook', 'azure', 'helped', 'verdant', 'trigonometry', 'postmodernism', 'behaviorism', 'dream', 'television', 'jubilant', 'breathtaking', 
                    'trombone', 'serenity', 'icecream', 'resonance', 'cosmic', 'daisy', 'luminous', 'pumpkin', 'velvet', 'rosemary', 'labyrinth', 'gave', 'please', 'infinite', 'delightful', 
                    'radiant', 'projector', 'alabaster', 'mountain', 'halcyon', 'chocolate', 'effulgent', 'blackberry', 'xenon', 'cascade', 'share', 'porcupine', 'clarinet', 'gazelle', 
                    'avocado', 'nostalgia', 'headset', 'danced', 'tintinnabulation', 'wanderlust', 'quintessence', 'yesteryear', 'serendipity', 'scanner', 'thyme', 'cared', 'atoll', 
                    'incandescent', 'cranberry', 'gleaming', 'and', 'jazz', 'give', 'might', 'lettuce', 'speaker', 'peregrinate', 'bucolic', 'microphone', 'romanticism', 'she', 'shared', 
                    'joie de vivre', 'opulent', 'whimsical', 'rainbow', 'benevolent', 'care', 'penguin', 'it', 'harmony', 'tranquil', 'melancholy', 'sweet potato', 'autobiography', 'like', 
                    'I', 'was', 'slow', 'accordion', 'lemur', 'lavender', 'but', 'mystical', 'played', 'soothing', 'an', 'enchanting', 'surreptitious', 'rhapsody', 'lime', 'thank',
                    'talisman', 'enigmatic', 'keyboard', 'will', 'enrapture', 'play', 'quasar', 'honeysuckle', 'papaya', 'yearning', 'felicity', 'suspended', 'orange', 'peace', 'laughed',
                    'xylophone', 'cherry', 'ethics', 'realism', 'cold', 'could', 'lullaby', 'gossamer', 'smartwatch', 'giraffe', 'cynosure', 'oasis', 'smile', 'vellichor', 'would',
                    'harmonious', 'harmonica', 'tranquility', 'elephant', 'tender', 'is', 'paradise', 'glacier', 'apple', 'bagpipes', 'down', 'anteater', 'western', 'dance', 'are',
                    'biography', 'they', 'fig', 'kangaroo', 'friend', 'celestial', 'bad', 'quixotic', 'utopia', 'armadillo', 'you', 'mesmerizing', 'saxophone', 'luminosity', 
                    'cantaloupe', 'mystique', 'out', 'happy', 'canyon', 'fjord', 'marigold', 'algebra', 'inspiration', 'statistics', 'crescendo', 'whisper', 'nirvana', 'went', 'high', 
                    'caterpillar', 'hot', 'sapphire', 'earbuds', 'umbrella', 'off', 'minimalism', 'thanked', 'big', 'banana', 'we', 'cave', 'kismet', 'blissful', 'eggplant', 'iris', 'am', 
                    'beet', 'fast', 'in', 'fireplace', 'sociology', 'detective', 'kaleidoscope', 'ethereal', 'small', 'rhetoric', 'resplendent', 'comedy', 'walrus', 'calculus', 'a', 'blueberry', 
                    'good', 'do', 'vortex', 'plateau', 'lemon', 'no', 'mellifluous', 'yellow', 'yes', 'kind', 'yonder', 'saw', 'journalism', 'sang', 'glimmer', 'effervescent', 'ravine', 
                    'hope', 'marvelous', 'laughter', 'tangerine', 'cabbage', 'oblivion', 'orison', 'sing', 'winsome', 'the', 'xylitol', 'uplifting', 'melodious', 'pleased', 'logic', 'zephyr', 
                    'ephemeral', 'zestful', 'laugh', 'sage', 'he', 'quiescent', 'luminescent', 'cascading', 'lustrous', 'asparagus', 'guitar', 'cauliflower', 'ambrosia', 'loved', 'charming', 
                    'mousepad', 'zucchini', 'nautical', 'mesa', 'petrichor', 'happiness', 'indigo', 'veritas', 'metaphysics', 'apricot', 'carnation', 'radish', 'pomegranate', 'ocean', 'dog', 
                    'captivating', 'on', 'ubiquitous', 'low', 'mango', 'xanadu', 'ineffable', 'daffodil', 'geometry', 'fandango', 'artichoke', 'splendor', 'joy', 'sunflower', 'zenith', 
                    'existentialism', 'nectarine', 'cheetah', 'surrealism', 'melodic', 'flamingo', 'see', 'quintessential', 'may', 'dandelion', 'grapefruit'
                    ]   
    return random.choice(queries)


def type_query(query):
    for i in query:
        pyautogui.press(i)

        random_number = np.random.normal(50, 40)
        random_number = max(0, min(100, random_number))

        time.sleep(random_number/250)



def search(n):
    for i in range(n):
        random_query = generate_random_word()

        print("searched word ", random_query)

        pyautogui.hotkey('ctrl','k')
        pyautogui.press('backspace')

        type_query(random_query)
        
        pyautogui.press("enter",presses=3)

        time_interval = random.uniform(6,7)
        time.sleep(time_interval)

def search_links(links):
    for url in links:

        print("link searched ", url)

        pyautogui.hotkey('ctrl','k')
        pyautogui.press('backspace',presses=10)

        pyautogui.typewrite(url)
        
        pyautogui.press("enter")

        time_interval = random.uniform(6,7)
        time.sleep(time_interval)

def read_status_file():
    while True:
        try:
            with open("E:\shared folder\\search_status.json", 'r') as status_file:
                file_content = json.loads(status_file.read())
            break
        except Exception as e:
            print("Error Reading status file",e)
            time.sleep(1)
    
    return file_content

def write_status_file(file_content):
    while True:
        try:
            with open("E:\shared folder\\search_status.json", 'w') as status_file:
                status_file.write(json.dumps(file_content))
                break
        except Exception as e:
            print("error writing status file",e)
            time.sleep(1)

while True:
    try:
        with open("/home/dewa/windows_shared/search_status.json", 'r') as status_file:
            file_content = json.loads(status_file.read())
        break
    except Exception as e:
        print("Error Reading status file",e)
        time.sleep(1)

with open("/home/dewa/VM_details.json") as vm_details:
    vm_details_data = json.loads(vm_details.read())
    print("guest VM",vm_details_data['VM_name'])
    print("under if")

if file_content['VM_name'] == vm_details_data['VM_name'] :
    open_browser = file_content['open_browser']
    n_search = file_content['no_of_searches']
    file_content['VM_status'] = 'running'

    while True:
        try:
            with open("/home/dewa/windows_shared/search_status.json", 'w') as status_file:
                status_file.write(json.dumps(file_content))
                break
        except Exception as e:
            print("error writing status file",e)
            time.sleep(1)


    if open_browser:
        #subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        subprocess.Popen('google-chrome')
        print("opened chrome")
        time.sleep(20)


    search(int(n_search))
    
    if len(file_content['search_links']) != 0:
        search_links(file_content['search_links'])

    if file_content['take_screenshot']:
        screenshot = pyautogui.screenshot()
        path = "/home/dewa/windows_shared/screenshots/"+file_content['VM_name']+".png"
        screenshot.save(path)

    file_content['VM_status'] = 'completed'
    file_content['VM_name'] = None

    while True:
        try:
            with open("/home/dewa/windows_shared/search_status.json", 'w') as status_file:
                status_file.write(json.dumps(file_content))
            break
        except Exception as e:
            print("Error writing json file",e)
            time.sleep(1)
    
    time.sleep(10)
else:
    print("not matching VM")
    time.sleep(1)

