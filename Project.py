# definition of a project object
class Project:
    projectName = "Name"
    lastWorkedOn = "Can't remember"
    projectDescription = "Desc Go Here"
    whereDidILeaveIt = "Last thing done go here"
    nextSteps = "What to do next goes here"

    def __str__(self):
        s = "Project Name:\t\t" + self.projectName + "\n"
        s += "Last worked on:\t\t" + self.lastWorkedOn + "\n"
        s += "Description:\t\t" + self.projectDescription + "\n"
        s += "Where Did I Leave It:\t" + self.whereDidILeaveIt + "\n"
        s += "Next Steps:\t\t" + self.nextSteps + "\n\n"
        return s
