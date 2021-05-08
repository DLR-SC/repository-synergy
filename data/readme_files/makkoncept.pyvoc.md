<p align="center">
  <img  algin="center" height="300" src="https://raw.githubusercontent.com/makkoncept/pyvoc/master/.art/logo14.png" />
   <h3 align="center">Cross-platform dictionary and vocabulary building command line tool</h3> 
  <p align="center">
    <a href="https://github.com/makkoncept/pyvoc/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
    </a>
    <a href="https://github.com/makkoncept/pyvoc">
    	<img src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-blue.svg" alt="platforms" />
    </a>
    <a href="https://github.com/makkoncept/pyvoc/">
      <img src="https://img.shields.io/badge/awesome-yes-green.svg" />
    </a>
  </p>
</p>

---

# Pyvoc 

<p align="center">
  <img alt="simple pyvoc example" src="https://raw.githubusercontent.com/makkoncept/pyvoc/master/.art/new.gif">
</p>


**Use it to improve your english vocabulary, brush up some word meanings or as a simple command line dictionary.**

---
Jump to:

- [Installation](#Installation)
- [Usage](#Usage)
- [Groups](#Groups)
- [Examples](#Examples)
- [todo](#todo)

## Installation
Install it using pip. Just run:
```bash
pip3 install pyvoc
```

## Usage
After installing pyvoc, run `pyvoc word` to _automatically create necessary config files_ in your home directory.

- Fetch meaning of word
```
pyvoc word
```

- Fetch meaning of word and add it to vocabulary group:
```
pyoc word -a
```
- Take quiz of 20 questions from vocabulary group 101:
```
pyvoc 101 -q 30
```
_read some more [examples](#Examples)_

```
➜ pyvoc -h
usage: pyvoc [-h] [-a] [-g G] [-r] [-q QUIZ] [-l] word

command line dictionary and vocabulary building tool

positional arguments:
  word                  give meaning of WORD

optional arguments:
  -h, --help            show this help message and exit
  -a, --add             add WORD to vocabulary group
  -g G                  {optional} group no.(1-50) to add the WORD to
  -r, --revise          revise a vocabulary group (WORD is group number).
  -q QUIZ, --quiz QUIZ  starts quiz, WORD is group no. and QUIZ is no. of
                        questions
  -l, --list            list all user made vocabulary groups

```
## groups
pyvoc lets you add words to vocabulary groups, which you can later revise or take quiz from.
- 100 groups of 60 words are **reserved** for the user. 
- pyvoc **incrementally add words** to groups 51-100, if group number is not provided.
- you can specify a group from 1-50 using [-g] option. (helpful when you want to **organize some words yourself**) 
- 3 refined, **custom groups of 800 words each** (words taken from GRE and SAT preparation websites) already present.
- these groups are 101, 102 and 103.

## Examples

### add word to a specific group
```
pyvoc word -a -g 5
```
 
Fetch meaning of the word and add it to vocabulary group 5. **Use this option to organize words however you like.**

**_for example_** 
- alphabatically
- words from books you have been reading
- parts of speech  
- increasing difficulty
---
### revise a group
```
pyvoc 51 -r
```
 revise word meaning of vocabulary group 51(if present) in random order.
 
 ---
 ### show group list
```
pyvoc word -l
```
 Fetch meaning of word and lists all group numbers along with their size.
 
## todo
 - [ ] make the code more pythonic (_continuous process_)
 - [ ] add options to revise by pattern a particular group. (like all the words starting with 's')
 - [ ] show the word-meaning user got wrong at the end of quiz.
 - [ ] add option to show all the words added by the user to groups. 
 - [ ] increase the number of custom groups
 - [ ] also show custom groups in [-l] option