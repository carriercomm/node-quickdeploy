node-quickdeploy
================

Python script generating upstart and monit configuration-files for production environment.

At The Moment script generates and saves upstart script and put it straight to it's place at /etc/init/<application_name>
Monit script is printed to stdout because you n't want to overwrite your monit configurations.

Make sure you don't have any other upstart script with same name because otherwise it will be overwritten.


usage: deploy_node.py [-h] NAME PATH USER HOME AUTHOR PORT

Deploys node.js with upstart and monit

positional arguments:
  NAME        application machine name (dont use any special letters or
              spaces)
  PATH        absolute path of node.js script
  USER        user that runs the node-process
  HOME        home directory
  AUTHOR      application author
  PORT        application port for monit

optional arguments:
  -h, --help  show this help message and exit

Example:


Generate upstart and monit configurations straight to their places:
	python deploy_node.py test /srv/nodejs/examples/example.js nodeuser /srv/nodejs/examples/ "Tero Testi" 2222 |tee /etc/monit/monitrc

Start your upstart/node process:
	start test

Start monit by running:
	monit -d 60 -c /etc/monit/monitrc
