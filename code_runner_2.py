import json
import time


with open("/home/dewa/VM_details.json") as vm_details:
    vm_details_data = json.loads(vm_details.read())
    print("guest VM",vm_details_data['VM_name'])

while True:
    while True:
        
        try:
            with open("/home/dewa/windows_shared/search_status.json", 'r') as status_file:
                file_content = json.loads(status_file.read())
            break
            
        except Exception as e:
            print("Error Reading status file",e)
            time.sleep(1)

    if file_content['VM_name'] == vm_details_data['VM_name'] :
        with open("/home/dewa/windows_shared/search_edge.py") as search_file:
            search_code = search_file.read()
            exec(search_code)
    else:
        print("not matching VM")
        time.sleep(2)


