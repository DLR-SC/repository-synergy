[swganh][1] - an open source Star Wars Galaxies Publish 14.1 server emulator
=======================================================================

This project aims to recreate the Star Wars Galaxies Pre-Combat Upgrade experience as it was during Publish 14.1. In addition it serves as a playground for experimenting with new ideas for MMORPG server architecture, for more information see the [online documentation][2].

## Quick Build Guide ##

### Requirements ###

*   Microsoft Visual Studio 11.0 Beta or higher (windows)
*   GCC 4.6 (*nix)
*   CMake 2.8.7 or higher
*   Git 1.7 or higher
*   Python 3.2
*   MySQL 5.1/MariaDB 5.2 or higher

### Visual Studio / Windows Development ###

Use git to checkout the latest version of the source:

    git clone https://github.com/anhstudios/swganh.git

Next, download the latest dependencies package for Visual Studio 11 here: 

https://github.com/anhstudios/swganh/downloads

Extract this inside of the swganh repository you just cloned:

    ie., C:\swganh\vendor

Shift-right click and choose to "Open command window here" on the swganh directory.

Run the following commands to generate the project and build the source.

    mkdir build
    cd build
    cmake -G "Visual Studio 11" ..
    cmake --build .

This will kick off a full build of the project. The final output can be found at swganh/build/bin/(Configuration).

* **NOTE** Since the project files are located outside the source directory adding new files from within visual studio requires changing the default save location.*

To add a new file, manually create it in the src directory and then run the following from within the build directory.
    
    cmake ..


### GCC / Linux Development ###

On linux platforms a minimum of GCC 4.6 is required to build the project. After running the bootstrap script as outlined in the Quick Build Guide change directories to the **build** directory. You can use your favorite text editor to edit source files, the project can be rebuilt using familiar gnu make commands.

    git clone https://github.com/anhstudios/swganh.git
    cd swganh
    mkdir build
    cd build
    cmake ..
    make
    
A more complete set of instructions that covers building dependencies can be found in the official documentation.

### Clang and other compilers ###

[Clang][3] does not yet support lambdas, a C++0x feature commonly used in this project. Once lambda support is available we will investigate officially adopting it as a supported compiler. 

## Quick Links ##

*   **[Online Documentation][2]**

[1]: http://swganh.com
[2]: http://swganh.com/anh_docs
[3]: http://clang.llvm.org/
