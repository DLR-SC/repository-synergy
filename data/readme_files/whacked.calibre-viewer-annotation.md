#+ARCHIVE: doc/devlog/%s_archive::

* adding annotation (read and write) capability to calibre's ebook-viewer
  
  sporadic work in progress. last updated on 2016-02-10 *(BREAKS
  EARLIER VERSION, see below)*

  *WARNING: if you have used this before, and are planning to update,
  please backup your highlights database before updating*

  this plugin is *NOT* pre-packaged and ready to use. You will need to
  setup some dependencies (see below)

  [[./doc/img/ss-007.png]]
  
  There are 2 main issues we care about here, addressed in headings below

  1. importing, i.e. reading annotations made elsewhere.
  2. editing, i.e. displaying and editing annotations in calibre's
     =ebook-viewer= program. this is doable now. read below for
     details. notes are stored into an =sqlite= database using the
     =okfn/annotator= API and thus their JSON format.

* external dependencies + preparation

  - =sqlalchemy= (currently working with =0.9.8=)
    
  installable via =pip install sqlalchemy=; due to *PATH HACK* below,
  we're assuming a system install where you know the inclusion path
  for both libraries

** alternative installation

   [[http://www.sqlalchemy.org/download.html][download]] and extract sqlalchemy, and

   =mv SQLAlchemy-*/lib/sqlalchemy calibre/lib/python2.7/site-packages=

* installing+using the plugin

  *NOTE: if you have problems installing over an existing =Viewer Annotation Plugin.zip= in your calibre plugins directory, try deleting that zip file first*

  1. ensure you have a working development environment set up (basically, ensure you can run =calibre-customize=)
  2. clone this repo
  3. edit the *PATH HACK* [[file:ViewerAnnotationPlugin/annotator_model.py]]
     so calibre is able to see your local install of =sqlalchemy=.  It is
     currently hard-coded to search in
     =/usr/local/lib/python2.7/dist-packages=. There's probably a way to make
     this self-contained; see discussion [[http://www.mobileread.com/forums/showthread.php?t%3D241076][here]] but it's not currently a priority.
  4. in your terminal/command line program, navigate to the
     =ViewerAnnotationPlugin= directory and run =calibre-customize -b .=
     to install the plugin. If successful your =ebook-viewer= should
     incorporate the annotations. By default it will create a sqlite
     database =ebook-viewer-annotation.db= into your home directory.
     
* importing + managing annotations (update 2016-05-01)

  currently only works with epub books
  
  *USE AT YOUR OWN RISK* this includes a little manager app using [[http://electron.atom.io/][electron]] that aims to help importing annotations into the current =ebook viewer annotation= database.
  
  This aims to provide a GUI that performs the procedure described in =import_utility.rb=
  
** setup + requirements

   see file:package.json for npm dependencies. Unfortunately, you will need to build the [[https://github.com/mapbox/node-sqlite3][node sqlite3]] extension, which is rather tricky. A non-working build will cause the electron app to throw an exception on startup.

*** setting up electron sqlite3 extension

    steps after =npm install sqlite3= or however you've installed it
    
    - =npm install -g nw-gyp=
    - get electron version with =electron -v=
    - ref http://verysimple.com/2015/05/30/using-node_sqlite3-with-electron/ (careful with the =cd= and =lib= paths)
      also https://github.com/electron/electron/blob/master/docs/tutorial/using-native-node-modules.md,
      also http://stackoverflow.com/questions/32504307/how-to-use-sqlite3-module-with-electron

**** example build procedure sqlite3 for electron on recent ubuntu using electron =v0.37.7=

     #+BEGIN_SRC sh :eval never
     cd node_modules/sqlite3
     npm run prepublish
     node-gyp configure --module_name=node_sqlite3 --module_path=lib/binding/node-v47-linux-x64
     node-gyp rebuild --target=0.37.7 --arch=x64 --target_platform=linux --dist-url=https://atom.io/download/atom-shell --module_name=node_sqlite3 --module_path=lib/binding/node-v47-linux-x64
     mkdir lib/binding/electron-v0.37-linux-x64
     mv build/Release/node_sqlite3.node lib/binding/electron-v0.37-linux-x64
     #+END_SRC

** USAGE
   
   start the application with =electron .= from the current project directory (where =package.json= is).

*** viewer panel

    - search calibre books (currently *hard-coded* to =~/Calibre Library/metadata.db=)
    - select a book to load annotations you have for that book (currently *hard-coded* to =~/ebook-viewer-annotation.db=)
    - open the selected book using =ebook-viewer= (assumes your path is set up correctly)

*** match-tool panel

    for reconciling structured highlight files (e.g. downloaded) with your book file, and output the result or add them to the viewer annotation database.

**** generate highlights yml files

     for kindle, this uses =get_kindle_highlights.rb=, it relies on
     [[https://github.com/speric/kindle-highlights][speric's kindle-highlights]] so you will need to run =gem install
     kindle-highlights=. You can either enter your login information
     at run-time, or store your login information in a file at
     =~/.aws/kindle= or =~/.aws/kindle.gpg= if you have the =gpgme=
     gem installed.
    
     this script and does some additional matching and sanity checking
     on top of =kindle-highlights=. *In particular, speric's version
     does not handle text notes attached to highlights*; this script
     does a 2-pass to put them together.

**** reconcile annotation positions with book + insert to database

     - select a yml file (currently hard-coded to expect yml files in =kindle-highlights=. This should change in the future.)
     - it will try to load the epub from Calibre, and match highlight text with the epub text.
     - click the "check" button to visually check it finds the text correctly in the book.
     - if the check is successful you may get a button to directly insert to your annotation database
     - you can output the results of reconciliation to a json file with =save output to file=

**** reconcile all

     cycles through every entry that hasn't been verified and tries to verify them automatically. This uses an ugly setTimeout mechanism (because the match process takes some time and running all in parallel causes it to break)

*** importing the output json and write to the ebook-viewer-annotation database

    =python importjson.py xpath-matched-output.json ebook-file.epub=

    will perform a dry run, and you can check for surprises. the ebook
    file is optional. It is used to generate =anchor= entries, but the
    anchor positioning logic is not yet implemented (so we are relying
    on the =xpath= being accurate and robust).

    this will output basic information of what matches and what fails.
    if you are lucky, everything will find its proper position.

    once everything looks ok, apply the changes with
    
    =DRY_RUN=FALSE python importjson.py xpath-matched-output.json ebook-file.epub=

** text matching logic

   logic is in [[https://github.com/jbr/sibilant][Sibilant]] files in =manager/js/=; javascript can be generated via e.g.
   =for f in manager/js/*.sib; do sibilant $f -m -o manager/js; done=
   
*** cfi.js used by manager

    comes from [[https://github.com/kovidgoyal/calibre/blob/master/src/calibre/ebooks/oeb/display/cfi.coffee][cfi.coffee]]

    compiled with with =coffee --compile cfi.coffee=

* development
  
  The base plugin code is loosely taken from [[http://manual.calibre-ebook.com/creating_plugins.html#a-user-interface-plugin][user interface plugin]],
  although the viewer plugin is slightly different. refer to the
  [[http://manual.calibre-ebook.com/plugins.html#viewer-plugins][Viewer plugins]] section in the calibre API documentation. Other
  exploratory notes on interacting with calibre proper may be found in
  the =doc/devlog=.
  
  To play with this code, edit the code in the =ViewerAnnotationPlugin=
  directory, then run

  #+BEGIN_SRC sh :eval never
    calibre-customize -b . && ebook-viewer $PATH_TO_EPUB
  #+END_SRC
  
  and it should launch the viewer with the changes applied.

  for the electron live development using sibilant, also see [[https://github.com/skeeto/skewer-mode][Emacs skewer-mode]] and [[https://github.com/whacked/sibilant-skewer][sibilant-skewer]]

** data model
   
   *TODO: describe anchor model* (currently not used in viewer / annotator.js)
   
   We generally follow the [[http://docs.annotatorjs.org/en/v1.2.x/annotation-format.html][format from Annotator]]

   A sample =Annotation= structure is like:
   
   #+BEGIN_SRC javascript :eval never
     {
       "id": 42,                                  // INTEGER NOT NULL PRIMARY KEY
       "created": "2014-11-02 12:19:13.000000",   // DATETIME DEFAULT NOW
       "updated": "2014-11-02 12:19:13.000000",   // DATETIME DEFAULT NOW
       
       "title": "The title of an exemplary book", // TEXT, title of book in Calibre
       "text": "A note I wrote",                  // TEXT, content of annotation
       "quote": "The text actually said this, since I quoted it.", // TEXT, the annotated text (added by frontend)
       "uri": "epub://part0036.html",             // TEXT, URI of annotated document (added by frontend)

       "user": "yousir",                          // TEXT, generally set to $HOME username or machine hostname
       
       // these are populated run-time by backref via the `range` table
       "ranges": [                                // list of ranges covered by annotation (usually only one entry)
         {
           "start": "/p[69]/span/span",           // (relative) XPath to start element
           "end": "/p[70]/span/span",             // (relative) XPath to end element
           "startOffset": 23,                     // character offset within start element
           "endOffset": 120                       // character offset within end element
         }
       ]
     }
   #+END_SRC
  
   A sample =Range= structure is like:

   #+BEGIN_SRC javascript :eval never
     {
       "id": 2,                               // INTEGER NOT NULL PRIMARY KEY
       "start": "/p[69]/span/span",           // VARCHAR(255), (relative) XPath to start element
       "end": "/p[70]/span/span",             // VARCHAR(255), (relative) XPath to end element
       "startOffset": 23,                     // INTEGER, character offset within start element
       "endOffset": 120,                      // INTEGER, character offset within end element
       
       "annotation_id": 42                    // INTEGER FOREIGN KEY(annotation.id)
     }


   #+END_SRC

   The =Consumer= model is defined (inherited from the older reference
   implementation) but is not used.

** okfn/annotator files

   current code is hard-coded to expect =annotator-full.1.2.7=
   for javascript/css. For a different version:

   1. visit https://github.com/okfn/annotator/downloads/
   2. if you've unzipped e.g. annotator-full.1.2.7.zip, you should get
      a directory =annotator-full.1.2.7/= with a =.js= and a =.css= file
      inside it. Move this directory into the =ViewerAnnotationPlugin=
      directory.
   3. edit =ViewerAnnotationPlugin/__init__.py= and find the
      =load_javascript= and =run_javascript= sections and make sure the
      paths there correspond to your extracted annotator js/css
      files.

** okfn/annotator plugin (store.js)

   see =store.coffee=; =store.js= is derived from =coffee --compile store.coffee=
   then moved into =ViewerAnnotationPlugin=

* breaking changes / updating / migrating

  The most recent update (2016-02) is not compatible with all updates
  prior to 2016. However, the data model is mostly the same.
  
*** TOFIX

    - sometimes editing an annotation raises a UnicodeError (could be related to imported highlights)
    - annotation stops working with changing flow mode (ref https://github.com/whacked/calibre-viewer-annotation/issues/2)


*** 2016-02-09 :: elixir removed, change model;
    
    If you actually need to migrate, see [[file:migrate.sh]] which tries
    to convert the tables to the newer data model.

    In particular, =quote= is now the default =Annotation= field to
    store the highlighted text; =text= is for comments. =timestamp= is
    superceded by =updated= and =created=.
  
* issues

  - either the js file inclusion or css style injection or both cause
    long pauses in the reader when navigating between epub chapter
    boundaries


  
