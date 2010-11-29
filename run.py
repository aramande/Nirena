#!/usr/bin/env python
#from nirena.game import run
import os
import sys
import unittest
import optparse
import nirena.util.parser
from discover import discover

p = optparse.OptionParser()
p.add_option('--test', '-t', action ='store_true', help='run the game through all tests')
p.add_option('--version', '-v', action ='store_true', help='print the current version number')
options, arguments = p.parse_args()
version = {}
version['name'] = "Nirena"
version['tag'] = "Alpha"
version['major'] = "0"
version['minor'] = "2"
version['bugfix'] = "0"
vnum = " v"+version['major']+"."+version['minor']
if version['bugfix'] != "":
	vnum += "."+version['bugfix']
vstr = version['name']+" "+version['tag']+vnum
if options.test == True:
	temp_argv = sys.argv
	sys.argv = [sys.argv[0]] #fix: Arguments sent along to test-loaders.
	result = unittest.TestResult()
	dtl = discover.DiscoveringTestLoader()
	dtl.discover("nirena/test", "*_test.py").run(result)
	print "-"*20
	print "Running all tests"
	if len(result.errors) != 0:
		for error in result.errors:
			for line in error:
				print line
	if len(result.failures) != 0:
		for fail in result.failures:
			for line in fail:
				print line
	print "Out of the", result.testsRun, "tests run, you got", len(result.errors), 
	print "errors and", len(result.failures), "failures."
	if(len(result.errors) == 0 and len(result.failures) == 0):
		print "You are awesome!!"
	print "-"*20
	sys.argv = temp_argv
elif options.version == True:
	print vstr
#else:
#	run()
