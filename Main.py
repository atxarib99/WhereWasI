# Python file
from File import FileIO
import sys


def main():
    arglen = len(sys.argv)
    # if not enough arguments, fail
    if arglen < 2:
        print("installation path not specified!")
        return
    # if two or more arguments are provided
    if arglen >= 2:
        # create FileIO
        x = FileIO(sys.argv[1])
        # name and path provided
        if arglen == 2:
            # list all projects with full path
            x.listAll()
        # if three arguments and third is 'list'
        elif arglen == 3 and sys.argv[2] == "list":
            # list all project names
            x.list()
        elif arglen == 3 and (sys.argv[2] == "new" or sys.argv[2] == "create"):
            x.createNew()
        elif arglen == 4 and sys.argv[2] == "update":
            x.updateProject(sys.argv[3])
        elif arglen == 4 and (sys.argv[2] == "delete" or sys.argv[2] == "remove"):
            x.deleteProject(sys.argv[3])
        elif arglen == 4 and (sys.argv[2] == "finish" or sys.argv[2] == "complete"):
            x.finishProject(sys.argv[3])
        else:
            # for each argument print the project with that project name
            x.listProjects(sys.argv[2:])


main()
