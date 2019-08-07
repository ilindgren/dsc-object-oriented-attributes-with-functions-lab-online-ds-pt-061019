class School():
    def __init__(school, name = None, roster = {}):
        school.name = name
        school.roster = roster
    def add_student(grade, student):
        school.roster.append(grade, student)
            