# Library
import requests
import json
import urllib3
import pandas as pd
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def user_operation():
    print("==================== Welcome to Notification_setting fetch script ====================\n\
======================================================================================\n\
๐ Please select your platform by Typing number of platform for fetch data")
    print("\t{: <15} {: <18} {: <20} {: <15}".format('1.Intel_dom4', '2.HPE_dom1,2', '3.HPE_dom3_synergy', '4.HPE_dom3_simplivity'))
    print("\t{: <15} {: <18} {: <20} {: <15}".format('5.Flexpod_dom1', '6.Flexpod_dom2', '7.Flexpod_dom3', '8.Flexpod_Kerry'))
    print("\t{: <15} {: <18} {: <20}".format('9.Dell_dom2', '10.Dell_dom3_PRD', '11.Dell_dom3_POC'))
    print("======================================================================================")
    input_platform = input("{:<54} : ".format("\u25ba Please type number of platform (Example : 1/2/3)"))

    while True:
        input_confirm_connect_vpn = input("\u25ba Please connect each platform SSL VPN (Type : yes/no) : ")
        if input_confirm_connect_vpn == "yes":
            print("======================================================================================")
            break
    print("")
    return input_platform, input_confirm_connect_vpn

def convert_platform_number_to_platform_name(input_platform):
    platform_list = ['Intel_dom4', 'HPE_dom1,2', 'HPE_dom3_synergy', 'HPE_dom3_simplivity',
    'Flexpod_dom1', 'Flexpod_dom2', 'Flexpod_dom3', 'Flexpod_Kerry', 'Dell_dom2', 
    'Dell_dom3_PRD', 'Dell_dom3_POC']

    each_paltform_number = input_platform.split("/")
    platform_name_list = []
    for each_number in each_paltform_number:
        platform_name_list.append(platform_list[int(each_number) - 1])
    
    return platform_name_list

def get_token(platform):
    # try:
    print("==========================================")
    print("๐ Platform : ", platform)
    print("------------------------------------------")
    if "Intel" in platform:
        if platform == 'Intel_dom4':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
    elif "HPE" in platform:
        if platform == 'HPE_dom1,2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'HPE_dom3_synergy':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'HPE_dom3_simplivity':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
    elif "Flexpod" in platform:    
        if platform == 'Flexpod_dom1':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'Flexpod_dom2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'Flexpod_dom3':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'Flexpod_Kerry':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
    elif "Dell" in platform:
        if platform == 'Dell_dom2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'Dell_dom3_PRD':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        elif platform == 'Dell_dom3_POC':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/auth/token/acquire'
            body = {"username": "xxxxx", "password": "xxxxxxxxx", "authSource": "xxxxxx"}
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

    x = requests.post(url=fetch_data_from_vm_url, headers=headers, json=body, verify=False, timeout=20)

    platform_token_to_json = json.loads(x.text)
    # print(platform_token_to_json)
    platform_token = "vRealizeOpsToken " + platform_token_to_json["token"]

    print("{:<35} : OK".format("1.get_token "))
    return platform_token

# Query metric datas form selected metrics
def get_notification_setting_data(token, platform):
    if "Intel" in platform:
        if platform == 'Intel_dom4':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    if "HPE" in platform:
        if platform == 'HPE_dom1,2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'HPE_dom3_synergy':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'HPE_dom3_simplivity':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    elif "Flexpod" in platform:
        if platform == 'Flexpod_dom1':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Flexpod_dom2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Flexpod_dom3':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Flexpod_Kerry':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    elif "Dell" in platform:
        if platform == 'Dell_dom2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Dell_dom3_PRD':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Dell_dom3_POC':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/notifications/rules?page=0&amp;pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

    x = requests.get(url=fetch_data_from_vm_url, headers=headers, verify=False)
    notification_setting_data = json.loads(x.text)

    array_notification_setting_data_rulename = []
    array_notification_setting_data_vmuuid = []

    if platform != "Flexpod_dom2":
        for i in range (len(notification_setting_data["rules"])):
            array_notification_setting_data_rulename.append(notification_setting_data["rules"][i]["name"])
            try:
                array_notification_setting_data_vmuuid.append(notification_setting_data["rules"][i]["resourceFilter"]['resourceId'])
            except:
                array_notification_setting_data_vmuuid.append("-")
    else:
        for i in range (len(notification_setting_data["notification-rule"])):
            array_notification_setting_data_rulename.append(notification_setting_data["notification-rule"][i]["name"])
            try:
                array_notification_setting_data_vmuuid.append(notification_setting_data["notification-rule"][i]["resourceFilter"]['resourceId'])
            except:
                array_notification_setting_data_vmuuid.append("-")

    print("{:<35} : OK".format("2.get_notification_setting "))
    return array_notification_setting_data_rulename, array_notification_setting_data_vmuuid

# Query metric datas form selected metrics
def convert_uuid_to_vmname(token, platform):
    if "Intel" in platform:
        if platform == 'Intel_dom4':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    if "HPE" in platform:
        if platform == 'HPE_dom1,2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'HPE_dom3_synergy':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'HPE_dom3_simplivity':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    elif "Flexpod" in platform:
        if platform == 'Flexpod_dom1':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Flexpod_dom2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Flexpod_dom3':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Flexpod_Kerry':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    elif "Dell" in platform:
        if platform == 'Dell_dom2':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Dell_dom3_PRD':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        elif platform == 'Dell_dom3_POC':
            fetch_data_from_vm_url = 'https://xxxxxxx/suite-api/api/resources?resourceKind=virtualmachine&pageSize=2000'
            headers = {
                "Authorization": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
    x = requests.get(url=fetch_data_from_vm_url, headers=headers, verify=False)
    get_vm_data = json.loads(x.text)

    data_pair_vmname_and_uuid = []
    
    for i in range (len(get_vm_data["resourceList"])):
        data_pair_vmname_and_uuid.append([{"vmname": get_vm_data["resourceList"][i]["resourceKey"]["name"], "uuid": get_vm_data["resourceList"][i]["identifier"]}])

    print("{:<35} : OK".format("3.Convert UUID to VMname "))
    return data_pair_vmname_and_uuid

def append_data_prepare_for_pandas(array_notification_setting_data_rulename, array_notification_setting_data_vmuuid, data_pair_vmname_and_uuid):
    prepare_data_for_pandas = {"rulename" : [], "order_name" : []}
    for i in range (len(array_notification_setting_data_rulename)):
        prepare_data_for_pandas["rulename"].append(array_notification_setting_data_rulename[i])
        count_match = 0
        for j in range (len(data_pair_vmname_and_uuid)):
            if array_notification_setting_data_vmuuid[i] != data_pair_vmname_and_uuid[j][0]["uuid"]:
                count_match += 1
            else:
                prepare_data_for_pandas["order_name"].append(data_pair_vmname_and_uuid[j][0]["vmname"])
        if count_match == len(data_pair_vmname_and_uuid):
            prepare_data_for_pandas["order_name"].append("-")

    print("{:<35} : OK".format("4.append_data_prepare_for_pandas "))
    return prepare_data_for_pandas

def convert_list_to_excel_by_pandas(prepare_data_for_pandas, platform_name):
    username = os.getlogin()
    df = pd.DataFrame(prepare_data_for_pandas, columns = ['rulename', 'order_name'])
    df.to_excel (r'C:\Users\{0}\Desktop\export_notification_setting_{1}.xlsx'.format(username, platform_name), index = False, header=True)
    print("{:<35} : OK".format("5.convert_list_to_excel_by_pandas "))
    print("==========================================\n")

# Operation
def main():
    input_platform, input_confirm_connect_vpn = user_operation()
    platform_name_list = convert_platform_number_to_platform_name(input_platform)

    for platform_name in platform_name_list:
        token = get_token(platform_name)
        array_notification_setting_data_rulename, array_notification_setting_data_vmuuid = get_notification_setting_data(token, platform_name)
        data_pair_vmname_and_uuid = convert_uuid_to_vmname(token, platform_name)
        prepare_data_for_pandas = append_data_prepare_for_pandas(array_notification_setting_data_rulename, array_notification_setting_data_vmuuid, data_pair_vmname_and_uuid)
        convert_list_to_excel_by_pandas(prepare_data_for_pandas, platform_name)

if __name__ == "__main__":
    main()


