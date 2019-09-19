# File IO Python
from Project import Project
import datetime
import os
import fnmatch


class FileIO:
    # iterate through the installation directory and pull every .myproj file
    installationDirectory = ""

    def __init__(self, installationDirectory):
        self.installationDirectory = installationDirectory

    # list all of the projects that can be found
    def listAll(self):
        # for each file in the directory
        for file in os.listdir(self.installationDirectory):
            # if the file is a .myproj file
            if file.endswith(".myproj"):
                # read and output
                self.readAndPrintFile(self.installationDirectory + os.sep + file)

    # list all of the projects with project names given
    def listProjects(self, names):
        # for each file in the directory
        for file in os.listdir(self.installationDirectory):
            # if the file is a .myproj file
            if file.endswith(".myproj"):
                for name in names:
                    if file == name or (name + ".myproj") == file:
                        # read and output
                        self.readAndPrintFile(self.installationDirectory + os.sep + file)
                        break

    # list all the project names
    def list(self):
        # for each file in the directory
        for file in os.listdir(self.installationDirectory):
            # if the file is a .myproj file
            if file.endswith(".myproj"):
                # read and output
                print(file)

    # opens a file, reads its contents, and outputs a formatted copy
    def readAndPrintFile(self, file):
        # open file
        f = open(file, "r")
        # create project obj
        p = Project()
        # for each line in the file
        for line in f.readlines():
            # split by the ":"
            split = line.split(":")
            # assign attributes
            if split[0] == "ProjectName":
                p.projectName = split[1]
            elif split[0] == "LastWorkedOn":
                p.lastWorkedOn = split[1]
            elif split[0] == "Description":
                p.projectDescription = split[1]
            elif split[0] == "Path":
                p.projectPath = split[1]
                p.gitLog = self.getLogFile(p.projectPath)
            elif split[0] == "WhereDidILeaveIt":
                p.whereDidILeaveIt = split[1]
            elif split[0] == "NextSteps":
                p.nextSteps = split[1]
        # print the project
        print(p)
        # close the file!
        f.close()

    def readFile(self, file):
        # open file
        f = open(file, "r")
        # create project obj
        p = Project()
        # for each line in the file
        for line in f.readlines():
            # split by the ":"
            split = line.split(":")
            # assign attributes
            if split[0] == "ProjectName":
                p.projectName = split[1]
            elif split[0] == "LastWorkedOn":
                p.lastWorkedOn = split[1]
            elif split[0] == "Path":
                p.projectPath = split[1]
                p.gitLog = self.getLogFile(p.projectPath)
            elif split[0] == "Description":
                p.projectDescription = split[1]
            elif split[0] == "WhereDidILeaveIt":
                p.whereDidILeaveIt = split[1]
            elif split[0] == "NextSteps":
                p.nextSteps = split[1]
        # close the file!
        f.close()
        # return created project
        return p

    def createNew(self):
        p = Project()
        p.projectName = input("ProjectName: ")
        p.projectDescription = input("Description: ")
        p.projectPath = input("Absolute Path: ")
        dt = str(datetime.datetime.now().isoformat()).replace(":", ".")
        p.lastWorkedOn = input("LastWorkedOn [" + dt + "]: ")
        if p.lastWorkedOn == "":
            p.lastWorkedOn = dt
        p.whereDidILeaveIt = input("WhereDidILeaveIt: ")
        p.nextSteps = input("NextSteps: ")
        f = open(self.installationDirectory + p.projectName + ".myproj", 'w+')
        f.write("ProjectName:" + p.projectName + "\n")
        f.write("Description:" + p.projectDescription + "\n")
        f.write("Path:" + p.projectPath + "\n")
        f.write("LastWorkedOn:" + p.lastWorkedOn + "\n")
        f.write("WhereDidILeaveIt:" + p.whereDidILeaveIt + "\n")
        f.write("NextSteps:" + p.nextSteps + "\n")
        f.close()

    def updateProject(self, projectName):
        # for each file in the directory
        for file in os.listdir(self.installationDirectory):
            # if the file is a .myproj file
            pname = projectName
            if not pname.endswith(".myproj"):
                pname = pname + ".myproj"
            if file == pname:
                newp = Project()
                p = self.readFile(self.installationDirectory + os.sep + file)
                newp.projectName = input("ProjectName[" + p.projectName.replace("\n", "") + "]: ")
                if newp.projectName == "":
                    newp.projectName = p.projectName
                newp.projectDescription = input("Description[" + p.projectDescription[0:10].replace("\n", "") + "...]: ")
                if newp.projectDescription == "":
                    newp.projectDescription = p.projectDescription
                newp.projectPath = input("Path[" + p.projectPath.replace("\n", "") + "...]: ")
                if newp.projectPath == "":
                    newp.projectPath = p.projectPath
                dt = str(datetime.datetime.now().isoformat()).replace(":", ".")
                newp.lastWorkedOn = input("LastWorkedOn[" + p.lastWorkedOn.replace("\n", "") + "]: ")
                if newp.lastWorkedOn == "":
                    newp.lastWorkedOn = dt
                newp.whereDidILeaveIt = input("WhereDidILeaveIt[" + p.whereDidILeaveIt[0:10].replace("\n", "") + "...]: ")
                if newp.whereDidILeaveIt == "":
                    newp.whereDidILeaveIt = p.whereDidILeaveIt
                newp.nextSteps = input("NextSteps[" + p.nextSteps[0:10].replace("\n", "") + "...]: ")
                if newp.nextSteps == "":
                    newp.nextSteps = p.nextSteps
                f = open(self.installationDirectory + os.sep + file, "w")
                f.write("ProjectName:" + newp.projectName + "\n")
                f.write("Description:" + newp.projectDescription + "\n")
                f.write("Path:" + newp.projectPath + "\n")
                f.write("LastWorkedOn:" + newp.lastWorkedOn + "\n")
                f.write("WhereDidILeaveIt:" + newp.whereDidILeaveIt + "\n")
                f.write("NextSteps:" + newp.nextSteps + "\n")
                f.close()
                return
        print("No project found with that name!")

    def finishProject(self, projectName):
        for file in os.listdir(self.installationDirectory):
            # if the file is a .myproj file
            pname = projectName
            if not pname.endswith(".myproj"):
                pname = pname + ".myproj"
            if file == pname:
                os.rename(self.installationDirectory + os.sep + pname, self.installationDirectory + os.sep + pname + "arc")

    def deleteProject(self, projectName):
        for file in os.listdir(self.installationDirectory):
            # if the file is a .myproj file
            pname = projectName
            if not pname.endswith(".myproj"):
                pname = pname + ".myproj"
            if file == pname:
                os.remove(self.installationDirectory + os.sep + pname)

    def getLogFile(self, path):
        pathToHead = path.replace("\n", "") + "/.git/logs/HEAD"
        if not (os.path.exists(pathToHead) and os.path.isfile(pathToHead)):
            return ""
        o = open(pathToHead, "r")
        lineCount = len(o.readlines())
        o.seek(0)
        while lineCount > 5:
            o.readline()
            lineCount -= 1
        s = ""
        while lineCount > 0:
            s += o.readline().split("\t")[1]
            lineCount -= 1
        return s




