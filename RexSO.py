# <------CoDed By AnonCODER------>
# <------First Version : v1.0------>
# <------Help me improve it :)------>
import subprocess
from os import system
from colorama import Fore

#again
def again():
    again_v = input(Fore.GREEN+'For Menu type (M) for Exit type (E) : ')
    if again_v.upper() == 'M' or again_v.upper() == 'Menu' or again_v.lower() == 'm' or again_v.lower() == 'menu':
        start()
    elif again_v.upper() == 'E' or again_v.upper() == 'Exit' or again_v.lower() == 'e' or again_v.lower() == 'exit':
        print(Fore.YELLOW+'[-] Good Luck !')
    else:
        print(Fore.RED+'Wrong Value !')
        again()



#Information Gathering
def inf():
    info = input(Fore.CYAN+'''
 ___        __                                   
|_ _|_ __  / _| ___  
 | || '_ \| |_ / _ \|
 | || | | |  _| (_)  
|___|_| |_|_|  \___/  

[+] Welcome to Information Gathering section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool.
[~] More Tools Coming... :)
---------------------------------
|    [+] Nmap : 1               |                          
|    [+] WPScan : 2             |                
|    [+] CMS Scanner : 3        |                    
|    [+] XSStrike : 4           |                                          
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')

    info = int(info)

    if info == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        nmap = subprocess.check_output('git clone https://github.com/nmap/nmap.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Nmap is ready to use')
        again()


    elif info == 2:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        wpscan = subprocess.check_output('git clone https://github.com/wpscanteam/wpscan.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! WPScan is ready to use')
        again()


    elif info == 3:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        cms = subprocess.check_output('git clone https://github.com/ajinabraham/CMSScan.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! CMS Scanner is ready to use')
        again()


    elif info == 4:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        xss = subprocess.check_output('git clone https://github.com/s0md3v/XSStrike.git')
        system('clear')
        print(Fore.BLUE+'[+] Done ! XSStrike is ready to use')
        again()
        

    elif info == 10:
        start()

    elif info == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()
                 


#Password Attacks
def password():
    passwd = input(Fore.YELLOW+'''
 ____                                     _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|


[+] Welcome to Password Attacks section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool (Python,Ruby and libraries).
[~] More Tools Coming... :)
---------------------------------
|    [+] Cupp : 1               |                          
|    [+] Ncrack : 2             |                
|    [+] CeWL : 3               |                                                                       
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')

    passwd = int(passwd)

    if passwd == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        cupp = subprocess.check_output('git clone https://github.com/Mebus/cupp.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Cupp is ready to use')
        again()

    elif passwd == 2:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        ncrack = subprocess.check_output('git clone https://github.com/nmap/ncrack.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Ncrack is ready to use')
        again()

    elif passwd == 3:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        cewl = subprocess.check_output('git clone https://github.com/digininja/CeWL.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Cewl is ready to use')
        again()

    elif passwd == 10:
        start()
        
    elif passwd == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()



#Wireless Testing
def wireless():
    wire = input(Fore.BLUE+'''
__        ___          _               
\ \      / (_)_ __ ___| | ___  ___ ___ 
 \ \ /\ / /| | '__/ _ \ |/ _ \/ __/ __|
  \ V  V / | | | |  __/ |  __/\__ \__
   \_/\_/  |_|_|  \___|_|\___||___/___/
                                       

[+] Welcome to Wireless Testing section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool (Python,Ruby and libraries).
[~] More Tools Coming... :)
---------------------------------
|    [+] Aircrack-ng : 1        |                          
|    [+] Wifite : 2             |                
|    [+] Kismet : 3             |                                                                       
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')

    wire = int(wire)

    if wire == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        air = subprocess.check_output('git clone https://github.com/aircrack-ng/aircrack-ng.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Aircrack-ng is ready to use')
        again()

    elif wire == 2:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        wifi = subprocess.check_output('git clone https://github.com/derv82/wifite.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Wifite is ready to use')
        again()

    elif wire == 3:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        kis = subprocess.check_output('git clone https://github.com/kismetwireless/kismet.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Kismet is ready to use')
        again()

    elif wire == 10:
        start()

    elif wire == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()   



#Exploitation Tools
def exp():
    exploit = input(Fore.RED+'''  
 _____            _       _ _                 
| ____|_  ___ __ | | ___ (_) |_  
|  _| \ \/ / '_ \| |/ _ \| | __/ 
| |___ >  <| |_) | | (_) | | || 
|_____/_/\_\ .__/|_|\___/|_|\__
           |_|                          

[+] Welcome to Exploitation Tools section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool (Python,Ruby and libraries).
[~] More Tools Coming... :)
---------------------------------
|    [+] Commix : 1             |                          
|    [+] ATSCAN : 2             |                
|    [+] Sqlmap : 3             |
|    [+] Metasploit : 4         |                                                                       
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')

    exploit = int(exploit)

    if exploit == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        commix = subprocess.check_output('git clone https://github.com/commixproject/commix.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Commix is ready to use')
        again()

    elif exploit == 2:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        ats = subprocess.check_output('git clone https://github.com/AlisamTechnology/ATSCAN.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! ATSCAN is ready to use')
        again()

    elif exploit == 3:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        sqlmap = subprocess.check_output('git clone https://github.com/sqlmapproject/sqlmap.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Sqlmap is ready to use')
        again()

    elif exploit == 4:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        meta = subprocess.check_output('git clone https://github.com/rapid7/metasploit-framework.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Metasploit is ready to use')
        again()

    elif exploit == 10:
        start()

    elif exploit == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()          



#Sniffing & Spoofing
def snf():
    snif = input(Fore.LIGHTMAGENTA_EX+''' 
 ____        _  __  __ _             
/ ___| _ __ (_)/ _|/ _(_)_ __   __ _ 
\___ \| '_ \| | |_| |_| | '_ \ / _` |
 ___) | | | | |  _|  _| | | | | (_| |
|____/|_| |_|_|_| |_| |_|_| |_|\__, |
                               |___/ 
                                          
[+] Welcome to Sniffing & Spoofing Tools section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool (Python,Ruby and libraries).
[~] More Tools Coming... :)
---------------------------------
|    [+] Responder : 1          |                          
|    [+] Mitmproxy : 2          |                                                                                              
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')

    snif = int(snif)

    if snif == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        responder = subprocess.check_output('git clone https://github.com/SpiderLabs/Responder.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Responder is ready to use')
        again()

    elif snif == 2:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        mitm = subprocess.check_output('git clone https://github.com/mitmproxy/mitmproxy.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Mitmproxy is ready to use')
        again()

    elif snif == 10:
        start()

    elif snif == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()          



#Web Hacking
def web():
    web_h = input(Fore.LIGHTCYAN_EX+'''        
__        __   _     
\ \      / /__| |__  
 \ \ /\ / / _ \ '_ \ 
  \ V  V /  __/ |_) |
   \_/\_/ \___|_.__/ 
                         
[+] Welcome to Web Hacking section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool (Python,Ruby and libraries).
[~] More Tools Coming... :)
---------------------------------
|    [+] Nikto : 1             |                          
|    [+] Joomscan : 2           |                
|    [+] Vbscan : 3             |                                                                           
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')

    web_h = int(web_h)

    if web_h == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        nikto = subprocess.check_output('git clone https://github.com/sullo/nikto.git' , shell=True) 
        system('clear')
        print(Fore.BLUE+'[+] Done ! Nikto is ready to use')
        again()

    elif web_h == 2:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        joomscan = subprocess.check_output('git clone https://github.com/OWASP/joomscan.git' , shell=True) 
        system('clear')
        print(Fore.BLUE+'[+] Done ! Joomscan is ready to use')
        again()

    elif web_h == 3:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        vbscan = subprocess.check_output('git clone https://github.com/OWASP/vbscan.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Vbscan is ready to use')
        again()

    elif web_h == 10:
        start()

    elif web_h == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()          
   

   
#Post Exploitation
def p_exploit():
    p_exp = input(Fore.LIGHTCYAN_EX+'''        
 ____           _   
|  _ \ ___  ___| |_ 
| |_) / _ \/ __| __|
|  __/ (_) \__ \ |_ 
|_|   \___/|___/\__|
           
[+] Welcome to Web Hacking section.
[+] Now You can choose your tools.
[!] After installation you need to check Requirements for each tool (Python,Ruby and libraries).
[~] More Tools Coming... :)
---------------------------------
|    [+] Weeman : 1             |                                                                                                               
|                               |                     
|    [+] Start Menu : 10        |                                          
|    [-] Exit : 0               |                        
---------------------------------
    
RexSO >>> ''')
 
    p_exp = int(p_exp)

    if p_exp == 1:
        print(Fore.BLUE+'[~] Ok, Please Wait...')
        exe2hex = subprocess.check_output('git clone https://github.com/evait-security/weeman.git' , shell=True)
        system('clear')
        print(Fore.BLUE+'[+] Done ! Weeman is ready to use')
        again()

    elif p_exp == 10:
        start()

    elif p_exp == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'Wrong Value !')
        again()



#Update
def update():
    system('git clone https://github.com/AnonC0DER/RexSO.git')
    print('~> Updated successfully !')
    sleep(1.5)
    system('cd RexSO')
    system('clear')
    system('python3 RexSO.py')


#About Me && contact Me
def contact():
    system('clear')
    print(Fore.LIGHTYELLOW_EX +'''
 ____________________________________________                                       
|   # I'm AnonCODER                          |
|     # Or NoobsFather                       |       
|       # My real name is Hesam              |         
| # if you have any idea for this appliction |
|        # or you wanna talk to me           |
|       # Contact Me : @NoobsFather          |
|      # Email : AnonCODER@tutanota.com      |
|____________________________________________|
''')



#start
def start():
    system('clear')
    os = int(input(Fore.LIGHTGREEN_EX+'''
 ____            ____   ___  
|  _ \ _____  __/ ___| / _ \ 
| |_) / _ \ \/ /\___ \| | | |
|  _ <  __/>  <  ___) | |_| |
|_| \_\___/_/\_\|____/ \___/ 

------------------------
|CodeD By AnonC0DER :) |
|        v1.0          |
------------------------

[*] Hello, Im RexSO Script.
[*] Im here to help you install Penetration testing tools on any linux Os.
[*] You can use me on Linux operating systems.   
[*] So, Which tools do you want to use now?

##############################################
#  [+] Information Gathering = 1             #
#  [+] Password Attacks = 2                  #
#  [+] Wireless Testing = 3                  #
#  [+] Exploitation Tools = 4                #
#  [+] Sniffing & Spoofing = 5               #
#  [+] Web Hacking = 6                       #                             
#  [+] Post Exploitation = 7                 #
#                                            #
#  [+] About Author && Contact Author = 1000 #    
#  [+] Update = 100                          #  
#  [-] Exit = 0                              #    
##############################################

    
RexSO >>> '''))

    

    if os == 1:
        system('clear')
        inf()

    elif os == 2:
        system('clear')
        password()

    elif os == 3:
        system('clear')
        wireless()

    elif os == 4:
        system('clear')
        exp()

    elif os == 5:
        system('clear')
        snf()

    elif os == 6:
        system('clear')
        web()

    elif os == 7:
        system('clear')
        p_exploit()

    elif os == 1000:
        contact()
        again()

    elif os == 100:
        update()

    elif os == 0:
        print(Fore.YELLOW+'[-] Se You Later :)')

    else:
        print(Fore.RED+'[*] Wrong Value !')
        again()


start()


# <------CoDed By AnonCODER------>
# <------First Version : v1.0------>
# <------Help me improve it :)------>