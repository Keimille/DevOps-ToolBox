## CLI Solution
- Launch multiple instances from the cli with the following command:
``aws ec2 run-instances --image-id <ami> --count <integer> --instance-type <ex. t2.micro>``
- Terminate all instances from cli 
``aws ec2 terminate-instances --instance-ids <imageid> <imageid> <etc>``

## CLI and CloudFormation Solution
- Create key using CLI
``aws ec2 create-key-pair --key-name mytestkey``
- Create template from scratch (for practice but not necesarry) There is a sample template in this repository.
- Validate template
``aws cloudformation validate-template --template-body file://ec2nginx.yaml``
- Launch template
``aws cloudformation create-stack --stack-name myteststack1 --template-body file://ec2nginx.yaml``

You can check your stack progress by using the command ``aws cloudformation describe-stacks``
