Simple tool to display LOC (lines of code) count history for a git branch.


Example:

2010-05-13 14:38:21       42   +44    -2     initial
2010-05-13 14:40:14       44    +3    -1     hashbang added
2010-05-13 14:40:14       49    +8    -3     show last commit too


Run it as `git-loc --svg' to output svg graph on stdout.
It is possible to specify the .git folder you wish to the repository you wish to get stats about.
`git-loc --svg ../another-repo'
