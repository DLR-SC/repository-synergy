.. raw:: html

   <!--
   Copyright 2015-2019 F5 Networks Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   -->

Ansible F5
==========

|slack badge| |travis badge| |shippable badge|

Introduction
------------

This repository provides the foundation for working with the F5 Modules for Ansible.
The architecture of the modules makes inherent use of the BIG-IP REST APIs as well as the tmsh API where required.

This repository is an **incubator** for Ansible modules. The modules in this repository **may be
broken due to experimentation or refactoring**.

The F5 Modules for Ansible are freely provided to the open source community for automating BIG-IP device configurations.

If you want to download the stable modules, please install latest collection release found on galaxy: |f5_collection|.


Collections Daily Build
-----------------------

We offer a daily build of our most recent collection |dailybuild|. Please use this Collection to test the most
recent Ansible module updates between releases.

Installing the Daily Build
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: shell

    ansible-galaxy collection install <collection name> -p ./collections
    e.g.
    ansible-galaxy collection install f5networks-f5_modules-1.0.0-devel.tar.gz -p ./collections

.. note::

   "-p" is the location in which the collection will be installed. This location should be defined in the path for
   ansible to search for collections. An example of this would be adding ``collections_paths = ./collections``
   to your **ansible.cfg**

Support
-------
F5 supports the F5 modules delivered in |ansible_distro|. Please refer to the |support_policy| for details.

Bugs, Issues
------------

Please file any bugs, questions, or enhancement requests by using |ansible_issues|. For details, see |ansiblegethelp|.

Documentation
-------------

All documentation is available on |ansiblehelp|.

Your ideas
----------

What types of modules do you want created? If you have a use case and can sufficiently describe the behavior you want to see, open an issue and we will hammer out the details.

If you've got the time, consider sending an email that introduces yourself and what you do. We love hearing about how you're using the F5 Modules for Ansible.

- Wojciech Wypior and the F5 team - solutionsfeedback@f5.com

Copyright
---------

Copyright 2017-2019 F5 Networks Inc.


License
-------

GPL V3
~~~~~~

This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work.

See `License`_.


.. |travis badge| image:: https://travis-ci.com/F5Networks/f5-ansible.svg?branch=devel
    :target: https://travis-ci.com/F5Networks/f5-ansible
    :alt: Build Status

.. |slack badge| image:: https://f5cloudsolutions.herokuapp.com/badge.svg
    :target: https://f5cloudsolutions.herokuapp.com
    :alt: Slack Status

.. |shippable badge| image:: https://api.shippable.com/projects/57c88ded5a5c0d0f0012c53e/badge?branch=devel
    :target: https://app.shippable.com/github/F5Networks/f5-ansible
    :alt: Shippable Status

.. _License: https://github.com/F5Networks/f5-ansible/blob/devel/COPYING


.. |dailybuild| raw:: html

   <a href="https://f5-ansible.s3.amazonaws.com/collections/f5networks-f5_modules-1.2.0-devel.tar.gz" target="_blank">here</a>

.. |f5_collection| raw:: html

   <a href="https://galaxy.ansible.com/f5networks/f5_modules" target="_blank">F5 Ansible Modules Collection</a>

.. |ansible_distro| raw:: html

   <a href="https://pypi.org/project/ansible/" target="_blank">Red Hat Ansible distributions</a>

.. |support_policy| raw:: html

   <a href="https://f5.com/support/support-policies" target="_blank">F5 Ansible Support Policy</a>

.. |ansible_issues| raw:: html

   <a href="https://github.com/F5Networks/f5-ansible/issues" target="_blank">Github Issues</a>

.. |ansiblehelp| raw:: html

   <a href="http://clouddocs.f5.com/products/orchestration/ansible/devel/" target="_blank">clouddocs.f5.com</a>

.. |ansibleguidelines| raw:: html

   <a href="http://clouddocs.f5.com/products/orchestration/ansible/devel/development/guidelines.html" target="_blank">Guidelines</a>

.. |ansiblegethelp| raw:: html

   <a href="http://clouddocs.f5.com/products/orchestration/ansible/devel/usage/support.html" target="_blank">Get Help</a>


