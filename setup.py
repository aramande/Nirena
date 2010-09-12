from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["test/*"]

setup(name = "Project13",
    version = "0.1",
    description = "Puzzle Adventure Sidescrolling Platformer",
    author = "Aramande",
    author_email = "aramande@hackular.com",
    url = "Hackular.com",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    # packages = ['src'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    # package_data = {'src' : files },
    #'runner' is in the root.
    scripts = ["runner"],
    long_description = """2D adventurer based on puzzles, and the style is a sidescrolling platformer""" 
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 