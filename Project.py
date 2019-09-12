# definition of a project object
class Project:
    projectName = "Name"
    projectDescription = "Desc Go Here"
    projectPath = "/path/to/project"
    lastWorkedOn = "Can't remember"
    gitLog = ""
    whereDidILeaveIt = "Last thing done go here"
    nextSteps = "What to do next goes here"

    def __str__(self):
        s = "Project Name:\t\t" + self.projectName + "\n"
        s += "Description:\t\t" + self.projectDescription + "\n"
        s += "Path:\t\t\t" + self.projectPath + "\n"
        s += "Last worked on:\t\t" + self.lastWorkedOn + "\n"
        if self.gitLog != "":
            s += "Last 5 git logs:\t" + self.gitLog.replace("\n", "\n\t\t\t") + "\n"
        s += "Where Did I Leave It:\t" + self.whereDidILeaveIt + "\n"
        s += "Next Steps:\t\t" + self.nextSteps + "\n\n"
        return s
