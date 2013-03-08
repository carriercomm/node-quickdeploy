node-quickdeploy
================

Python script generating upstart and monit configuration-files for production environment.

At The Moment script generates and saves upstart script and put it straight to it's place at `/etc/init/<application_name>`

Monit script is printed to stdout because you n't want to overwrite your monit configurations.

Make sure you don't have any other upstart script with same name because otherwise it will be overwritten.

Requirements
============
 * pystache (You can install with pip `pip install pystache`)
 * monit
 * upstart

<pre>
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
</pre>
Example:

## Default use

Generate upstart and monit configurations straight to their places:
<pre>
	python deploy_node.py test /srv/nodejs/examples/example.js nodeuser /srv/nodejs/examples/ "Tero Testi" 2222 |tee /etc/monit/monitrc
</pre>
Start your upstart/node process:
<pre>
	start test
</pre>
Start monit by running:
<pre>
	monit -d 60 -c /etc/monit/monitrc
</pre>

## Only generate configuration-files

Same than earlier but the script is ´generateconfs.py´
