#from nirena.game import run
import os
import sys
import unittest
import discover
import optparse
import nirena.util.parser

p = optparse.OptionParser()
p.add_option('--test', '-t', action ='store_true', help='run the game through all tests')
options, arguments = p.parse_args()
result = unittest.TestResult()
if options.test == True:
	temp_argv = sys.argv
	sys.argv = [sys.argv[0]] #fix: Arguments sent along to test-loaders.
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
#else:
#	run()