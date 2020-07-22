# domopoules
A project to make own chicken housr door locking system

This project is originally based on article by : 
https://www.ladomotiquepourtous.fr/20180424/poulailler-connecte.html

But as code presentation was ugly, made a git repo for it... and improved things

## Installation

prerequisites : 
- Install it on a raspbian
- install apache : `sudo apt install apache2`

- git clone this repo `git clone github.com/nbossard/domopoules`
- go to folder /var/ww/html and make here a link to the repo folder chickenweb : `ln -s /home/pi/domopoules/chickenweb/ chicken`
- go to folder /opt and make here a link to the folder chickenpython : `ln -s /home/pi/domopoules/chickenpython/ chickendoor`
