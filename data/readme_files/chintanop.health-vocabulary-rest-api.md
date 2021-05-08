Health Vocabulary REST API
==========================
Health Vocabularly simple REST API to quickly integrate smart semantic search capabilities in your health apps. Use HaVoc to leverage the knowledge of hundreds of health/biomedical vocabularies spanning millions of medical terms and relationships in a jiffy. 

Some use-cases:

1. Get all synonyms, abbreviations of a medical term:  *“CHF” => congestive heart failure, heart failure* and so on. Access over **12.8 million** synonym terms.

2. Perform class based queries, e.g. get all *drug* brand names for all *antibiotics*

3. Create an “autosuggest” dropdown for *disease* names or *symptoms* or even *gene* names. 

4. Get related terms, e.g. get all *body parts/anatomical* organs related to a *disease*

5. Translate/Map codes between 190 biomedical vocabularies and across languages, e.g. Spanish to English and vice versa. 

Additional Benefits:

- Roll you **own internal vocabulary** and perform all the operations above 
- Use Docker instances to create a **load balanced cluster** setup
- Battle tested in **production use** in several Healthcare web apps, big data applications using Solr, Elastic Search and Apache Spark.


API operations
--------------
**NOTE: The required field are marked as “bold” in the API parameters**

**1. GET /concepts**

Search concepts by term and source terminology (SAB)

Parameters:

 - **term:** Any source medical term, e.g. diabetes 
 - sabs: A comma separated list of source vocabularies to restrict the concepts. The full list of vocabulary abbreviations is available [here](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html).
 - tty: Source term type to restrict the terms, e.g. PT for 'designated preferred name', MH for 'main heading'. The full list of source term types is available [here](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html).
 - sty - Semantic type to restrict the terms, e.g.T047 for 'Disease or Syndrome', T200 for 'Clinical Drug'. The full list of semantic types is available [here](https://metamap.nlm.nih.gov/Docs/SemanticTypes_2013AA.txt).
 - partial: 1/0 (if partial=1 then term will be partial term matches
   will be returned. if partial =0 then all matches will be returned.
   default =0)

Returns:
A list of concept objects



**2. GET /concepts_bulk**

Search concepts by terms in bulk and source terminology (SAB)

Parameters:

 - **terms:** A comma separate list of terms 
 - sabs: A comma separated list of source vocabularies to restrict the concepts 
 - partial: 1/0 (if partial=1 then term will be partial term matches will be returned. if partial =0 then all matches will be returned. default =0) delimiter:
   delimiter which separates the terms, default is comma(,)

Returns:
A list of concept objects


**3. GET /concepts/:cui**

Get full details for a concept (specified by CUI)

Parameters:

**cui**: concept id

Returns
A Concept object


**4. GET /concepts/:cui/children**

Get all childrens for a given concept. By default it will get all childrens based on UMLS (REL=CHD/RN) or the relationships can be restricted a given vocabulary

Parameters:

 - **cui:** concept id 
 - sab: The source vocabs to restrict the child definition. Currently supported: MeSH and SNOMEDCT 
 - explode: 1/0 - if
   set to 1 then get all children recursively. Currently supported
   vocabularies: MeSH

Returns:
A list of Concept objects


**5. GET /concepts/:cui/parents**

Get all parents for a given concept. By default it will get all parents based on UMLS (REL=PAR/RB) or the relationships can be restricted a given vocabulary

Parameters:

 - **cui:** concept id 
 - sab: The source vocabs to restrict the child definition.  explode: 1/0 - if set to 1 then get all parents recursively. Currently supported vocabularies: MeSH

Returns:
A list of Concept objects


**6. GET /concepts_bulk/:cui,:cui,:cui/parents**

Get all parents for a given list of concepts. By default it will get all parents based on UMLS (REL=PAR,RB) or the relationships can be restricted a given vocabulary

Parameters:

 - **cui list:**: list of comma seperated cuis 
 - sab: The source vocabs to restrict the child definition.  
 - explode: 1/0 - if set to 1 then get all parents recursively. Currently supported vocabularies: MeSH

Returns:
A list of Concept objects for each provided CUI


**7. GET /concepts/:cui/synonyms**

Get all synonym strings for a given Concept (:cui). Optionally, restrict the synonyms to a list of vocabularies.

Parameters:

 - **cui:** concept id 
 - sabs: A List of source vocabularies

Returns:
A list of strings, e.g. [“diabetes”, “diabetes type 2”,...]


**8. GET /rel/:sab/:code/:rel_type**

Get all target codes related to a given vocab/code pair by relationship rel_type

Parameters:

 - **sab:** The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC. 
 - **code:** The value of code to be looked up, e.g. 111-ABC
   degree: Control the number of hops in the graph
 - **rel_type:** The
   relationship to be looked up, e.g. is_diagnosed_by,
   causative_agent_of. The full list of relationship attribute types is available [here](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html).

Returns:
A list of Concept objects

**

**Code API**

**
The following set of APIs work with vocabulary codes

**9. GET /codes**

Search all codes 

Parameters:

 - **code:** Search for a given code  
 - sabs: Restrict the search a given set of vocabularies

Returns:
A list of Code objects


**10. GET /codes/:code/sabs/:sab**

Get details about a code.

Parameters:

 - **code:** Get details about a code  
 - sab: In a given source vocabulary

Returns:
A Code object

**11. GET /codes/:code1/sabs/:sab1/mapping/:sab2**

Get semantically equivalent mappings for code1 in sab1 in sab2

Parameters:

 - **code1:** Get details about a code 
 - **sab1:** In a given source vocabulary 
 - **sab2:** The target vocabulary to find a code in sab2

Returns:
A list of Code objects (one or more mappings)


* * *
Requirements
------------

- Python 2.7
- Django 1.4 or above
- MySQL or any other relational database supported by Django
- [UMLS Metathesaurus](http://www.nlm.nih.gov/research/umls/) Files in .SQL format.

* * *
Install/Set up
--------------

1. Check out the code into your local. 
2. Edit *settings.py( and update DATABASE settings to point to your local database
3. Create corresponding database tables, *python manage.py syncdb*
4. Load the MRCONSO.sql, MRREL.sql, MRSTY.sql (pronounced as Mr. Conso, Mr. Rel, Mr. Sty) into database from command line as follows: 

  mysql -u&lt;user&gt; -p&lt;password&gt; &lt;db_name&gt; &lt; MRCONSO.sql
 
  alter table MRCONSO add column id int auto_increment primary key;

  mysql -u&lt;user&gt; -p&lt;password&gt; &lt;db_name&gt; &lt; MRREL.sql
  
  alter table MRREL add column id int auto_increment primary key;
  
  mysql -u&lt;user&gt; -p&lt;password&gt; &lt;db_name&gt; &lt; MRSTY.sql
  
  alter table MRSTY add column id int auto_increment primary key;
  
5. Run the app, python manage.py runserver
6. For production environment, it is advised to host the app inside a [WSGI](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/) container.

More resources:
----------

 - http://blog.appliedinformaticsinc.com/getting-started-with-metamorphosys-the-umls-installation-tool/
 - http://blog.appliedinformaticsinc.com/umls-metathesaurs-tool-mysql-load-scripts-database-browse/
 - http://blog.appliedinformaticsinc.com/umls-metathesaurs-loading-umls-schema-data-to-mysql/
 - http://blog.appliedinformaticsinc.com/rest-api-over-umls-terminologies/

TODOs
-----
Coming soon on next major release:
- Currently, it does not have authentication or rate throttling mechanism. The API is currently designed for internal apps consumption. 
- Develop a commands.py to load the UMLS files into the database instead of load into local.
- A memcached version to store the tables in memory instead of a relational database.
- Create a fully expanded ISA hierarcy to support class based queries.

Frequently Asked Questions
--------------------------
* Why did you create this API?

  It was one of late spring days in NYC, we were coding our patient portal app for the New York eHealth Collaborative Challenge. They provided us with oh-so-[SHIN-NY](http://digitalhealthaccelerator.com/shiny-api/) API, but it sent us raw CCDA files and we wanted to display patient friendly lab result names. So we coded up this API that was called by our Javascript client on the patient portal to display nicer lab names.

* How is it different from the [UMLS Terminology Services](https://uts.nlm.nih.gov/home.html)?

   Our goal with Health Vocabulary REST API was to create a developer friendly API that abstracts-away a lot of UMLS specific notions to support rapid app development. The UTS provides a full-fledged web services based interface. Additionally, this API server can be hosted and managed locally.

* Can I get support to get this API set up for us?

  Absolutely! Just shoot us an email at info@appliedinformaticsinc.com / chintan@trialx.com / nadeem@trialx.com 


* * *

LICENSE
-------
Copyright (c) 2015 by Applied Informatics Inc. Licensed under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) license.
