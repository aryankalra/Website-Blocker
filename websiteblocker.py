import time
from datetime import datetime as dt # utilising dt to refer the code easily

hosts_path = "/etc/hosts" # set host according to user operating system
redirect = "127.0.0.1" # redirect to the localhost's machine/IP - defaults to 127.0.0.1

websites = ["www.sportsbet.com.au", "sportsbet.com.au"]     # list of websites blockable through modification

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,8): # set time to dictate the period of time to block and unblock websites
        print("Blocking Specified Websites") # printed output viewed in terminal displaying the blocking method
        with open(hosts_path, "r+") as file: # r+ allows for the ability to read and append files
            content = file.read() # this line is used to print content
            for website in websites:
                if website in content:
                    pass # skip to time.sleep(5)
                else:
                    file.write(redirect+" "+website+"\n") # mapping the hostnames to the direct localhost IP address
    else:
        print("Unblocking Specified Websites") # printed output viewed in terminal displaying the unblocking method
        with open(hosts_path, "r+") as file:
            content = file.readlines() # returns a list containgin each line in the file as a list item
            file.seek(0)  # reset the pointer to the top of the text file and defaults to current position
            for line in content:
                if not any(website in line for website in websites): # overwrites the whole file
                    file.write(line) # this writes to an existing file and rewrites the content in the host file
                # do nothing otherwise
            file.truncate() # this is utilised to delete delete trailing lines and remove hostnames from the host file
    #optional print str may be displayed to display better emphasis to the user
    time.sleep(5) # adding a five second delay in the execution of a program

  
