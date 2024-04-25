import time
import os
import shutil
import pyautogui
import subprocess
import json
import virtualbox
from datetime import date

with open("E:\shared folder\\VM_list.json", 'r') as vm_list:
    vm_list = json.loads(vm_list.read())

    vm_list_30 = vm_list['normal_30']
    vm_list_90 = vm_list['normal_90']
    vm_list_30_cooldown = vm_list['cooldown_30']
    vm_list_90_cooldown = vm_list['cooldown_90']

    vm_error_30 = []
    vm_error_60 = []

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
                json.dump(file_content, status_file, indent=4)
                break
        except Exception as e:
            print("error writing status file",e)
            time.sleep(1)
def write_log(data):
    with open(r"E:\shared folder\\log_data.txt",'a') as log_data:
        log_data.write(data+"\n")

def add_completed_VM(vm_name):
    status = read_status_file()
    status['completed_VMs'].append(vm_name)
    write_status_file(status)
def add_cooldown_iteration(count = 1):
    status = read_status_file()
    status['cooldown_iteration']  = status['cooldown_iteration'] + count
    write_status_file(status)

write_log("\n" + str(date.today()) + "\n")





status = read_status_file()
if status['date'] == str(date.today()):
    completed_VM = status['completed_VMs']
    completed_cooldown_iteration = status['cooldown_iteration']
else:
    completed_VM = []
    completed_cooldown_iteration = 0
    status['date'] = str(date.today())
    status['completed_VMs'] = []
    status['cooldown_iteration'] = 0
    write_status_file(status)
    
    screenshots = "E:\shared folder\screenshots"
    old_screenshots_path = "E:\shared folder\screenshots\previous day"
    old_screenshots = os.listdir(old_screenshots_path)
    for file_name in old_screenshots:
        file_path = os.path.join(old_screenshots_path, file_name)
        os.remove(file_path)
        print(f"Deleted '{file_name}'")
    

    files = os.listdir(screenshots)
    for file_name in files:
        if file_name != "previous day":
            source_path = os.path.join(screenshots, file_name)
            destination_path = os.path.join(old_screenshots_path, file_name)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file_name}' to '{old_screenshots_path}'")

vbox = virtualbox.VirtualBox()


# -----------------------------30 points------------------------------------
for iteration in range(1):
    for vm_name in vm_list_30:
        status = read_status_file()
        if (vm_name not in status['error_VMs']) and (vm_name not in completed_VM):
        

            print(vm_name)

            status = read_status_file()
            status['VM_status'] = None
            status['VM_name'] = vm_name
            status['no_of_searches'] = 12
            write_status_file(status)

            session = virtualbox.Session()

            running_VM = vbox.find_machine(vm_name)
            running_VM = running_VM.launch_vm_process(session, "gui", [])

            print("Starting",vm_name)
            while running_VM.percent < 100:
                print(running_VM.percent)
                time.sleep(1)
            print("Started",vm_name)

            continue_search = True
            for temp_counter in range(10):
                time.sleep(1)
                status = read_status_file()
                if status['VM_status'] == 'running':
                    break
                if temp_counter == 9:
                    write_log("Error running "+vm_name)
                    status['error_VMs'].append(vm_name)
                    write_status_file(status)
                    continue_search = False
            
            if continue_search:
                search_start_time = time.time()
                for file_status_counter in range(status['no_of_searches']*2):
                    status = read_status_file()
                    if status['VM_status'] == 'completed':
                        write_log("completed normal 30 "+vm_name + " time taken " + str(int(time.time() - search_start_time)))
                        add_completed_VM(vm_name)
                        break
                    time.sleep(10)

            status = read_status_file()
            status['VM_status'] = None
            status['VM_name'] = None
            write_status_file(status)

            session.console.machine.save_state()
            while True:
                if session.state == virtualbox.library.SessionState.unlocked:
                    print("saved",vm_name)
                    break
                else:
                    print("saving",vm_name)
                    time.sleep(1)
        
#------------------------------90 points---------------------------------
for iteration in range(1):
    for vm_name in vm_list_90:
        time.sleep(1)
        status = read_status_file()
        if (vm_name not in status['error_VMs']) and (vm_name not in completed_VM):
        
            print(vm_name)

            status = read_status_file()
            status['VM_status'] = None
            status['VM_name'] = vm_name
            status['no_of_searches'] = 35
            write_status_file(status)

            session = virtualbox.Session()

            running_VM = vbox.find_machine(vm_name)
            running_VM = running_VM.launch_vm_process(session, "gui", [])

            print("Starting",vm_name)
            while running_VM.percent < 100:
                print(running_VM.percent)
                time.sleep(1)
            print("Started",vm_name)

            continue_search = True
            for temp_counter in range(10):
                time.sleep(1)
                status = read_status_file()
                if status['VM_status'] == 'running':
                    break
                if temp_counter == 9:
                    write_log("Error running "+vm_name)
                    status['error_VMs'].append(vm_name)
                    write_status_file(status)
                    continue_search = False
            
            if continue_search:
                search_start_time = time.time()
                for file_status_counter in range(status['no_of_searches']*3):
                    status = read_status_file()
                    if status['VM_status'] == 'completed':
                        write_log("completed normal 90 "+vm_name + " time taken " + str(int(time.time() - search_start_time)))
                        add_completed_VM(vm_name)
                        break
                    time.sleep(10)

            status = read_status_file()
            status['VM_status'] = None
            status['VM_name'] = None
            write_status_file(status)

            session.console.machine.save_state()
            while True:
                if session.state == virtualbox.library.SessionState.unlocked:
                    print("saved",vm_name)
                    break
                else:
                    print("saving",vm_name)
                    time.sleep(1)


#---------------------------cooldowm------------------------------

for iteration in range(completed_cooldown_iteration,9):
    iteration_start_time = time.time()
    for vm_name in vm_list_90_cooldown:
        time.sleep(1)
        status = read_status_file()
        if (vm_name not in status['error_VMs']) and (vm_name not in completed_VM):
        

            print("Cooldowm search 90",vm_name)

            status = read_status_file()
            status['VM_status'] = None
            status['VM_name'] = vm_name
            status['no_of_searches'] = 4
            write_status_file(status)

            session = virtualbox.Session()

            running_VM = vbox.find_machine(vm_name)
            running_VM = running_VM.launch_vm_process(session, "gui", [])

            print("Starting",vm_name)
            while running_VM.percent < 100:
                print(running_VM.percent)
                time.sleep(1)
            print("Started",vm_name)

            continue_search = True
            for temp_counter in range(10):
                time.sleep(1)
                status = read_status_file()
                if status['VM_status'] == 'running':
                    break
                if temp_counter == 9:
                    write_log("Error running "+vm_name)
                    status['error_VMs'].append(vm_name)
                    write_status_file(status)
                    continue_search = False
            
            if continue_search:
                search_start_time = time.time()
                for file_status_counter in range(status['no_of_searches']*3):
                    status = read_status_file()
                    if status['VM_status'] == 'completed':
                        write_log("cooldowm 90 iteration "+str(iteration)+" "+vm_name + " time taken " + str(int(time.time() - search_start_time)))
                        print("cooldowm 90 iteration "+str(iteration)+" "+vm_name)
                        break
                    if file_status_counter+1 == status['no_of_searches']*3:
                        write_log("------ERROR------ cooldowm 90 iteration "+str(iteration)+" "+vm_name)

                    time.sleep(10)

            status = read_status_file()
            status['VM_status'] = None
            status['VM_name'] = None
            write_status_file(status)

            session.console.machine.save_state()
            while True:
                if session.state == virtualbox.library.SessionState.unlocked:
                    print("saved",vm_name)
                    break
                else:
                    print("saving",vm_name)
                    time.sleep(1)
        if iteration <= 3:
            for vm_name in vm_list_30_cooldown:
        
                print("Cooldowm search 30",vm_name)

                status = read_status_file()
                status['VM_status'] = None
                status['VM_name'] = vm_name
                status['no_of_searches'] = 4
                write_status_file(status)

                session = virtualbox.Session()

                running_VM = vbox.find_machine(vm_name)
                running_VM = running_VM.launch_vm_process(session, "gui", [])

                print("Starting",vm_name)
                while running_VM.percent < 100:
                    print(running_VM.percent)
                    time.sleep(1)
                print("Started",vm_name)

                continue_search = True
                for temp_counter in range(10):
                    time.sleep(1)
                    status = read_status_file()
                    if status['VM_status'] == 'running':
                        break
                    if temp_counter == 9:
                        write_log("Error running "+vm_name)
                        status['error_VMs'].append(vm_name)
                        write_status_file(status)
                        continue_search = False
            
                if continue_search:
                    search_start_time = time.time()
                    for file_status_counter in range(status['no_of_searches']*3):
                        status = read_status_file()
                        if status['VM_status'] == 'completed':
                            print("cooldowm 30 iteration "+str(iteration)+" "+vm_name)
                            break
                        if file_status_counter+1 == status['no_of_searches']*3:
                            write_log("cooldowm 30 iteration "+str(iteration)+" "+vm_name + " time taken " + str(int(time.time() - search_start_time)))
                        time.sleep(10)

                status = read_status_file()
                status['VM_status'] = None
                status['VM_name'] = None
                write_status_file(status)

                session.console.machine.save_state()
                while True:
                    if session.state == virtualbox.library.SessionState.unlocked:
                        print("saved",vm_name)
                        break
                    else:
                        print("saving",vm_name)
                        time.sleep(1)

    write_log("completed cooldown iteration "+str(iteration))
    add_cooldown_iteration(1)
    if time.time() - iteration_start_time <= 1100:
        wait_time = 1100 - (time.time() - iteration_start_time)
        time.sleep(wait_time)
    


def open_and_run_script(vm_name):
    session = virtualbox.Session()
    running_VM = vbox.find_machine(vm_name)
    running_VM = running_VM.launch_vm_process(session, "gui", [])
    print("Starting",vm_name)
    while running_VM.percent < 100:
        print(running_VM.percent)
        time.sleep(1)
    print("Started",vm_name)
    write_log("Started "+vm_name)
    time.sleep(400)
    session.console.keyboard.put_keys(hold_keys=['CTRL','ALT'],press_keys=['t'])
    time.sleep(7)
    session.console.keyboard.put_keys("python3 /home/dewa/windows_shared/code_runner_2.py")
    session.console.keyboard.put_keys(press_keys = "\n")
    time.sleep(1)
    session.console.keyboard.put_keys(hold_keys=['CTRL','ALT'],press_keys=['t'])
    time.sleep(5)
    session.console.keyboard.put_keys("microsoft-edge")
    session.console.keyboard.put_keys(["ENTER"])

    time.sleep(60)
    write_log("opened edge and ran script")
    status = read_status_file()
    status['VM_status'] = None
    status['VM_name'] = vm_name
    status['no_of_searches'] = 5
    write_status_file(status)

    for temp_counter in range(10):
        time.sleep(1)
        status = read_status_file()
        if status['VM_status'] == 'running':
            break
        if temp_counter == 9:
            write_log("Error restarting "+vm_name)
            session.console.power_down()
            write_log("powered down "+vm_name)
            time.sleep(5)
            status = read_status_file()
            status['VM_name'] = None
            status['VM_status'] = None
            write_status_file(status)
            return False



    search_start_time = time.time()
    for file_status_counter in range(status['no_of_searches']*2):
        status = read_status_file()
        if status['VM_status'] == 'completed':
            write_log("completed restart test "+vm_name + " time taken " + str(int(time.time() - search_start_time)))
            break
        time.sleep(10)
    status = read_status_file()
    status['VM_name'] = None
    status['VM_status'] = None
    write_status_file(status)


    session.console.machine.save_state()
    while True:
        if session.state == virtualbox.library.SessionState.unlocked:
            print("saved",vm_name)
            write_log("saved "+vm_name)
            break
        else:
            print("saving",vm_name)
            time.sleep(1)
    return True




def restart_error_VM():
    write_log("restarting error VMs")
    error_VM = read_status_file()['error_VMs']
    write_log(str(error_VM))
    
    for vm_name in error_VM:
        time.sleep(1)
        status = read_status_file()
        status['VM_name'] = vm_name
        status['VM_status'] = None
        status['no_of_searches'] = 1
        write_status_file(status)

        session = virtualbox.Session()
        running_VM = vbox.find_machine(vm_name)
        running_VM = running_VM.launch_vm_process(session, "gui", [])

        print("Starting",vm_name)
        while running_VM.percent < 100:
            print(running_VM.percent)
            time.sleep(1)
        print("Started",vm_name)

        write_log("verifying Error "+vm_name)
        error_status = True
        for temp_counter in range(10):
            time.sleep(1)
            status = read_status_file()
            if status['VM_status'] == 'running':
                error_status = False
                for file_status_counter in range(status['no_of_searches']*3):
                    status = read_status_file()
                    if status['VM_status'] == 'completed':
                        write_log("search completed")
                        break
                    time.sleep(10)
                break
            if temp_counter == 9:
                write_log("Error running "+vm_name)
        status = read_status_file()
        status['VM_name'] = None
        status['VM_status'] = None
        write_status_file(status)

        if error_status:
            session.console.power_down()
            write_log("powered down "+vm_name)
            time.sleep(5)
            for i in range(4):
                restart_status = open_and_run_script(vm_name)
                if restart_status:
                    break
        else:
            write_log("NO ERROR IN "+vm_name)
            session.console.machine.save_state()
            while True:
                if session.state == virtualbox.library.SessionState.unlocked:
                    print("saved",vm_name)
                    write_log("saved "+vm_name)
                    break
                else:
                    print("saving",vm_name)
                    time.sleep(1)

        status = read_status_file()
        status['error_VMs'].remove(vm_name)
        write_status_file(status)
    
        
restart_error_VM()
