docker-ebs-attach
==============

Docker container that attaches an EBS volume to the local ec2 instance. Detaches volume on exit.

Usage: 

```
docker run -it --rm leg100/ebs-attach \
--volumeid vol-123123 \
--device /dev/xvdf \
--region eu-west-1
```

Note: it relies on the ec2 instance possessing an IAM profile with the following privileges:

 - ec2:AttachVolume
 - ec2:DetachVolume
 - ec2:DescribeVolumes
