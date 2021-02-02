import os
 
filename = input('Enter file name: ')
environment = int(input('Enter 1 for iot, 2 for preprod and 3 for prod: '))
snsSubject = []
m = 0
print(environment)

#Commands based on environment
iot = ''' aws sns publish --topic-arn "arn:aws:sns:us-east-1:XXXXXXXXXX:soa-iot-lfs-combined" --subject '''
preprod = ''' aws sns publish --topic-arn "arn:aws:sns:us-east-1:XXXXXXXXXX:soa-preprod-lfs-combined" --subject '''
prod = ''' aws sns publish --topic-arn "arn:aws:sns:us-east-1:XXXXXXXXXXX:soa-prod-lfs-combined" --subject '''
nonprod_message_end = ''' --message "test" --profile SOA-Nonprod-DevOpsMed '''
prod_message_end = ''' --message "test" --profile SOA-Prod-DevOpsMed '''

#Process file and execute commands based on environment
file_to_read = open(filename, 'r')
for line in file_to_read:
    snsSubject.append(line.rstrip('-200.dat\n'))
    if environment == 1:
        command = iot + snsSubject[m] + nonprod_message_end
        print(command)
        os.system(str(command))
        m += 1
    elif environment == 2:
        command = preprod + snsSubject[m] + nonprod_message_end
        print(command)
        os.system(str(command))
        m += 1
    elif environment == 3:
        command = prod + snsSubject[m] + prod_message_end
        print(command)
        os.system(str(command))
        m += 1
