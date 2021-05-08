![Spartacus Logo](Documentation/Images/spartacus-logo.jpg)

Version française plus bas.
## What is spartacus?
Spartacus is an open source learning environment that aims in helping students learn the basis of
assembly programming and operating system development. It is portable and easy to learn.

As of the current version (2.0) the game environment that was present in the original
project is no longer available. However, the virtual machine now has everything that
is required to write a basic operating system.

NOTE:
This project has been tested using python 3.5.2

All documentation is available in the "Documentation" folder.
Please note that some code examples are available in the "testFiles"
folder. Also note, for those who like code coloring, a Notepad++
syntax file is available at "Documentation/CapuaASM-NPPLanguage.xml".
Simply import that file into your "user defined" language in NPP
in order to benefit from code coloring for the Capua assembly language.

The Assembler.py, Linker.py, Debugger.py and HardDriveCreator.py files are meant to
be used by the user. Simply invoke these from the command line in order
to be able to see how to use them. Help option = -h

## Where to start?
There is a quick start guide in the documentation folder.

## Contribution
Spartacus is still in its early age and is far from being entirely done. Multiple
things are still required to make this project as useful as it can be. If you are
interested in contributing, before you start writing code, please contact us and
we will exchange on your idea and vision. This is simply to ensure that what you
have in mind can be merge into Spartacus main branch. Here is a list of areas that
still require a lot of work:


* Virtual memory system (no support at current time)
* Floating point arithmetic  (no support at current time)
* C (or other language) compiler (no compiler at current time)
* Debugger improvement (step into, step over, ...)
* ".o" file format improvement (current format is prone to bugs)


Please note that any contribution has to follow GPLv2 licence. Also, any contribution
should be reflected in the documentation for at least 1 of the languages. For example
if someone writes the code to support virtual memory, it is expected that this person
will contribute in updating the documentation so it reflects the changes made. 

Any code contribution not respecting these requirements will be rejected.

## Folder structure
* CapuaEnvironment:
    * This folder is where the VM code sits.
* Configuration:
    * This folder holds multiple configuration elements used at multiple place inside the project
* Documentation:
    * All non code documentation is in there
* ToolChain:
    * NOTE ABOUT THE TOOL CHAIN:
        This tool chain was originally built for testing purpose not for programmer.
        Therefore, bugs are present and code is NOT fully tested. We are improving this
        but there is still a lot of work to be done. The linker is
        more than likely going to be re-written.
    * All tool chain related code is here. For example, the code allowing to parse and link files
    is in there. The debugger code is there too.
* testFiles:
    * This directory holds some code example
- - -
## Qu'est-ce que Spartacus?
Spartacus est un environnement libre visant à aider les étudiants à apprendre les bases
de la programmation assembleur et du développement de systèmes d'exploitation. C'est
un environnement portable et facile à apprendre.

La version actuelle (2.0) ne comprend plus le code de l'environnement de jeu qui 
était présent dans la version original du projet. Cependant, la machine virtuelle
comprend maintenant tous les éléments requis pour l'écriture d'un système d'exploitation
minimaliste.

NOTE:
Ce projet fut testé à l'aide de python 3.5.2

L'ensemble de la documentation est disponible à l'intérieur du
dossier "Documentation". Notez que des exemples de code sont disponibles
à l'intérieur du dossier "testFiles". Un fichier de syntaxe Notepas++
est aussi diponible à l'emplacement "Documentation/CapuaASM-NPPLanguage.xml".
Vous pouvez ajouter ce fichier à vos langage personnalisés dans NPP afin
de bénéficier de la coloration du code pour le langage assembleur Capua.

Les fichiers Assembler.py, Linker.py, Debugger.py and HardDriveCreator.py ont
pour objectif d'être utiliser par l'utilisateur. Invoquez simplement ces fichiers
à partir de la ligne de commandes. Les options d'aides pour ceux-ci sont accessibles
à l'aide de l'option "-h". 

## Où commencer?
Un guide de démarrage rapide est présent dans le dossier "Documentation".

## Contribution
Spartacus n'est pas encore un projet mature. Plusieurs éléments sont toujours
requis afin de rendre ce projet le plus utile possible. Si vous êtes intéressé
à contribuer, avant de commencer, veuillez nous contacter. Nous échangerons sur
votre idée et votre vision. Ceci a simplement pour objectif de s'assurer que
votre idée de développement peut être intégrée à l'intérieur du projet principal.
Voici une liste d'éléments qui demandent encore beaucoup de travail:


* Mémoire virtuelle (aucun support actuellement)
* Opérations en virgule flotyante  (aucun support actuellement)
* Compilateur C (ou autre langage) (aucun support actuellement)
* Ajout au débugueur (step into, step over, ...)
* Amélioration du format".o" (current format is prone to bugs)


Please note that any contribution has to follow GPLv2 licence. Also, any contribution
should be reflected in the documentation for at least 1 of the languages. For example
if someone writes the code to support virtual memory, it is expected that this person
will contribute in updating the documentation so it reflects the changes made. 

Any code contribution not respecting these requirements will be rejected.

## Structure de fichier
* CapuaEnvironment:
    * Ce dossier contient le code de la machine virtuelle.
* Configuration:
    * Ce dossier contient les fichiers de configuration utilisés à multiples endroits dans le projet.
* Documentation:
    * Ce dossier contient toute la documentation
* ToolChain:
    * NOTE AU SUJET DES OUTILS:
        Les outils ont, à l'origine, été développé à des fins de test et validation
        et non pas pour être utilisés par le programmeur. Ainsi, des problèmes sont
        présents dans le code et ce dernier n'a pas été entièrement testé. Nous
        travaillons à l'amélioration des outils mais plusieurs autres éléments demandent
        aussi de l'attention. L'éditeur de liens sera probablement
        ré-écrit.
    * L'ensemble du code relié aux outils de développement est ici. Par exemple, le code permettant
    l'édition des liens et l'analyseur de code est dans ce répertoire. Le code du débogueur y est
    aussi présent.
* testFiles:
    * Ce répertoire contient des exemples de code.
- - -
This file is part of Spartacus project
Copyright (C) 2016  CSE

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
