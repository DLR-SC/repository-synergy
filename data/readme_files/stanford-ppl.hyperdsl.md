hyperdsl
=====
This is a repository containing all of the latest code dependencies for the Delite Compiler Framework, an interactive framework to rapidly and effeciently create DSL's.  

Three repositories are submodules in this framework.  See each individual repository for further detail:

1) Forge: https://github.com/stanford-ppl/Forge

2) Delite: https://github.com/stanford-ppl/Delite

3) LMS: https://github.com/TiarkRompf/virtualization-lms-core

Installation
============

    cd hyperdsl
    git submodule update --init
    sbt compile

Updating Existing Repo to Latest Commits
============

    cd hyperdsl
    git pull
    git submodule update
    sbt compile

Environment Variables
============
sbt and several other scripts require the following environment variables to be set:

    HYPER_HOME: hyperdsl repository home directory
    LMS_HOME: virtualization-lms-core repository home directory
    DELITE_HOME: Delite repository home directory
    FORGE_HOME: Forge repository home directory
    JAVA_HOME: JDK home directory

init-env.sh contains the sensible defaults for all of these paths except JAVA_HOME

More Information
============
The hyperdsl repository points to a specific commit of each of the three repositories above that are known to work with each other.  If you 'cd' into any of these repositories and enter `git status` you will notice this.  If you want to checkout a specific branch of a submodule you can do so and operate on that branch in a normal fashion.  Please see http://blog.jacius.info/git-submodule-cheat-sheet/ for more information on working with git submodules.
