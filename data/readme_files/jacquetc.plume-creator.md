PLUME CREATOR

v 0.67
	- new feature : overview in the project tree.
	- Fix Mise en Scene crash when deleting an object
	- fix : huge memory leak when opening a sheet with spellchecker activated.
	- trash : you can rename deleted files
	- Outliner : adds a few colors
	- fix : colors of "Space Opera" theme
	- fix : "add" menu button of Mise en Scene pops up instantly


v 0.66.1
	- fix : new project dialog freeze on Windows when clicking on "next"
	- russian translation updated
	- french translation updated

v 0.66
	- new icon set
	- fix the Space Opera theme
	- fix the copy/paste from a document with comments
	- project dock now adapts itself to the tree size.
	- fix : text is truncated when text zone width at max
	- fix : can't open plume project in Gnome and Unity
	- added a script to compile and deploy on OSX

V 0.65.2
	- quick fix : we can't select a word.
	
v 0.65
	- removed 'text width' option from settings
	- added option for commas in numbers (e.g. 1,000)
	- added custom colors in settings
	- added theme manager in settings
	- new page in the "New Project" wizard : structure
	- new theme : Space Opera (dark theme)
	- new tool bar
	- fix : splitter option didn't launch
	- fix : Mise en Scène manager tree didn't update correctly
	- fix : update checker was blocking the interface
	- updated Windows version to Qt 5.1.1
	
	
v 0.64
	- fix : crash when no dictionary was selected
	- spell check activates for the whole project
	- Mise en scène (ex-Attendance) : 
		- added Drag & Drop

v 0.63
	- Spanish (Spain) language added
	- Russian language added
	- New spell-checker
		- suggestions
		- underlining
		- user dictionary manager
		- user dictionary importer
		- Mise en scène names are added
		- user dictionary importer
	- New Find & Replace dialog
	- New quick Find & Replace
	- Project tree :
		- added "status" to right-click menu
		- added a bold font for the currently opened sheet
	- Exporter :
		- checkbox behavior now allow for single selection
	- fix : no wordcount in status bar for scenes and separators
	- fix : tree icons didn't update for collapsed state or not
	- new handle bars to change the size of the main text area
	- Fullscreen :
		- fix : "next" button didn't work
	- fix : "paste unformatted" shortcut didn't work
	- fix : crash when opening directly a *.plume_backup
	- removed system tray message when closing Plume (bug in Ubuntu)
	- added style switching in the "previous" and "next" texts zones
	- now we know what style is selected.
	
v 0.62
	- new Project tree :
		- "act" level added
		- new icons
		- drag / drop faster
		- new right-click menu
		- trash added
		- new "badges" in right-click menu
	- Outliner :
		- "Outliner becomes "Workbench"
		- drag / drop added
		- new right-click menu
		- new "badges" column
		- new "status" column
	- Fullscreen :
		- new tree navigator
		- fix : cursor position isn't saved when quitting fullscreen
	- bug fixed : outliner doesn’t launch when no sheet is opened
	- better copy / paste
	- added "Copy unformatted" to the right-click menu
	- Bug fixed : text had an underground color when pasted from internet 
	- Quazip updated
	- zip files ".plume" are cleaned of intruders before compressing
	- Portuguese (Brazil) language added
	- fix : PoV column in Outliner displays sometimes HTML.
	- exporter updated to the new project tree system
	

v 0.61
	- Added colors
	- status bar thined
	- fix : splitter in note dock recovered
	- main text zone : added arrows to show previous and next texts
	- Quazip updated
	- Outliner :
		- fix : synopsis and note inverted
		- added icons in the tree
	- Start Center :
		- is now the active window
		- fix : tool-tips unreadable on Ubuntu
	- saves :
		- file checker added;
		
v 0.60
	- New Start Center
	- Removed Project Manager
	- Exporter :
		- Added export to CVS
		- Added ### or *** as scene titles
		- Add export in PDF
	- Proxy settings changed
	- Linux :
		- fix : no mime icon and action
	Progress bar :
		- fix : progress bar doesn't start at 0  


v 0.59.2
	- Attendance :
		- fix : Plume crash when droping characters in the top box list.
	
v 0.59.1
	- Attendance :
		- indentation in views shorted
	- Outliner :
		- force a reset for this version
		- add a button to force a reset manually
	- Project manager :
		- fix : add again project in the list when opening an unknown project

v 0.59
	- New Attendance Manager and dock.
		- Point of View
		- customizable roles
	- New real time word count
	- Outliner :
		- added "Point of View" column
		- row are colored
	- Fullscreen :
		- added buttons "previous", "next" and "new sheet"
	- New progress bar
	- New Find & Replace in right-click menu
	- The projects are now one single file
	- Added .plume_backup for worst cases
	- Major change of Plume inner workings
	- Added notification tray message when exiting
	- Text is saved while in fullscreen mode
	- Qt5 ready, waiting for packages in Linux distribs
	
	
v 0.58
	- More consistent key bindings
	- Added proxy support for updater
	- Fixed the size of the exporter preview window for netbooks
	- Bug fixed : text cursor keeps blinking when losing focus in notes 
	- Added a target word count for the session
	
v 0.57.1
	- Bug fixed : main window stuck in 550x800

v 0.57
	- New updater
	- Outliner : right-menu in headers to hide/show columns
	
v 0.56
	- added german translation (de_DE)
	
v 0.55
	- added italian translation (it_IT)
	- Bug Fixed : in fullscreen, text lost when no zoom applied
	- code cleansing

v 0.54
	- New feature : styles, with a style manager.
	- New fullscreen mode
	- Bug fixed : word count doesn’t see the line breaks 
	- Bug fixed : for external projects, crash when opening menu options 
	- text edit options font name and font size disabled
	- "Show Previous Scene" and "Show Next Scene" buttons removed
	- added "Keep only one tab opened" option in settings 
	- added "Hide tabs" option in settings 

v 0.53
	- Text Splitter Dialog finished.
	- New Project Manager
	- Outliner :
		- the table is a tree now
		- right-click menu
	
	- Handle bars added above and below the main text zone to show previous and next scene.
	- bug fixed : when pasting plain text, line breaks weren't pasted
	- bug fixed : crash when tabs are all closed and showing previous scene
	- bug fixed : notes an synopsys right margins wrong in new scenes
	- bug fixed : the docks sizes are minimal at startup.
	- Projects files (*.plume) can now be opened on Linux !
	- behavior when opening external projects fixed
	- Wordcount centered under the sheet.
	- "Tree" dock renamed "Project" dock
	- Closing Project dock is now forbidden
	- Project button removed in vertical toolbar
	- "Show Previous Scene", "Outliner" and "Fullscreen" buttons are moved to the side tool bar
	- Plume is now lightly styled
	- added a basic spreadsheet Outliner
	- removed the sheets Outliner
	- added a "View" menu
	- added a few icons from Oxygen theme
	- added "Release notes" in the menu

v 0.52
	- bug fixed : in netbook mode, the note dock stays at the bottom.
	- "Show Previous scene" button is moved to the status bar
	- "Show Notes" button is removed from the status bar

v 0.51
	- Dialogs resized for 10" netbooks
	- 2 display modes available : "Desktop" and "Netbook"
	- Toolbar to hide/show docks added
	- right-side menu removed
	- edit options moved to the top menu
	- slider for "main text zone width" moved to settings dialog
	- Outliner is temporarily removed  

v 0.50
	- Plume adapts its style to Gnome and KDE
	- style selector added in settings
	- button "Hide Notes" added (temporary)
	- menu bar position selector added in settings (top or side)
	- french translation updated

v 0.49
	- tree : 
		- bug fixed: crash when deleting a scene separator
	- Exporter : Html export got manuscript formatting

v 0.48
	- annoying bug fixed : text font sometimes came back to default system font
	- copy/paste from an external source : text is now formated
	- button added to give a project, a book and a chapter wordcount
	- prevent multiple space characters between words in fullscreen, synopsies ans notes
	- bold, italic and shortcuts added in outliner text zones
	- french translation updated

v 0.47
	- in fullscreen editor : 
		- added "escape" key to quit the fullscreen editor
	- option added : prevent multiple space characters between words


v 0.46
	- bug fixed : crash after opening an external project

v 0.45
	- update checker added
	- language selector added at startup and in settings
	- french translation updated

v 0.44.1
	- character/item/place manager :
		- bug fixed : crash after deleting an item already opened
		- icons added
		- tooltips added

v 0.44
	- character/item/place manager :
		- bug fixed : crash when opening the att. manager two times
		- bug fixed : names lost
	- french translation updated

v 0.43
	- printing system enabled
	- font menu added in attendance
	- bold, italic and text alignment shortcuts added in text zones
	- french translation updated

v 0.42
	- character/item/place manager :
		- sheet list dynamic title added
 		- bug fixed : item details doesn't save
		- bug fixed : crash when exiting with att. manager launched
	- bug fixed : crash when exiting with no project opened
	- french translation updated
	- first Mac release ! Tested on OSX Lion
		- app bundled and .plume file association  

v 0.41
	- Microsoft Windows release :
		- add .plume file association and .plume file icon
	- only one instance of Plume Creator is allowed
	- opening a .plume file adds it in the project manager
 
v 0.40
	- first Microsoft Windows release ! Tested on Xp and 7
	- character/item/place manager :
		- a few bugs solved
	  
v 0.39  
	- character/item/place manager :
		- it's working !
		- option menu will be implemented shortly
	- bug solved : crash when opening a new sheet after deleting one

v 0.38  
	- in fullscreen editor :
		- mouse cursor hide when idle for 3 seconds
	- very basic character/item/place manager (not finished and not useable yet)
	- tabs not moveable anymore (it solves a few bugs)
	- bug solved: font problem for text zone at the first line

v 0.37  - Outliner :
		- paragraph indent & margin menu added
		- bug solved: the outliner crashed when closed
		- outliner centers on the opened sheet
	- Exporter can give a preview

v 0.36
	- Outliner :
		- display bugs solved
		- notes and synopsies keep the good fonts when their entire first line is deleted 
		- the outline is updated when the main tree is modified
		- outline titles are more visible
		- "write" button ("w") opens the respective sheet
		

v 0.35
	- Outliner :
		- font family & size menu added
		- size menu added
		- item scroll bars color blend more 
	- french translation updated

v 0.34
	- set default style to Qt's "Plastique"
	- set default save time to 20 000 ms, not 20 ms
	- "auto rename children" repaired
 	- load / save more centralized. 
	- "rename" context menu action repaired
	- tree : added drag / drop of scene breaks
	- added very basic Outliner :
		- title editing
		- synopsys editing
		- note editing
		(no "drag / drop" or "add item" yet)

v 0.33
	- tree : drag & drop selects the good item now
	- in fullscreen editor : removed the blank line below the main edit zone
	- added new splash screen icon

v 0.32
	- added french translation (fr_FR)
	- exported document is more neat
	- progress bar when exporting

v 0.31
	- added fast access to synopsies and notes in fullscreen editor
	- added application icon and a sample splash screen

v 0.30
	- font config for synopsies and notes
	- config for indent and margin
	- export in .odt .html and .txt

v 0.29
	- in fullscreen editor :
		- SOLVED bug : same docs between projects displayed in fullscreen editor
	- cursor position saved in notes and synopsies
	- basic indent and margin for all editors (no config)

v 0.28
	- in fullscreen editor :
		- added colors

v 0.27
	- in fullscreen editor :
		- added clock
		- added timer label
		- added wordcount
		- added context menu
		- added text area width option
	- bug solved : project manager displayed wrong project number

v 0.26
	- added fullscreen editor (very basic)
	- font change more reliable (menu and config)
	- removed seconds in countdown (useless) 

v 0.25
	- font config (size and family)
	- save last cursor position

v 0.24
	- config dialog	
	- autosave and its config


v 0.23

	- two openings of the "project manager" when "new project" clicked.
	- slider in edit menu to change the text area width.
