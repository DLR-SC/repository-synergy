#PySchema

PySchema is a library for Python class declaration with typed fields that can be introspected and have data contracts associated with them. This allows for better data integrity checks when serializing/deserializing data and safe interaction with external tools that require typed data.

The foremost design principle when creating the library was to keep the definitions very concise and easy to read. Inspiration was taken from Django's ORM and the main use cases in mind has been database interaction (Postgres) and Apache Avro schema/datum generation.

PySchema has been tested on Python 2.6 and Python 2.7

For documentation and more info see http://spotify.github.io/pyschema/

