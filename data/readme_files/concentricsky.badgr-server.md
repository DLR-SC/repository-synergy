# Badgr Server
*Digital badge management for issuers, earners, and consumers*

Badgr-server is the Python/Django API backend for issuing [Open Badges](http://openbadges.org). In addition to a powerful Issuer API and browser-based user interface for issuing, Badgr offers integrated badge management and sharing for badge earners. Free accounts are hosted by Concentric Sky at [Badgr.com](http://info.badgr.com), but for complete control over your own issuing environment, Badgr Server is available open source as a Python/Django application.

See also [badgr-ui](https://github.com/concentricsky/badgr-ui), the Angular front end that serves as users' interface for this project.

### About the Badgr Project
Badgr was developed by [Concentric Sky](https://concentricsky.com), starting in 2015 to serve as an open source reference implementation of the Open Badges Specification. It provides functionality to issue portable, verifiable Open Badges as well as to allow users to manage badges they have been awarded by any issuer that uses this open data standard. Since 2015, Badgr has grown to be used by hundreds of educational institutions and other people and organizations worldwide. See [Project Homepage](https://badgr.org) for more details about contributing to and integrating with Badgr.

## How to get started on your local development environment.
Prerequisites:

* Install docker (see [instructions](https://docs.docker.com/install/))

### Customize local settings to your environment
* `cp .docker/etc/settings_local.py.example .docker/etc/settings_local.py`
* Edit the settings_local.py file and insert local credentials for DATABASES and email, then run the following from within the `code` directory:
  * `DEFAULT_FROM_EMAIL` "noreply@localhost"
  * The default `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` will log email content to console, which is often adequate for development. Other options are available. See Django docs for [sending email](https://docs.djangoproject.com/en/1.11/topics/email/).
  * `SECRET_KEY` and `UNSUBSCRIBE_SECRET_KEY`. For each, generate a (secure random for production) string of 40 uppercase characters.
  * PAGINATION_SECRET_KEY: This key is used for symmetrical encryption of pagination cursors.  If not defined, encryption is disabled.  Must be 32 byte, base64-encoded random string.  For example: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"
  * AUTHCODE_SECRET_KEY must be 32 url-safe base64-encoded bytes. This key is used for symmetrical encryption of pagination cursors.  If not defined, encryption is disabled.  Must be 32 byte, base64-encoded random string as above.
  
#### Additional configuration options
Set these values in your settings_local.py file to configure the application to your specific needs. Required options are listed in bold.
* *HELP_EMAIL* (Required)
  - An email address for your support staff.
* BADGR_APPROVED_ISSUERS_ONLY:
  - If you choose to use the BADGR_APPROVED_ISSUERS_ONLY flag, this means new user accounts will not be able to define new issuers (though they can be added as staff on issuers defined by others) unless they have the Django user permission 'issuer.add_issuer'. The recommended way to grant users this privilege is to create a group that grants it in the `/staff` admin area and addthe appropriate users to that group.
* PINGDOM_MONITORING_ID:
  - If you use Pingdom to monitor site performance, including this setting will embed Pingdom tracking script into the header.
* CELERY_ALWAYS_EAGER = True
  - Celery is an asynchronous task runner built into Django and Badgr. Advanced deployments may separate celery workers from web nodes for improved performance. For development environments where Celery tasks should run synchronously, set this flag to true. Very few time-intensive tasks are part of this repository, and eager is a safe setting for most production deploys.
* OPEN_FOR_SIGNUP = True
  - This defaults to True, but allows you to turn off signup if you would like to use Badgr for only single-account use or to manually create all users in `/staff`. UX is not well-supported.
* `DEFAULT_FILE_STORAGE` and `MEDIA_URL`. Django supports various backends for storing media, as applicable for your deployment strategy. See Django docs on the [file storage API](https://docs.djangoproject.com/en/1.11/ref/files/storage/)
 
### Migrate databases, build front-end components
* `docker-compose up`: build and get django and other components running
* `docker-compose exec api python /badgr_server/manage.py migrate` - (while running) set up database tables
* `docker-compose exec api python /badgr_server/manage.py dist` - generate docs swagger file(s)
* `docker-compose exec api python /badgr_server/manage.py collectstatic` - Put built front-end assets into the static directory (Admin panel CSS, swagger docs).
* `docker-compose exec api python /badgr_server/manage.py createsuperuser` - follow prompts to create your first admin user account

### First Time Setup
* Sign in to http://localhost:8080/staff/
* Add an EmailAddress object for your superuser. [Edit your super user](http://localhost:8080/staff/badgeuser/badgeuser/1/change/)
* Add an initial TermsVersion object

#### Badgr App Configuration
* Sign in to http://localhost:8080/staff
* View the "Badgr app" records and use the staff admin forms to create a BadgrApp. BadgrApp(s) describe the configuration that badgr-server needs to know about an associated installation of badgr-ui.

If your badgr-ui is running on http://localhost:4000, use the following values:
* CORS: ensure this setting matches the domain on which you are running badgr-ui, including the port if other than the standard HTTP or HTTPS ports. `localhost:4000`
* Signup redirect: `http://localhost:4000/signup/`
* Email confirmation redirect: `http://localhost:4000/auth/login/`
* Forgot password redirect: `http://localhost:4000/change-password/`
* UI login redirect: `http://localhost:4000/auth/login/`
* UI signup success redirect: `http://localhost:4000/signup/success/`
* UI connect success redirect: `http://localhost:4000/profile/`
* Public pages redirect: `http://localhost:4000/public/`

#### Authentication Configuration
* [Create an OAuth2 Provider Application](http://localhost:8080/staff/oauth2_provider/application/add/) for the Badgr-UI to use with
    * Client id: `public`
    * Client type: Public
    * allowed scopes: `rw:profile rw:issuer rw:backpack`
    * Authorization grant type: Resource owner password-based
    * Name: `Badgr UI`
    * Redirect uris: blank (for Resource owner password-based. You can use this to set up additional OAuth applications that use authorization code token grants as well.)

### Install and run Badgr UI {#badgr-ui}
Start in your `badgr` directory and clone badgr-ui source code: `git clone https://github.com/concentricsky/badgr-ui.git badgr-ui`

For more details view the Readme for [Badgr UI](https://github.com/concentricsky/badgr-ui).
