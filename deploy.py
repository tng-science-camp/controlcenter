#!/usr/bin/env python3
import paramiko
import subprocess
import getpass
import re
import os
from time import sleep

DELAY_TICK=0.05

#TARGET_ROVER is now automatically determined based on userid. You may hardcode it below 
USERNAME='rover'
PASSWORD='rover'



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()



#get userid
userid = getpass.getuser()

#parse a num after "control". userid must be in the control"X" format
num = re.sub('\control', '', userid)

TARGET_ROVER = "rover"+num
#print(TARGET_ROVER)
exit


# Create transmission delay
# make a list
items = list(range(0, 57))
i = 0
l = len(items)

# Initial call to print 0% progress
printProgressBar(i, l, prefix = 'Transmitting:', suffix = 'Complete', length = 50)
for item in items:
    # Do stuff...
    sleep(DELAY_TICK)
    # Update Progress Bar
    i += 1
    printProgressBar(i, l, prefix = 'Transmitting:', suffix = 'Complete', length = 50)


# remote execution
print('Executing...')


# Connect to remote host
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(TARGET_ROVER, username=USERNAME, password=PASSWORD)

# Setup sftp connection and transmit this script
sftp = client.open_sftp()
sftp.put('command.py', '/home/rover/command.py')
sftp.close()

# Run the transmitted script remotely without args and show its output.
# SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
stdout = client.exec_command('python3 /home/rover/command.py')[1]
#stdout = client.exec_command('python3 /home/rover/command.py')

for line in stdout:
    # Process each line in the remote output
    #print(line.rstrip('\n'))
    print(line)
client.close()

 
i = 0
# Initial call to print 0% progress
printProgressBar(i, l, prefix = 'Receiving:', suffix = 'Complete', length = 50)
for item in items:
    # Do stuff...
    sleep(DELAY_TICK)
    # Update Progress Bar
    i += 1
    printProgressBar(i, l, prefix = 'Receiving:', suffix = 'Complete', length = 50)


#rsync data and img files. 
os_cmd="rsync -a rover@" + TARGET_ROVER + ":/var/www/html/rover_img/ rover_img"
#print(os_cmd)
os.system(os_cmd)


#You can call a subprocess from python using the following snippet

#subprocess.call(["rsync", "-a", "rover1@rover1:/var/www/html/rover_img/", "/Users/kevincho/rover_img"])
