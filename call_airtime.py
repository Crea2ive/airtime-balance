'''
CALCULATING CREDIT BALANCE USING CALL LOG FILE FROM GSM GATEWAY

This code is designed to analyze an extracted call log file in .csv format obtained from a GSM gateway device with four ports. 
Each port on the GSM gateway corresponds to a SIM card. The code will prompt you to input the port name and the total amount you 
have recharged on the corresponding SIM card. This information is then used to calculate the credit balance associated with each SIM card.  

'''

w = input('Enter port name: ')
if w == "GSM1":
    w = "GSM1"
elif w == "GSM2":
    w = "GSM2"
elif w == "GSM3":
    w = "GSM3"
elif w == "GSM4":
    w = "GSM4"
else:
    print("Incorrect input: try to sepcify the port name, e.g: GSM1")
    quit()

while True:
    break

try:
  rch = int(input("Enter total airtime amount recharged: N "))
#  print("rch:", rch)
except ValueError:
    print("Please input integer only...")
    quit()
    
am = float(rch)
rchdr = 8.07 # time in seconds
next_call_duration = am * rchdr # next Call duration in seconds
fhand = open("calllog.txt")
#print(fhand)


ctime = 0 # call duration in secs
for line in fhand:
    lines = line.rstrip()
    if not w in lines : #this searches for 'GSM1' in all lines
        continue
    sp = lines.split(',')
    sub = (sp[6])
    c = float(sub)
    ctime = ctime + c
mcall = 60.0
cd = ctime/mcall # Call duration in minutes
next_call = next_call_duration/mcall

print("\n"
"-Expected Next Call time:", int(next_call),"m",'\n'
"-Actual call time:",int(cd),"m",'\n'                  # This should always be less than the 'next_call'
"-Remaining call time:",int(next_call-cd),"m",'\n'    #
"-Airtime Balance:","N",int(((next_call-cd)*60)/8.07)
)
