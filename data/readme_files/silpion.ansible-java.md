# silpion.java

Install Oracle Java.

# Synopsis

```yaml
- name: Install Java 8u102 JDK to /opt/java
  hosts: all
  roles:
    - role: silpion.java
```

```yaml
- name: Install Java server-jre to /usr/local/java
  hosts: all
  roles:
    - role: silpion.java
      java_oracle_distribution: srv
      java_install_dir: /usr/local/java
```

```yaml
- name: Install Java JRE 8u60
  hosts: all
  roles:
    - role: silpion.java
      java_oracle_version: 8u60
      java_oracle_distribution: jre
```

# Description

The role downloads redistributable packages from the internet
to the hosts local filesystem before it may install those on
any number of managed nodes in the local network.

Downloads are performed with the ``command`` module using ``curl``.
It is required to have curl installed on the local host you
are running ansible-playbook on to manage nodes (your workstation).

Downloaded assets are verified based on SHA 256 checksums on
the local workstation before getting copied to the managed node.

The local shasum binary is guessed automatically but may get
configured via ``java_shasum_binary: /path/to/shasum/binary``.

For detailed configuration options see [Role Variables](#role_variables)
documentation below.

# Dependencies

* [silpion.lib][1]
* [silpion.util][2]

roles. This is configured for the ``ansible-galaxy install`` command in
**requirements.yml**.

```sh
ansible-galaxy install --no-deps --role-file requirements.yml
```

# <a name="role_variables"></a>Role Variables

* ``java_oracle_distribution``: Configure the Java distribution to be installed (default: ``jdk``, values: [``jdk``, ``jre``, ``srv``])
* ``java_oracle_version``: Configure Java version to be installed (string, default: ``8u66``)
* ``java_install_dir``: Base installation directory for any Java implementation/distribution (string, default: ``/opt/java``)
* ``java_shasum_binary``: Allows to configure shasum binary for local\_action: command (string, default: ``with_first_found: java_shasum_binaries`` (see ``vars/main.yml``))
* ``java_path_to_lib_role``: configure path to lib-role, which can get configured via silpion.lib role (string, default: ``{{ lib_roles_path }}``)

Note: ``srv`` is an Ansible compatible shorthand for the Oracle ``server-jre``.

## Versioned variables

Predefined SHA sums and further version specific configuration may get found in
the ``vars/versions`` directory. When configuring a version, that is not predefined
(so far), the following variables must also be defined in the playbook:

* ``java_oracle_version_major``: Oracle major version
* ``java_oracle_version_minor``: Oracle minor version
* ``java_oracle_version_patch``: Oracle patch version
* ``java_oracle_version_update``: Oracle major version
* ``java_oracle_version_build``: Oracle build version
* ``java_oracle_redis_jdk_sha256sum``: SHA256 sum for the downloaded Oracle Java JDK redistributable package - mandatory when ``java_oracle_distribution`` is ``jdk``
* ``java_oracle_redis_jre_sha256sum``: SHA256 sum for the downloaded Oracle Java JRE redistributable package - mandatory when ``java_oracle_distribution`` is ``jre``
* ``java_oracle_redis_srv_sha256sum``: SHA256 sum for the downloaded Oracle Java Server-JRE redistributable package - mandatory when ``java_oracle_distribution`` is ``srv``
* ``java_oracle_redis_jce_sha256sum``: SHA256 sum for the downloaded Oracle Java JCE policies package
* ``java_oracle_mirror_jce``: Mirror URL for the download of the Oracle Java JCE policies package
* ``java_oracle_redis_jce_filename``:  File name of the Oracle Java JCE policies package
* ``java_oracle_redis_jce_archive_dirname``: Name of the base directory in the Oracle Java JCE policies package

## Supported versions

* 7u21
* 7u51
* 7u71
* 7u80
* 8u20
* 8u25
* 8u31
* 8u45
* 8u51
* 8u60
* 8u65
* 8u66
* 8u92
* 8u101
* 8u102

Starting with

* ``7u80`` (Java 7)
* ``8u66`` (Java 8)

configuration of ``java_oracle_distribution``: ``srv`` is available.

# Role facts

This role sets persistent facts for other roles to use via

* facts.d ``ansible_local.java.general.java_home``

This variable contains the path to the default JVM configured with this role.

# Checkmode

Checkmode is supported provided that all assets have been downloaded.
Otherwise, the copy tasks will fail.

You can download the assets without making any changes on the remote nodes by executing this role with the ``java_download`` tag.

# Contributing

If you want to contribute to this repository please be aware that this
project uses a [gitflow](http://nvie.com/posts/a-successful-git-branching-model/)
workflow with the next release branch called ``next``.

Please fork this repository and create a local branch split off of the ``next``
branch and create pull requests back to the origin ``next`` branch.

# License

Apache Version 2.0

# Author

* Mark Kusch @mark.kusch silpion.de
* Marc Rohlfs @marc.rohlfs silpion.de
* Alvaro Aleman @alvaro.aleman silpion.de

## Contributors

* Lars Maehlmann @lars.maehlmann silpion.de
* Sebastian Davids @sebastian.davids silpion.de
* [ludovicc](https://github.com/ludovicc)
* [nixlike](https://github.com/nixlike)
* [trumant](https://github.com/trumant)



[1]: https://github.com/silpion/ansible-lib
[2]: https://github.com/silpion/ansible-util


<!-- vim: set ts=4 sw=4 et nofen: -->
