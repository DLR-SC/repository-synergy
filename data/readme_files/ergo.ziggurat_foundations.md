# Ziggurat Foundations

[![Build Status]](https://travis-ci.org/ergo/ziggurat_foundations) [![logo]](https://gitter.im/ergo/ziggurat_foundations)

**DOCUMENTATION**: http://readthedocs.org/docs/ziggurat-foundations/en/latest/

**BUG TRACKER**: https://github.com/ergo/ziggurat_foundations

High level mixins for adding authorization, resource ownership and permission management
fast, simple and easy. In summary, Ziggurat Foundations is a set of framework agnostic
set of SQLAalchemy classes, so it can be used with Flask, Pyramid or other popular frameworks.
It is the perfect solution for handling complex login and user
management systems, from e-commerce systems, to private intranets or large CMS systems.
It can easily be extended to support any additional features you may need (explained
further in the documentation)

Zigg has been used (at scale) for very large implementations (millions of real users) and
has been extended for custom applications such as geo-location applications that rely
on pin-point accuracy for a users location. Zigg has been designed to work for
high end environments, where the user(s) are at the main focus of the application
(for example Zigg could become the backbone for a social media style application).

The aim of this project is to supply set of generic models that cover the most
common needs in application development when it comes to authorization - using
flat and tree like data structures. We provide most commonly needed features in a "standard"
application, but provide them as mixins as we understand that every implementation
has its own use case and in doing so, extending the base models is very easy.

Zigg supplies extendable, robust and well tested models that include:

- User - base for user accounts
- Group - container for many users
- Resource - Arbitrary database entity that can represent various object hierarchies -
  blogs, forums, cms documents, pages etc.

Zigg provides standard functions that let you:

- Assign arbitrary permissions directly to users (ie. access certain views)
- Assign users to groups
- Assign arbitrary permissions to groups
- Assign arbitrary resource permissions to users (ie. only user X can access private forum)
- Assign arbitrary resource permissions to groups
- Manage nested resources with tree service
- Assign a user o an external identity (such as facebook/twitter)
- Manage the sign in/sign out process
- Change users password and generate security codes
- Example root context factory for assigning permissions per request (framework integration)


Ziggurat Foundations is BSD Licensed

[Build Status]: https://travis-ci.org/ergo/ziggurat_foundations.svg?branch=master
[logo]: https://badges.gitter.im/ergo/ziggurat_foundations.svg
