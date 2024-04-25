import random
import time
import pyautogui
import subprocess
import numpy as np
import json

def generate_random_word(): 
    global queries
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

        time_interval = random.uniform(5,9)
        time.sleep(time_interval)

def search_links(links):
    for url in links:

        print("link searched ", url)

        pyautogui.hotkey('ctrl','k')
        pyautogui.press('backspace',presses=2)
        pyautogui.typewrite(url)
        pyautogui.press("delete",presses=2)
        pyautogui.press("enter")

        time_interval = random.uniform(7,8)
        time.sleep(time_interval)

def read_status_file():
    while True:
        try:
            with open("/home/dewa/windows_shared/search_status.json", 'r') as status_file:
                file_content = json.loads(status_file.read())
            break
        except Exception as e:
            print("Error Reading status file",e)
            time.sleep(1)
    
    return file_content

def write_status_file(file_content):
    while True:
        try:
            with open("/home/dewa/windows_shared/search_status.json", 'w') as status_file:
                json.dump(file_content, status_file, indent=4)
                break
        except Exception as e:
            print("error writing status file",e)
            time.sleep(1)

with open("/home/dewa/windows_shared/queries.txt",'r') as queries:
    queries = queries.read()
    queries = queries.split("\n")

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
                json.dump(file_content, status_file, indent=4)
                break
        except Exception as e:
            print("error writing status file",e)
            time.sleep(1)


    if open_browser:
        subprocess.Popen('microsoft-edge')
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
                json.dump(file_content, status_file, indent=4)
            break
        except Exception as e:
            print("Error writing json file",e)
            time.sleep(1)
    
    time.sleep(10)
else:
    print("not matching VM")
    time.sleep(1)

