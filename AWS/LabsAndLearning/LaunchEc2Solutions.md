## CLI Solution
- Launch multiple instances from the cli with the following command:
``aws ec2 run-instances --image-id <ami> --count <integer> --instance-type <ex. t2.micro>``
- Terminate all instances from cli 
``aws ec2 terminate-instances --instance-ids <imageid> <imageid> <etc>
