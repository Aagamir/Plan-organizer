from enum import Enum
import random
import matplotlib.pyplot as plt

class ClassType(Enum):
    WYK = "Wykład"
    LAB = "Laboratorium"
    KONW = "Konwersatorium"
    LEK = "Lektorat"
    CW = "Ćwiczenia"
    SEM = "Seminarium"

class Group:
    def __init__(self, id, name, start, end, capacity, day, slots, type):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.capacity = capacity
        self.priority = 0
        self.students = []
        self.day = day
        self.slots = slots
        self.type = type

    def is_available(self):
        return self.slots > 0

    def add_slots(self, slots):
        self.slots += slots

    def conflicts_with(self, other):
        return self.day == other.day and not (other.end <= self.start or other.start >= self.end)

    def day_name(self):
        day_labels = {
            1: "Poniedziałek",
            2: "Wtorek",
            3: "Środa",
            4: "Czwartek",
            5: "Piątek",
            6: "Sobota",
            7: "Niedziela"
        }
        return day_labels.get(self.day, f"Dzień {self.day}")

class Subject:
    def __init__(self, name, obligatory=False):
        self.name = name
        self.obligatory = obligatory
        self.groups = []

    def add_group(self, *groups):
        for g in groups:
            if isinstance(g, (list, tuple)):
                for gg in g:
                    self.groups.append(gg)
            else:
                self.groups.append(g)

    def groups_by_type(self):
        result={}
        for g in self.groups:
            result.setdefault(g.type, []).append(g)
        return result

    def get_group_types(self):
        """Zwraca listę unikalnych typów zajęć w tym przedmiocie, posortowaną po nazwie."""
        return sorted(set(g.type for g in self.groups), key=lambda t: t.name)

    def get_groups_by_type(self, gtype):
        """Zwraca listę grup danego typu (np. wszystkie LABy)."""
        return [g for g in self.groups if g.type == gtype]

class Student:
    def __init__(self, index):
        self.index = index
        self.schedule = []
        self.assigned_groups = {}  # {przedmiot: grupa}

    def has_conflict(self, group):
        for g in self.schedule:
            if g.day == group.day and not (group.end <= g.start or group.start >= g.end):
                return True
        return False



    def release_slots(self):
        for subject, groups in list(self.assigned_groups.items()):
            for group in groups:
                group.slots += 1
                if self in group.students:
                    group.students.remove(self)
        self.schedule = []
        self.assigned_groups = {}

class Plan:
    def __init__(self, students, subjects):
        self.students = students
        self.subjects = subjects

    def assign(self, student, subject, group):
        if not group.is_available():
            return False
        if student.has_conflict(group):
            return False

        existing = self._get_assigned_list(student, subject)
        for eg in existing:
            if eg.type == group.type:
                return False
        group.students.append(student)
        student.schedule.append(group)
        existing.append(group)
        group.slots -= 1
        return True

    def unassign(self, student, subject, group):
        if group in student.schedule:
            student.schedule.remove(group)
        if student in group.students:
            group.students.remove(student)
        if subject in student.assigned_groups and group in student.assigned_groups[subject]:
            student.assigned_groups[subject].remove(group)
            if not student.assigned_groups[subject]:
                del student.assigned_groups[subject]
        group.slots += 1

    def _get_assigned_list(self, student, subject):
        return student.assigned_groups.setdefault(subject, [])

    def visualize(self, student):
        fig, ax = plt.subplots(figsize=(12, 6))

        # mapowanie dni tygodnia
        day_labels = {
            1: "Poniedziałek",
            2: "Wtorek",
            3: "Środa",
            4: "Czwartek",
            5: "Piątek",
            6: "Sobota",
            7: "Niedziela"
        }
        positions = {d: i for i, d in enumerate(day_labels.keys())}

        # kolory do różnych typów zajęć
        colors = {
            "WYK": "skyblue",
            "LAB": "lightgreen",
            "KONW": "lightcoral",
            "CW": "khaki",
            "LEK": "plum",
            "SEM": "orange"
        }

        for g in student.schedule:
            x = positions[g.day]
            ax.bar(
                x=x,
                height=g.end - g.start,
                bottom=g.start,
                width=0.6,
                color=colors.get(g.type, "gray"),
                edgecolor="black",
                align="center"
            )
            ax.text(
                x,
                g.start + 0.05,
                f"{g.name}",
                va="bottom", ha="center", fontsize=8
            )

        ax.set_ylabel("Godzina")
        ax.set_ylim(8, 20)
        ax.set_xticks(list(positions.values()))
        ax.set_xticklabels([day_labels[d] for d in positions.keys()])
        ax.set_title(f"Plan studenta {student.index}")

        ax.grid(True, which='both', axis='y', linestyle='--', color='gray', alpha=0.5)
        ax.set_axisbelow(True)  # słupki będą nad siatką

        plt.tight_layout()
        plt.show()



    def assign_student_to_subject(self, student, subject):
        """
        Przypisuje studenta do wszystkich typów zajęć danego przedmiotu (WYK, LAB, KONW, SEM).
        Zwraca True jeśli udało się przypisać wszystkie wymagane grupy, False jeśli nie.
        """
        needed_types = subject.get_group_types()
        assigned = []

        for gtype in needed_types:
            available_groups = subject.get_groups_by_type(gtype)
            # wybieramy tylko grupy z wolnymi slotami
            available_groups = [g for g in available_groups if g.slots > 0]

            if not available_groups:
                print(f"  ⚠️ Brak wolnych grup typu {gtype} dla przedmiotu '{subject.name}'")
                return False

            assigned_this_type = False
            for g in available_groups:
                if not student.has_conflict(g):
                    # przypisz grupę
                    student.schedule.append(g)
                    g.students.append(student)
                    g.slots -= 1
                    assigned.append(g)
                    assigned_this_type = True
                    break
                else:
                    # 🔍 znajdź i wypisz kolidującą grupę
                    for existing in student.schedule:
                        if existing.conflicts_with(g):
                            print(
                                f"  ⛔ Kolizja: {g.name} ({g.day_name()} {g.start}-{g.end}) "
                                f"z {existing.name} ({existing.day_name()} {existing.start}-{existing.end})"
                            )

            if not assigned_this_type:
                print(f"  ❌ Nie udało się przypisać typu {gtype} dla '{subject.name}'")
                # usuń wcześniej przypisane grupy tego przedmiotu, by nie zostawić niepełnych
                for g in assigned:
                    g.students.remove(student)
                    g.slots += 1
                    student.schedule.remove(g)
                return False

        return True





    # def assign_student_to_subject(self, student, subject):
    #     """Przypisuje studenta do wszystkich typów zajęć z danego przedmiotu."""
    #     grouped = subject.groups_by_type()
    #
    #     for class_type, groups in grouped.items():
    #         # losujemy lub wybieramy najmniej zatłoczoną grupę
    #         possible = [g for g in groups if g.slots > 0 and not student.has_conflict(g)]
    #         if not possible:
    #             return False  # brak dostępnych grup dla tego typu zajęć
    #
    #         chosen = min(possible, key=lambda g: len(g.students))
    #         self.assign(student, subject, chosen)
    #     return True

    def evaluate(self):
        score = 0
        for s in self.students:
            s.schedule.sort(key=lambda g: g.start)
            for i in range(len(s.schedule)-1):
                gap = s.schedule[i+1].start - s.schedule[i].end
                if gap > 1:
                    score -= gap
        return score

