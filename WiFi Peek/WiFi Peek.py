from os import system
from subprocess import getoutput

# Changin system color
system('color a')

print('            #####################################')
print('            #                                   #')
print('            #        WiFi Peek                  #')
print('            #        version 1.0                #')
print('            #        Author: Owbird             #')
print('            #        https://github.com/owbird  #')
print('            #                                   #')
print('            #####################################')

print('')

# Collecting saved WiFi networks to a text file
system('netsh wlan show profiles > database.txt')

print('*'*30)

# Opening and reading text file
with open('database.txt', 'r') as db:

    for line in db.readlines():

        if 'All User Profile' in line:

            line = line.strip('\n').split(': ')

            # Viewing profile for each network
            status = getoutput(f'netsh wlan show profiles "{line[1]}" key=clear')

            # Extracting passwords
            for key in status.split('\n'):

                if 'Key Content' in key:

                    key = key.split(':')

                    # printing found passwords
                    print(f'[+] WiFi Name: {line[1]}\n[+] WiFi Password: {key[1]}\n')

                    print('*'*30)

# Deleting text file
system('del database.txt')
system('pause')
