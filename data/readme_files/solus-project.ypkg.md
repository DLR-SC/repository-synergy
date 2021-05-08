ypkg2
-----

**Modern, declarative, structured build format**


ypkg is the build tool of choice for Solus. Simply put, it is a tool to convert a build process into a packaging operation.

ypkg evolved from a basic set of ideas within the Solus project, that packaging should be simple. Given rules should be obeyed globally, and where appropriate the packager should be able to tweak the results to how they desire.

As a result, `ypkg` provides a highly intuitive, simple, yet incredibly powerful package building system, which follows the Solus philosophy of sane defaults, and hidden power under the surface. `ypkg` is capable of many build types, multilib, automatic & intelligent package splitting, choice compiler optimisations, standardised `GDB`-compatible `debuginfo` packages, automatic dependency resolution, and much more.

`ypkg` is a [Solus project](https://solus-project.com/).

![logo](https://build.solus-project.com/logo.png)

**How Rules Work:**

Everything in ypkg can be traced to a *pattern*. We use these to define what part of a package, or sub-package, a file should be placed in. To enforce consistency, we have our own in-built patterns, i.e.:

    /usr/lib64/lib*.so   = devel subpackage
    /usr/lib64/lib*.so.* = "main" package

There are many in-built patterns which designate how the subpackages should be emitted, allowing for self resolving dependency graphs:

    dev: depends on "main":
        /usr/lib64/pkgconfig/*.pc
        /usr/lib64/lib*.so
    dev: also depends on whatever the pkgconfig files depend on

    main: shared library dependencies:
        /usr/lib64/lib*.so.*

However, sometime's it is desirable to split up a package. Consider this example:

    main:
        /usr/lib64/libpoppler-glib.so.*
        /usr/lib64/libpoppler-qt5*.so.*
    devel:
        /usr/lib64/lib*.so

The automatic behaviour would by default make the main package gain a dependency on the `qt5` package, through direct binary dependencies. This can be very undesirable and would cause unnecessary bloat in lighter systems.

The solution, therefore, is to do the following:

    main:
        /usr/lib64/lib*.so.*
    devel:
        /usr/lib64/lib*.so
        /usr/lib64/pkgconfig/*.pc

    qt5:
        /usr/lib64/libpoppler-qt5*.so.*
    qt5-devel:
        /usr/lib64/libpoppler-qt5*.so
        /usr/lib64/pkgconfig/poppler-qt5.pc

Dependency Handling
-------------------

ypkg formulates many of the dependencies on an automatic basis, even on your own custom patterns. Listed below are the supported types.

**Direct Dependency**

When building the package we first analyze all ELF dynamic objects to determine both exported SONAMEs and _direct dependencies_ on shared libraries. We initially filter out dependencies on internal sonames to ensure a package doesn't gain an unnecessary *external* dependency.

These are validated against provided rpaths in the objects as well as against the global symbol table.

In the instance the dependency is provided externally, it will be sought out externally via a combination of the linker paths and the soname.

**SOLINK**

Typically when splitting packages, we provide the `.so` symbolic link in the `-devel` pattern. To alleviate the need for manually describing this dependency graph, we automatically detect resolvable solinks in the current build tree in order to place a dependency on the providing package.

In the instance of libpopplet-qt5.so, in the `qt5-devel` package, this resolves to `libpoppler-qt5.so.1.3.0` in the `-qt5` package, thus a solink dependency is added automatically.

**PkgConfig**

Ypkg exports two kinds of pkgconfig providers: `PkgConfig` and `PkgConfig32`. This allows for correct dependency chaining in `emul32` build scenarios. In short, a pkgconfig() provider becomes a pkgconfig32() provider when it is in the /usr/lib32 tree.

Much as with soname resolution, we scan pkg-config dependencies in `-devel` type packages against a global provider table. Using again the `poppler-qt5` example, this pkgconfig file expresses a dependency on `poppler`, which is provided by the `poppler-devel` package. In turn, `poppler` pkgconfig has dependencies on `cairo`, which is resolved to an external package dependency.

All in all, we formulate a self resolving dependency graph through entirely logical rules and splitting, without having to construct them ourselves.

    poppler-qt5-devel:
        poppler-qt5 ->
            poppler
                -> cairo, etc.
        poppler-devel ->
            poppler
                -> cairo, etc

As such, this makes `pkgconfig()` build dependencies very powerful, as using `pkgconfig(poppler-qt5)` grabs *everything* necessary for use, and nothing more. Note also in Solus we implement the equivalent of `-Wl,--as-needed` at the toolchain level itself, in order to ensure we only need to deal with absolutely required dependencies.

`emul32` packages
-----------------

To build a package in a multilib fashion, simply set the `emul32` key to `yes`. This will cause the build steps to double up, the first run will build as a 32-bit build, and the second set will be the native 64-bit set.

Build dependencies for 32-bit packages can expressly be 32-bit pkgconfig dependencies, i.e:

    pkgconfig32(zlib)

`ypkg` will automatically add the following build dependencies for `emul32` builds, to save the developer extra effort:


    - glibc-32bit-devel
    - libgcc-32bit
    - libstdc++-32bit

Note that 32-bit builds are done *first*, in a separate build root to the native 64-bit package. However they will both install to the same tree. Note that for `emul32` packages, we use `--prefix=/emul32 --libdir=/usr/lib32`. This avoids collisions of binaries and assets, but you may need to tweak to your requirements.

Utilising Profile Guided Optimization
-------------------------------------

Packages wishing to make use of PGO will require multiple build steps. In short, a package must provide a valid *workload* to generate PGO data. The steps are as follows:

    - setup: (unpack roots, clean trees, run `setup` step with PGO GEN flags)
    - build
    - profile (Run the actual `profile` step)
    - setup (unpack and clean again, use PGO USE flags)
    - build
    - install
    - check

Basically, provide a `profile` step to run the workload after the *first* build, and `ypkg` will take care of the necessary ordering and environmental overrides.

License
-------

GPL-3.0

Copyright © 2015-2017 Ikey Doherty

Some portions: Copyright (C) 2016 Intel Corporation

Some elements have been gratefully borrowed from autospec:

https://github.com/clearlinux/autospec
