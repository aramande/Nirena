#import run from nirena.game
import sys
import unittest
import discover
import optparse

p = optparse.OptionParser()
p.add_option('--test', '-t', action ='store_true', help='run the game through all tests')
options, arguments = p.parse_args()
result = unittest.TestResult()
if options.test == True:
	temp_argv = sys.argv
	sys.argv = [sys.argv[0]] #fix: Arguments sent along to nose, breaking nose.
	dtl = discover.DiscoveringTestLoader()
	dtl.discover("nirena/test", "*_test.py").run(result)
	print "test:", result
	sys.argv = temp_argv
#else:
#	run()