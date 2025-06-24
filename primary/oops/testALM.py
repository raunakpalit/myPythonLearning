# final_result = False
#     #architecture  = sys.argv[1]
#     architecture=architecture.lower()
#     ecg_type = architecture
#     #print("ecg_type is -----",ecg_type)

#     can_ini_relative_path = r"\AppData\Roaming\can.ini"
#     can_ini_file = os.path.expanduser('~')+ can_ini_relative_path
#     #print(can_ini_file)

#     config_obj = configparser.ConfigParser()
#     config_obj.read(can_ini_file)

#     hs1_serial = config_obj.get('HS1','serial')
#     hs1_channel = config_obj.get('HS1','channel')
#     fd1_serial = config_obj.get('FD1','serial')
#     fd1_channel = config_obj.get('FD1','channel')


#     config_file = r'C:\FORD-IVIC-TEST\FT-ECG-ALM\config\conf.py'    
#     with open(config_file) as f1:
#         out = f1.read()

#         #ecg_type parameter is updated to ECG1/ECG2 based on architecture
#         match= re.search("'type':\s+'([A-Za-z0-9]+)", out)
#         if match:
#             out = re.sub(match.group(1),ecg_type,out)

#         #HS1 and FD1 serial is updated based on CAN.INI  file
#         match= re.search("('HS1':\s+\{\s+'serial':\s+')([a-zA-Z0-9]+)", out)
#         if match:
#             out = re.sub(match.group(),match.group(1)+hs1_serial, out)

#         match= re.search("('HS1':\s{+\s*[^}]*'channel':\s+)([0-9]+)", out)
#         if match:
#             out = re.sub(match.group(),match.group(1)+hs1_channel, out)

#         match = re.search("('FD1':\s+\{\s+'serial':\s+')([a-zA-Z0-9]+)", out)
#         if match:
#             out = re.sub(match.group(),match.group(1)+fd1_serial, out)

#         match= re.search("('FD1':\s{+\s*[^}]*'channel':\s+)([0-9]+)", out)
#         if match:
#             out = re.sub(match.group(),match.group(1)+fd1_channel, out)

#         #token_required parameter is set to True
#         match=re.search("'token_required': False",out)
#         if match:
#             out=re.sub(match.group(),"'token_required': True",out)

#         #Updating COMPort based on value set in environmet variable ECG_CCPU
#         match=re.search("COM102",out)
#         if match:
#             ecg_ccpu=os.environ["ECG_CCPU"]
#             out=re.sub(match.group(),ecg_ccpu,out)

#         #set_value of ECG based on architecure only if architecture is ECG2 then the paramenter is updated to ECG2     
#         match=re.search("ECG",out)
#         if match and ecg_type=='ecg2':
#             ecg_type=ecg_type.upper()
#             out=re.sub(match.group(),ecg_type,out)

#     with open(config_file,'w') as f2:
#         f2.write(out)
#         final_result = True    

#     return final_result


ecg_type = "ECG2"
hs1_serial = "B20101"
hs1_channel = 1
fd1_serial = "XYZ123"
fd1_channel = 2
config_file = "conf.py"

# type_match = re.search("'type':\s+'([A-Za-z0-9]+)", out)

with open(config_file, "r+") as fd:
    for line in fd.readlines():
        if "'ap_port': " in line:
            print(line.strip())
        if "'token_required': " in line:
            print(line.strip())
        if "'type': " in line:
            print(line.strip())
        if "'HS1': {" in line:
            print(line.strip())
        if "'FD1': {" in line:
            print(line.strip())
        if "ecu_config.get_config('ecu_type')" in line:
            print(line.strip())
