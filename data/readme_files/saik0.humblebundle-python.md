humblebundle-python
===================

humblebundle-python is an unofficial library for querying the undocumented Humble Bundle API.


Usage
-----
Basic usage looks something like::

    client = humblebundle.HumbleApi()
    
    client.search_store("ftl")
    
    client.login("username@example.com", "secret")
    
    gamekeys = client.get_gamekeys()
    
    for gamekey in gamekeys:
        order = client.get_order(gamekey)
        for subproduct in order.subproducts:
            print(subproduct)

See examples.py for more examples

humblebundle-python is not affiliated in any way with Humble Bundle, Inc.
