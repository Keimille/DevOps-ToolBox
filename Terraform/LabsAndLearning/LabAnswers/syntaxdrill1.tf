source "aws" "ec2_instance"{
    ami             = "<ami-id>"
    instance_type   = "t2.micro"
    instcance_count = 2
}
