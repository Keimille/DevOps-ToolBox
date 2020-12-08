# Terraform Core Knowledge
In this area you should find some general knowledge to getting started and getting comfortable will Terraform skill sets.

## Recommended Learning
I generally like to begin study of a new area by studying for certifications. Most organizations that offer certification for their tools usually compile and organize the knowledge needed to gain basic competency. With Terraform I recommend stusdying with the study guide used for their Terraform Associate certification.

The outline for this [study guide](https://learn.hashicorp.com/tutorials/terraform/associate-study) is as follows:

- Learn about IaC
- Manage Infrastructure
- Master the workflow
- Learn more subcommands
- Use and create modules
- Read and write configuration
- Manage State
- Debug Terraform
- Understand Terraform Cloud and Enterprise

I try to design labs or drills to help build skill sets for each of these areas in the Labs and Learning folder. Additionaly, the [study guide](https://learn.hashicorp.com/tutorials/terraform/associate-study) has tutorials that are very helpful.

## Other Helpful Resources
I have found Anton Babenko's content especially helpful. You can check out his [YouTube channel](https://www.youtube.com/channel/UCGH0yYPvlCN1VjSFMGVmFgQ) for weekly content. 

## Labs & Drills

### Manage Infrastructure

### Master The Workflow

### Use and Create Modules

#### Lab 1 - Sourcing a Module and Specific Version from Github

1. Create a module repository from Github or [fork this one](https://github.com/Keimille/terraform-aws-s3website)
2. Create a terraform plan without any errors

#### Lab 2 - Source a Module That is Located Locally

1.Clone the repository mentioned in Lab 1
2. Create a terraform plan without any errors by sourcing the module locally

### Read and Write Configuration
#### Lab 1 - Navigating Local Workspaces

1. Create a workspace named test in the command line and navigate between the two.
2. List all workspaces
3. Switch to default workspace
4. Destroy test workspace

#### Drill 1 - Create EC2 resource
1. Recall only one resource block that creates two ec2 instances resource without refrencing documentation. Include tags to include ami id, and instance type.

### Manage state

### Debug Terraform
