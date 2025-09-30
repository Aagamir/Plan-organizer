class Group:
    def __init__(self, id, name, start, end, capacity, day, slots):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.capacity = capacity
        self.priority = 0
        self.students = []
        self.day = day
        self.slots = slots

    def is_available(self):
        return len(self.students) < self.capacity

    def add_slots(self, slots):
        self.slots += slots

class Subject:
    def __init__(self, name, obligatory=False):
        self.name = name
        self.obligatory = obligatory
        self.groups = []

    def add_group(self, group):
        for g in group:
            self.groups.append(g)

class Student:
    def __init__(self, index):
        self.index = index
        self.schedule = []
        self.assigned_groups = {} #{przedmiot: grupa}

        def has_conflict(self, group):
            for g in self.schedule:
                if not (group.end <= g.start or group.start >= g.end):
                    return True
                return False

class Plan:
    def __init__(self, students, subjects):
        self.students = students
        self.subjects = subjects

    def assign(self, student, subject, group):
        if subject in student.assigned_groups:
            return False

        if group.is_available():
            return False

        if student.has_conflict(group):
            return False

        group.students.append(student)
        student.schedule.append(group)
        student.assigned_groups[subject] = group

        return True

    def evaluate(self):
        score = 0
        for s in self.students:
            s.schedule.sort(key=lambda g: g.start)
            for i in range(len(s.schedule)-1):
                gap = s.schedule[i+1].start - s.schedule[i].end
                if gap > 1:
                    score -= gap
        return score

