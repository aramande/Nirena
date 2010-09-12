#!/usr/bin/env python
import src.main
import optparse
	
p = optparse.OptionParser()
p.add_option('--test', '-t', action ='store_true', help='run the game through all tests')
options, arguments = p.parse_args()
if options.test == True:
	temp_argv = sys.argv
	sys.argv = [sys.argv[0]]
	nose.main()
	sys.argv = temp_argv
else:
	src.main.rungame()