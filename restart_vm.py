import time
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

write_log("\n" + str(date.today()) + "\n")

vbox = virtualbox.VirtualBox()

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
    time.sleep(300)
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
    session.console.machine.save_state()
    while True:
        if session.state == virtualbox.library.SessionState.unlocked:
            print("saved",vm_name)
            write_log("saved "+vm_name)
            break
        else:
            print("saving",vm_name)
            time.sleep(1)




def restart_error_VM():
    write_log("restarting error VMs")
    error_VM = read_status_file()['error_VMs']
    write_log(str(error_VM))
    
    for vm_name in error_VM:
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
            open_and_run_script(vm_name)
            

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
