## Ansible playbook to deploy distributed technologies
This project is a set of Ansible playbooks to easily install a set of distributed technologies on [AWS](https://aws.amazon.com/)

## Table of Contents
1. [Supported playbooks](#supported-playbooks)
2. [Supported commands](#supported-commands)
3. [Setup](#setup)
  * [On your local/remote machine](#on-your-localremote-machine)
  * [Using Docker container](#using-docker-container)
4. [Playbooks](#playbooks)
  * [Launch/Terminate EC2 instances on AWS](#ec2)
  * [Zookeeper](#zookeeper)
  * [Kafka](#kafka)
  * [Vowpal Wabbit](#vowpal-wabbit)

## Supported playbooks
* EC2
* Zookeeper
* Kafka

## Supported Commands
```bash
~$ ansible-playbook <master-playbook>.yml --extra-vars "<var1>=<value1> <var2>=<value2>" --tags "<tag1>,<tag2>"
```
* **EC2** playbook is controlled by a yaml file containing variables for the EC2 instances to be acted on. More details [below](#ec2)
* **Zookeeper**, **Kafka**, and **Vowpal Wabbit** playbooks need respective cluster tags to be specified to identify which nodes are in the cluster and need to be acted on. More details [below](#zookeeper)

## Setup
### On your local/remote machine
1. [Setup ansible for your system](http://docs.ansible.com/ansible/intro_installation.html)
2. Create following folders

  ```bash
  ~$ mkdir -p /etc/ansible/hosts
  ```
3. Clone this repo

  ```bash
  ~$ git clone https://github.com/InsightDataScience/ansible-playbook.git
  ```

4. Copy the `ec2.py` and `ec2.ini` files in this repo to `/etc/ansible/hosts`
5. Update information in `ansible_example.cfg` and move it to `/etc/ansible/ansible.cfg`
6. Export AWS credentials as environment variables

  ```bash
  export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXX
  export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXX
  ```

## Using Docker container
1. [Setup Docker for your system](https://docs.docker.com/engine/installation/)
2. Clone this repo

  ```bash
  ~$ git clone https://github.com/InsightDataScience/ansible-playbook.git
  ```
3. Build your docker image locally with the following command - run this from the root folder of this repo

  ```bash
  ~$ docker build -t ansible-playbook -f conf/Dockerfile .
  ```

4. Run the docker container in interactive mode using the script in the repo - `run_ansible_playbook_container.sh`

  ```bash
  ~$ ./run_ansible_playbook_container.sh
  ```
5. Update information in `/etc/ansible/ansible.cfg` config file inside the container
6. Export AWS credentials in `~/.profile` inside the container

  ```bash
  export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXX
  export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXX
  ```

## Playbooks
* ###EC2

  Launch/Start/Stop/Terminate EC2 instances on AWS.

  * ####Variable file: 
    
    Update `example_ec2_vars.yml` as per your requirement

    EC2 playbook is controlled by a yaml file with variables defined for the EC2 instances. An example variable file -`example_ec2_vars.yml` - is included in this repo. You can define your own yaml file with the following information:

    ```yaml
    ---
    key_pair: <key-name>
    instance_type: <instance-type>
    region: <region>
    security_group_id: <security-group-id>
    num_instances: <num-of-instances>
    subnet_id: <subent-id>
    tag_key_vals:
      Name: <cluster-name>
      <custom-tag-key1>: <custom-tag-val1>
      <custom-tag-key2>: <custom-tag-val2>
    ```

    The `Name` tag in the `tag_key_vals` is mandatory to create an identifier for the instances. More tags can be added if needed but are optional.

    In your terminal, you will likely also need to add your private key to an ssh agent:

    ```bash
    ssh-add </path/to/my.pem>
    ```

  * ####Launch EC2 instances:
    
    ```bash
    ~$ ansible-playbook ./ec2.yml --extra-vars "vars_file=./example_ec2_vars.yml" --tags launch
    ```
  * ####Stop EC2 instances:
  
    ```bash
    ~$ ansible-playbook ./ec2.yml --extra-vars "vars_file=./example_ec2_vars.yml" --tags stop 
    ```
  * ####Start EC2 instances:
  
    ```bash
    ~$ ansible-playbook ./ec2.yml --extra-vars "vars_file=./example_ec2_vars.yml" --tags start 
    ```
  * ####Terminate EC2 instances:
  
    ```bash
    ~$ ansible-playbook ./ec2.yml --extra-vars "vars_file=./example_ec2_vars.yml" --tags terminate
    ```

* ###Zookeeper
  For Zookeeper playbook, a `zookeeper_tag` needs to be specified to identify the nodes in the cluster. This `zookeeper_tag` can be any tag specified in `tag_key_vals` in the variable file for [EC2]( while launching EC2 instances.

  The `zookeeper_tag` is specifed as `<key>_<value>` for one of the `tag_key_vals` to be used. For example, if the `<cluster-name>` in the [EC2 variable file](example_ec2_vars.yml) mentioned above was `test-cluster`, the `zookeeper_tag` would be specified as `zookeeper_tag=Name_test-cluster`. It doesn't have to be the `Name` tag but could be any key value pair in `tag_key_vals` specified as `zookeeper_tag=<key>_<value>`.

  * ####Install Zookeeper:

    ```bash
    ~$ ansible-playbook ./zookeeper.yml --extra-vars "zookeeper_tag=<cluster_tag>" --tags install
    ```
  * ####Start Zookeeper:

    ```bash
    ~$ ansible-playbook ./zookeeper.yml --extra-vars "zookeeper_tag=<cluster_tag>" --tags start
    ```
  * ####Get info about Zookeeper on the specified cluster:

    ```bash
    ~$ ansible-playbook ./zookeeper.yml --extra-vars "zookeeper_tag=<cluster_tag>" --tags info
    ```
  * ####Stop Zookeeper:

    ```bash
    ~$ ansible-playbook ./zookeeper.yml --extra-vars "zookeeper_tag=<cluster_tag>" --tags stop 
    ```
  * ####Uninstall Zookeeper:

    ```bash
    ~$ ansible-playbook ./zookeeper.yml --extra-vars "zookeeper_tag=<cluster_tag>" --tags uninstall
    ```

* ###Kafka
  Kafka has a dependency on Zookeeper for cluster membership, topic configuration, data partition, etc. For Kafka playbook, a `zookeeper_tag` and a `kafka_tag` needs to be specified to identify the nodes in the zookeeper and kafka cluster respectively. The `kafka_tag` and `zookeeper_tag` can be any tag specified in `tag_key_vals` in the [variable file for EC2](#variable-file).

  The `kafka_tag` and `zookeeper_tag` are specifed as `<key>_<value>` for one of the `tag_key_vals` to be used. For example, if the `<cluster-name>` in the [EC2 variable file](#variable-file) mentioned above was `test-cluster` and we had same cluster for Zookeeper and Kafka, the `kafka_tag` and `zookeeper_tag` would be specified as `zookeeper_tag=Name_test-cluster` and `kafka_tag=Name_test-cluster` respectively. Both Zookeeper and Kafka don't have to be on the same cluster and it doesn't have to be the `Name` tag but it could be any key value pair in `tag_key_vals` specified as `zookeeper_tag=<key>_<value>` and `kafka_tag=<key>_<value>`.

  ####Kafka's dependency on Zookeeper

  Kafka's dependency on Zookeeper is taken care of by the Kafka playbook. If you are trying to ssetup Kafka on the cluster specified by `kafka_tag`, the playbook will check that Zookeeper is installed on the cluster `zookeeper_tag` and if it is not setup, the playbook will first setup Zookeeper and then Kafka. By default, any operation on Kafka cluster, like `start`, `install`, etc., will first be executed on the Zookeeper cluster. However, we would want some of the operations to be executed on the Kafka cluster, like `stop`, `uninstall`, etc., not be executed on the Zookeeper cluster. This can be achieved by specifying a flag `--skip-tags zookeeper` while running the Kafka playbook. Examples for this behavior are shown below in the `stop` and `uninstall` operations.
  

  * ####Install Kafka:

    ```bash
    ~$ ansible-playbook ./kafka.yml --extra-vars "zookeeper_tag=<cluster_tag> kafka_tag=<cluster_tag>" --tags install
    ```
  * ####Start Kafka:

    ```bash
    ~$ ansible-playbook ./kafka.yml --extra-vars "zookeeper_tag=<cluster_tag> kafka_tag=<cluster_tag>" --tags start
    ```
  * ####Get info about Kafka on the specified cluster:

    ```bash
    ~$ ansible-playbook ./kafka.yml --extra-vars "zookeeper_tag=<cluster_tag> kafka_tag=<cluster_tag>" --tags info
    ```
  * ####Stop Kafka:

    ```bash
    ~$ ansible-playbook ./kafka.yml --extra-vars "zookeeper_tag=<cluster_tag> kafka_tag=<cluster_tag>" --tags stop --skip-tags zookeeper
    ```
  * ####Uninstall Kafka:

    ```bash
    ~$ ansible-playbook ./kafka.yml --extra-vars "zookeeper_tag=<cluster_tag> kafka_tag=<cluster_tag>" --tags uninstall --skip-tags zookeeper

    ```

 *  #### Vowpal Wabbit   

Vowpal Wabbit is a fast out-of-core Machine Learning system. Installation can take upwards of 10 minutes on micro instances, as it compiles a lot of C++ with high optimization levels using Clang. 

  * ####Install Vowpal Wabbit:

    ```bash
    ~$ ansible-playbook ./vw.yml --extra-vars "vw_tag=class_vw" --tags install
    ```

