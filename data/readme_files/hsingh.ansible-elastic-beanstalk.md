elastic_beanstalk
=========

Ansible modules for working with Amazon Elastic Beanstalk

Requirements
------------

This module requires [boto3](https://github.com/boto/boto3) and Ansible >= 2.0


Versioning
------------

Module version 2.X (master branch) requires boto3 and Ansible >= 2.0. Module
version 1.X (release-1.0 branch) requires [boto](https://github.com/boto/boto)
and works with Ansible < 2.0.


Example Playbook
----------------

The example playbook demonstrates how to create an application and version and update an existing environment.

    ---
    - hosts: localhost
      connection: local
      gather_facts: False

      tasks:

      - name: Create Elastic Beanstalk application
        elasticbeanstalk_app:
          region: us-east-1
          app_name: Sample App
          description: "Sample App Description"
          state: present
        register: app


      - name: Create application version
        elasticbeanstalk_version:
          region: us-east-1
          app_name: Sample App
          version_label: Sample Version
          s3_bucket: sample-app-versions-bucket
          s3_key: sample-version-1.0.0.zip
          state: present
        register: version


      - name: Create appo
        elasticbeanstalk_env:
          region: us-east-1
          app_name: Sample App
          env_name: sampleApp-env
          version_label: Sample Application
          solution_stack_name: "64bit Amazon Linux 2014.09 v1.2.1 running Docker 1.5.0"
          option_settings:
            - Namespace: aws:elasticbeanstalk:application:environment
              OptionName: PARAM1
              Value: bar
            - Namespace: aws:elasticbeanstalk:application:environment
              OptionName: PARAM2
              Value: foobar
        register: env


License
-------

MIT

Author Information
------------------

[Harpreet Singh](http://about.me/hs)
