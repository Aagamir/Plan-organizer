import mod
import subjects as subj
import students as studs
import itertools
import matplotlib.pyplot as plt

class PlanBuilder(mod.Plan):
    def generate(self):
        """Rozpoczyna generowanie planu dla wszystkich studentów"""
        return self._assign_recursive(0)

    def _assign_recursive(self, student_idx):
        if student_idx == len(self.students):
            return True  # wszyscy studenci mają plan

        student = self.students[student_idx]
        obligatory_subjects = [s for s in self.subjects if s.obligatory]

        # Dla każdego przedmiotu przygotowujemy listę grup pogrupowanych po typie
        subject_choices = []
        for subject in obligatory_subjects:
            types = subject.groups_by_type()
            # jeśli któryś typ nie ma żadnej grupy -> brak możliwości
            if any(len(lst) == 0 for lst in types.values()):
                return False
            # wszystkie możliwe kombinacje po jednej grupie z każdego typu
            choices = list(itertools.product(*types.values()))
            subject_choices.append((subject, choices))

        # próbujemy wszystkie kombinacje dla tego studenta
        return self._try_combinations(student_idx, student, subject_choices)

    def _try_combinations(self, student_idx, student, subject_choices, subj_idx=0):
        if subj_idx == len(subject_choices):
            # ocena planu studenta
            if self.evaluate_student(student) >= -2:  # np. dopuszczalne małe przerwy
                return self._assign_recursive(student_idx + 1)
            else:
                return False

        subject, choices = subject_choices[subj_idx]
        for choice in choices:
            valid = True
            used = []

            for g in choice:
                if g.slots <= 0 or student.has_conflict(g):
                    valid = False
                    break
                ok = self.assign(student, subject, g)
                if not ok:
                    valid = False
                    break
                used.append((subject, g))

            if valid and self._try_combinations(student_idx, student, subject_choices, subj_idx + 1):
                return True

            # cofnij przypisania (backtracking)
            for subject_used, g in used:
                self.unassign(student, subject_used, g)

        return False

    def evaluate_student(self, student):
        """Ocena planu – im mniej przerw, tym lepiej"""
        score = 0
        student.schedule.sort(key=lambda g: (g.day, g.start))
        for i in range(len(student.schedule) - 1):
            if student.schedule[i].day == student.schedule[i+1].day:
                gap = student.schedule[i+1].start - student.schedule[i].end
                if gap > 0.5:
                    score -= gap
        return score


def main():
    all_students = studs.students
    all_subjects = [
        subj.bazy_danych,
        subj.fizyka_issp_3,
        subj.pracownia_fiz,
        subj.metody_numeryczne,
        subj.pracownia_ele,
        subj.programowanie_ai,
        subj.rachunek_pr,
        subj.wstep_ele,
    ]

    plan = mod.Plan(all_students, all_subjects)

    print("🔧 Rozpoczynam generowanie planów...\n")

    all_ok = True

    for student in all_students:
        print(f"📅 Układam plan dla studenta {student.index}...")
        print("  Przedmioty:", [s.name for s in all_subjects])

        success = True
        for subject in all_subjects:
            ok = plan.assign_student_to_subject(student, subject)
            if not ok:
                print(f"  ⚠️ Nie udało się przypisać {student.index} do wszystkich grup przedmiotu '{subject.name}'")
                success = False

        if success:
            print(f"  ✅ Ułożono poprawny plan dla {student.index}")
            #plan.visualize(student)
        else:
            print(f"  ❌ Plan dla {student.index} jest niekompletny (brak wolnych miejsc lub kolizje)")
            all_ok = False


    print("\n🔹 Wizualizacja planów wszystkich studentów:")
    plan.visualize_all()
    figures = []
    for student in all_students:
        fig = plan.visualize(student)
        figures.append(fig)

    # Pokaż wszystkie figury naraz
    plt.show()  # wszystkie otworzą się w osobnych oknach

    if all_ok:
        print("\n✅ Wszystkim studentom ułożono poprawne plany!")
    else:
        print("\n⚠️ Nie wszystkim studentom udało się ułożyć pełny plan.")



if __name__ == "__main__":
    main()
