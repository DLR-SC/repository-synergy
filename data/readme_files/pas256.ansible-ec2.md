# ansible-ec2

A collection of commands to simplify common tasks built on top of Ansible and the EC2 external inventory plugin.


## Examples

    # Tell me what the heck the 'info' command does
    ansible-ec2 help info

    # SSH into the EC2 instance with the 'Name' tag 'Web1'
    ansible-ec2 ssh --name Web1
    
    # List all instances in the us-east-1a availability zone
    ansible-ec2 list --zone us-east-1a
    
    # Give me detailed information about all m1.xlarge instances in the 'database' security group 
    ansible-ec2 info --type m1.xlarge --sg database


## Setup and Installation

1.  Set up Ansible

    http://ansible.cc/docs/gettingstarted.html
   
1.  Configure the EC2 inventory plugin
   
        cp ansible/plugins/inventory/ec2.py /etc/ansible/hosts
        cp ansible/plugins/inventory/ec2.ini /etc/ansible/ec2.ini
        cat > ~/.boto <<EOF
        [Credentials]
        aws_access_key_id = AKIA123
        aws_secret_access_key = SeCrEt123
        EOF
    
    Confirm it is working by running
  
        /etc/ansible/hosts
   
1.  Put `ansible-ec2` on your path somewhere, or change your path

        export PATH="${PATH}:/path/to/ansible-ec2/bin"

Now you can run through the [examples](#examples) above or simply list all instance

    ansible-ec2 list


## Usage

    ansible-ec2 COMMAND [OPTIONS] [FILTERS]


## Commands

-   `help`  Get help about a command

-   `list`  Get a list of instances

-   `info`  Get detailed information about instances

-   `ssh`  Open an interactive SSH connection to a specific instance


## Filters

By default, `ansible-ec2` performs a command against all instances. This might be fine for `list`, but far from ideal for `ssh`. This is where filters become powerful, by limiting the set of instances a command runs on.

Multiple filters can be used together to target specific instances. In this example, only *m1.large* instances using the *peter* key pair in *us-east-1b* are listed:

    ansible-ec2 list --type m1.large --key peter --zone us-east-1b

### Name

EC2 instances can have tags (simple key/value pairs) associated with them. The 'Name' tag is of particular interest as it is the first column in the [AWS Web Console](https://console.aws.amazon.com/ec2/home#s=Instances). To run only against instances with a specific value for the 'Name' tag, use:

    --name NAME
    
    Example:
    ansible-ec2 list --name MyDB1
    
### Security Group

Run a command only against instances in a specific security group

    --sg SECURITY_GROUP
    
    Example:
    ansible-ec2 list --sg default

### Key Pair

The name of the key pair to filter on

    --key KEY_PAIR
    
    Example:
    ansible-ec2 list --key superadmin

### Instance Type

EC2 instances come in a variety of different types, from *t1.micro* to *m1.medium* to *hi1.4xlarge*. This filter enables limiting the instance list to only those using a specific instance type

    --type INSTANCE_TYPE
    
    Example:
    ansible-ec2 list --type=m1.xlarge

### Region and Availability Zone

EC2 is all over the world, so these 2 filters create a subset of instance only in a specific region or availability zone

    --region REGION
    --zone AVAILABILITY_ZONE
    
    Examples:
    ansible-ec2 list --region us-east-1
    ansible-ec2 list --zone us-east-1a

### Instance ID and Raw Group Name

The hosts returned by the EC2 inventory plugin are in one or more groups. One such group is the Instance ID. As the plugin evolves, more groups may be added, so this allows access to all of them without code modification. It also allows filtering on other tag key/value pairs.

    Examples:
    ansible-ec2 info i-abcd1234
    ansible-ec2 list tag_aws_elasticmapreduce_instance-group-role_CORE
    ansible-ec2 list tag_aws_elasticmapreduce_job-flow-id_j-ABCD1234EFGH
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        