import pystache

import argparse

output = './output/'

parser = argparse.ArgumentParser(prefix_chars='-', description='Deploys node.js with upstart and monit')
parser.add_argument('application_name', metavar='NAME', help="application machine name (dont use any special letters or spaces)")
parser.add_argument('absolute_path', metavar='PATH', help="absolute path of node.js script")
parser.add_argument('user', metavar='USER', help="user that runs the node-process")
parser.add_argument('home', metavar='HOME', help="home directory")
parser.add_argument('author', metavar='AUTHOR', help="application author")
parser.add_argument('port', metavar='PORT', help="application port for monit")

args = parser.parse_args()

template = open('template_upstart.conf', 'ru')
monit = open('template_monit.conf', 'ru')

upstart = open(output+args.application_name+'.conf', 'w')
upstart.write(pystache.render(template.read(), args))
upstart.close()

monit_out = open(output+args.application_name+'.monit.conf', 'w')
monit_out.write( pystache.render(monit.read(), args))

monit_out.close()

template.close()
#print args
