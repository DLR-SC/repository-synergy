Cassandra-tools
=========================

This repository is a collection of automation scripts that allow you to launch and test different Cassandra configurations. You can have multiple profiles to test against to see the difference in performance between an 8GB heap and a 12GB heap for example, or making multiple changes to a yaml file vs a control cluster to see if performance or stability improved with your changes. 

Cassandra tools pulled a lot of bootstrapping and node configuration from the DataStax AMI Builder tool and simplified it via Fabric so that you have more control over the changes you want to make to your cluster and giving you a clear view on what is going on. 

The topology that would be recommended would be something as seen below. Where you have a dedicated node running opscenter that can be static and separate instances of stress and C*

![Topology](https://dl.dropboxusercontent.com/u/9507712/cassandra/topology.png)


  
Bootsrapping a cluster supports:

- Mounting and formatting Drives using XFS 
- RAID0 for testing the i2 series of instance types

Workflow
=========

The basic workflow is as follows:
 
1. Launch a machine and install Opscenter 
2. Launch and bootstrap a cluster of C* nodes
3. Launch and bootstrap several stress runner nodes
4. Run stress yaml files against the cluster and monitor

Pre-Reqs
================

All of these scripts expect you to have the requirements installed from requirements.txt To do that simply type from the root directory

    pip install -r requirements.txt
    


Since this is for AWS it's expected that you have your keys exported in your shell for auth. 

    export AWS_ACCESS_KEY_ID=YOURKEY
    export AWS_SECRET_ACCESS_KEY=YOURSECRET


#### Ubuntu Note ####
you may need to install python dev tools to get pycrypto working

    sudo apt-get install python-dev


Launching
================

Now let's get to launching. It's assumed that you have an AMI you want to use as your base. It can just be a base Ubuntu AMI from the AWS console for example. Once you have that AMI you'll need to configure a launch json file that has the ami id, security groups you want applied, tags, launch key, etc... so launcher.py knows how to build your instances. 

Take a look at the configs/*.sample files for examples of where to plug your information in. This also assumes you're in a VPC. If you're not feel free to submit a pull request to support non VPC launching or just launch your nodes via the AWS console or CLI. Launcher does nothing fancy and doesn't bootstrap anything. It just provisions instances, which you can do yourself via the AWS console. 

Copy a profile sample to work with

    cd launcher/configs/
    cp c4-highperf.json.sample c4-highperf.json
    

Now edit that profile with your AMI ID to use, tags you want on the instances, security groups, subnets to launch in, etc...

You can see the AMI ID in this screenshot as ami-d05e75b8

![AMI](https://dl.dropboxusercontent.com/u/9507712/cassandra/ami.png)

Assuming you're using the launcher script, let's fire up 3 nodes in us-east-1a using the c4-highperf profile that you created from a .sample file. 

    cd launcher/
    python launch.py launch --nodes=3 --config=c4-highperf --az=us-east-1a
 

You can repeat the process across AZ's as needed to get the final cluster topology squared away. At the end of that output you'll see  a list of IPs that it provisioned. Copy those down for future use. 

Managing
================

### Creating a Profile ###

The first step in the process will be to use one of the sample profiles to base a new profile you want to test. 

    cd manage/configs
    cp -rf c4-highperf-sample c4-highperf
   
 

More docs to come on this but for now go through the files in that directory and change the 10.10.10.XX ips to ones in your environment. e..g in address.yaml put in your opscenter IP address

Files of interest:

* address.yaml the IP address to where your opscenter node is for reporting
* cassandra-env.sh contains the startup params, GC settings for config
* cassandra.yaml contains the properties used to control various C* settings
* collectd.conf if you want to use collectd to monitor via graphite, put your graphite ip in there
* hostfile.txt contains all the IP address for the nodes you want to manage
* metrics.yaml if you're reporting to graphite, send C* metrics over with a whitelist 


NOTE: For EBS volumes it's expected you mount your drives in specific locations. e.g. commit drive goes to /dev/sdk(xvdf) and data drive goes to /mnt/sdf(xvdf) or as seen below

![EBS](https://dl.dropboxusercontent.com/u/9507712/cassandra/ebs.png)


Once you have your cluster up and running you're now ready to bootstrap and provision it. The manager file expects your list of ips to be newline separated and in configs/yourconfig/hostfile.txt

Place all of your IP address in that file. 

### Bootstrapping/Provisioning ###

To test out your running system (assuming you ran the pip install -r requirements.txt cmd above)

    fab -u ubuntu  bootstrapcass21:config=c4-highperf

That command will run all the apt-get update/installs, install java, format the EBS volume using XFS, turn off swap, etc.... One thing to note is that the fab command will always prompt you as to which hostfile you want to run. There are times you just want to bootstrap a few nodes and not the whole cluster. So you can just put those ips anywhere like /tmp/newips.txt and use type in that file in the prompt instead. 

Note that at time of writing it installs Cassandra Community version 2.1.9, if you're bored, submit a PR to make that configurable from the profile :)

Once that is complete you'll want to set your seed nodes for that cluster. So pick one IP or a comma separated list and run

    fab -u ubuntu  set_seeds:config=c4-highperf,seeds='10.10.100.XX'


Once you have your seeds set up now we can start up Cassandra
    
    fab -u ubuntu  start_cass:config=c4-highperf

At this point you should login to one or all of the instances and just do a headcheck in /var/log/cassandra/system.log to ensure everything started up ok. If you want to do a quick check on what nodes are running Cassandra you can use the getrunning task

    fab -u ubuntu  getrunning:config=c4-highperf


For a list of all the commands available you can ask fab to list the tasks

    fab -l
    

Other common tasks will be changing yaml files or cassandra-env settings for testing different GC combinations. For that you would make your changes, save the files and run

    fab -u ubuntu  configs:config=c4-highperf
    

You can also use the free form cmd task. For example, want to see all the java versions across your cluster?

    fab -u ubuntu cmd:config=c4-highperf,cmd="java -version 2>&1 | grep version  | awk '{print \$NF}'"
    
Or see how much "MAX HEAP SIZE" your nodes are configured for

    fab -u ubuntu cmd:config=c4-highperf,cmd="grep MAX_HEAP_SIZE /etc/cassandra/cassandra-env.sh | grep G"
    
The cmd task runs in parallel so going over 60+ nodes is within seconds. 

Running Stress
--------

This repo also has support for running your stress machines. The workflow I was using was the following
1. Launch stress instances
2. Set hostfile.txt in stress/hostfile.txt with the IP address of stress machines
3. Bootstrap stress machines with stress 2.1 code and yaml files
4. Use csshX to view all the stress machines in multiple terminals
5. Tweak yaml files and re-push stress to test various configs

A note on stress is that there is a 70MB compiled stress tarball included so rather than push that up on every node I'll run

    fab -u ubuntu installstress
    
which will install stress on a single node (if just one is in your hostfile) then create an AMI of that node to launch more stress boxes to make things a bit faster. 


### csshX ###

csshX is a neat little program that will allow you run the same command across multiple terminal windows simultaneously. 

You can find it here: https://github.com/brockgr/csshx
or install on OSX with 

    brew install csshx

![csshX view](http://www.brock-family.org/gavin/macosx/csshX.png)


to fire up csshX just type in

    csshX --login ubuntu `cat ../stress/hostfile.txt`
    
that will bring up the pane of stress machines, alt+tab if you don't see it right away and find the terminal windows. 


### Bootstrapping Stress Nodes ####

to install stress and the base yaml files, you can run

    fab -u ubuntu installstress
    
that will install all the base code needed to run stress. If you make changes to the yaml files or add new ones and profiles you can use what's below to just push those changes

    fab -u ubuntu  putstress


Once the files are uploaded you're ready to run stress. Using csshX in the red area that controls the output to all terminals you can type in

    python runstress.py --profile=stress --seednode=10.10.10.XX --nodenum=1


That will run the following cmd under the covers

    /home/ubuntu/apache-cassandra-2.1.5/tools/bin/cassandra-stress user duration=100000m cl=ONE profile=/home/ubuntu/summit_stress.yaml ops\(insert=1\) no-warmup  -pop seq=1..100000000 -mode native cql3 -node 10.10.10.XX -rate threads=1000  -errors ignore
    

Type python runstress.py -h 
for all the available options to pass like threads, seednode, etc...

Place the correct IP there and you should be running stress against your new cluster. Dig around the runstress.py file to see what other profiles you can run, or add your own. 

