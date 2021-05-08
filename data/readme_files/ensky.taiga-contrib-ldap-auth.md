Taiga contrib ldap auth
=======================

The Taiga plugin for ldap authentication.

Installation
------------

### Taiga Back

In your Taiga back python virtualenv install the pip package
`taiga-contrib-ldap-auth` with:

```bash
  pip install taiga-contrib-ldap-auth
```

Modify your settings/local.py and include it on `INSTALLED_APPS` and add your
LDAP configuration:

```python
  INSTALLED_APPS += ["taiga_contrib_ldap_auth"]

  LDAP_SERVER = 'ldap://ldap.example.com'
  LDAP_PORT = 389

  # Full DN of the service account use to connect to LDAP server and search for login user's account entry
  # If LDAP_BIND_DN is not specified, or is blank, then an anonymous bind is attempated
  LDAP_BIND_DN = 'CN=SVC Account,OU=Service Accounts,OU=Servers,DC=example,DC=com'
  LDAP_BIND_PASSWORD = 'replace_me'   # eg.
  # Starting point within LDAP structure to search for login user
  LDAP_SEARCH_BASE = 'OU=DevTeam,DC=example,DC=net'
  # LDAP property used for searching, ie. login username needs to match value in sAMAccountName property in LDAP
  LDAP_SEARCH_PROPERTY = 'sAMAccountName'
  LDAP_SEARCH_SUFFIX = None # '@example.com'

  # Names of LDAP properties on user account to get email and full name
  LDAP_EMAIL_PROPERTY = 'mail'
  LDAP_FULL_NAME_PROPERTY = 'name'
```

The logic of the code is such that a dedicated domain service account user performs a search on LDAP for an account that has a LDAP_SEARCH_PROPERTY value that matches the username the user typed in on the Taiga login form.  
If the search is successful, then the code uses this value and the typed-in password to attempt a bind to LDAP using these credentials.
If the bind is successful, then we can say that the user is authorised to log in to Taiga.

Optionally LDAP_SEARCH_SUFFIX can be set to allow for the search to match only the beginning of a field containing e.g. an email address.

If the LDAP_BIND_DN configuration setting is not specified or is blank, then an anonymous bind is attempted to search for the login user's LDAP account entry.


RECOMMENDATION: Note that if you are using a service account for performing the LDAP search for the user that is logging on to Taiga, for security reasons, the service account user should be configured to only allow reading/searching the LDAP structure. No other LDAP (or wider network) permissions should be granted for this user because you need to specify the service account password in this file.
A suitably strong password should be chosen, eg. VmLYBbvJaf2kAqcrt5HjHdG6



### Taiga Front

Change in your dist/js/conf.json the loginFormType setting to "ldap":

```json
...
    "loginFormType": "ldap",
...
```
