import smtplib  #simple mail transfer protocol
from email.message import EmailMessage

def sendmail(name,branch,section,mailid):
    covstr="\nStay Safe and Make sure to wear a Mask when you go outside."
    autogenstr="\n\n(This is a Auto Generated mail written in python by Hariharan.A using data from the branch allotment pdf.)"
    genstr="Happy Birthday "+name+" of "+branch+" branch and "+section+" section.\n"+"Have a great day..!\n"+autogenstr+"\n"+covstr+"\n\nWishes from:\n"+"Hariharan.A\n"+"ECE S2"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("email", "password")
    email=EmailMessage()
    email["From"]="email"
    email["To"]=mailid
    subgen="Happy Birthday "+name
    email["Subject"]=subgen
    email.set_content(genstr)
    server.send_message(email)
    print("\nMail sent to:\n",mailid,"\nMessage:\n",genstr,"\n")

file = open("final.txt","r")
d={}
while True:
    line = file.readline()
    l1 = line.split()
    if l1==[]:
        break
    #print(l1)
    strl=""
    i=3
    while "@" not in l1[i]:
        strl+=l1[i]
        strl+=" "
        i+=1
    #0 i+3 is branch 1 i+2 is bday 2 -1 is section
    d[l1[i]] = [strl,l1[i + 3], l1[i + 2],l1[-1]]
    #print(strl)
    #print(l1[i+2])
    #print(d)
    #print()
file.close()
print(len(d))

while True:
    opt=int(input("Enter 1 to search with Name or \n2 to search with DOB or \n3 to search by section(S2, etc)\n4 to search by Branch(CS, IT, ECE...etc): "))
    retval=False
    if opt==1:
        inp=input("Enter the Name: ")
        for i in d:
            if inp.upper() in d[i][0]:
                print(d[i][0],d[i][2],d[i][1],d[i][3])
                retval=True
    elif opt==2:
        inp=input("Enter DOB in format (mm/dd/yyyy): ")
        for i in d:
            if inp in d[i][2]:
                print(d[i][0],d[i][2],d[i][1],d[i][3])
                #sending mail
                conopt=input("Do you want to send Birthday wishes mail to "+d[i][0]+" "+i+"\n(y for yes)")
                if conopt=="y"or conopt=="Y":
                    sendmail(d[i][0],d[i][1],d[i][3],i)
                else:
                    print("Email not sent!")
                retval=True
    elif opt==3:
        inp = input("Enter Section (S1 or S2,etc): ")
        for i in d:
            if inp in d[i][3] or inp.upper() in d[i][3]:
                print(d[i][0],d[i][2],d[i][1],d[i][3])
                retval = True
    elif opt==4:
        inp = input("Enter Branch (CS or IT or ECE or EEE or MECHANICAL or CIVIL or CHEMICAL or BME: ")
        for i in d:
            if inp in d[i][1] or inp.upper() in d[i][1]:
                print(d[i][0],d[i][2],d[i][1],d[i][3])
                retval = True
    else:
        print("WRONG OPTION!")
    print()
    if retval==False:
        print("Record not found!")
    conopt=input("Enter y to continue searching: ")
    if conopt!="y":
        print("Exiting!")
        break
