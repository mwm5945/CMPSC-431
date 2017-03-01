# CMPSC-431
THON Inventory System

## Prereqs.
 * Python 3 
 * Pip 
 * virtualenv
 * virtualenvwrapper
 * MySQL 5
 
## Repository 
* $ mkdir inventory
* $ cd inventory
* $ git clone https://github.com/mwm5945/CMPSC-431.git

## Setting Up Stuff
1. vim ~/.bash_profile and add the following

   export WORKON_HOME=~/Envs
   
   source /usr/local/bin/virtualenvwrapper.sh

   Then do $ source ~/.bash_profile

2. Make a virtual environment

  $ cd inventory
  
  $ mkvirtualenv inventory
   
3. Activate it 

   $ workon inventory
   
4. Create mysql database 

  mysql> create database inventory
  
5. Install requirements

   $ pip install -r requirements.txt
  
  



