import mod

#BAZY DANYCH
bazy_danych = mod.Subject("Bazy danych", obligatory=True)
wyklad_bd = mod.Group(10,"Wykład - Bazy Danych", start=10.00, end=10.45, capacity=50, day=3, slots=50)
bazy_danych.add_group(wyklad_bd)

BD_lab1 = mod.Group(11, "Bazy Danych LAB 1 Środa", start=13.00, end=14.45, capacity=12, day=3, slots=0)
BD_lab2 = mod.Group(12, "Bazy Danych LAB 2 Czwartek", start=15.00, end=16.45, capacity=12, day=4, slots=0)
BD_lab3 = mod.Group(13, "Bazy Danych LAB 3 Środa", start=11.00, end=12.45, capacity=12, day=3,slots=0)

bazy_danych.add_group(BD_lab1)
bazy_danych.add_group(BD_lab2)
bazy_danych.add_group(BD_lab3)

#FIZYKA DLA ISSP 3
fizyka_issp_3 = mod.Subject("Fizyka ISSP 3", obligatory=True)
wyklad_fiz = mod.Group(20,"Wykład - Fizyka ISSP 3", start=15.00, end=16.45, capacity=50, day=3, slots=50)
fizyka_issp_3.add_group(wyklad_fiz)

FIZ_konw1 = mod.Group(21,"Fizyka KONW 1 Poniedziałek", start=12.00, end=13.45, capacity=15, day=1, slots=0 )
FIZ_konw2 = mod.Group(22,"Fizyka KONW 2 Poniedziałek", start=12.00, end=13.45, capacity=15, day=1, slots=0 )
fizyka_issp_3.add_group(FIZ_konw1)
fizyka_issp_3.add_group(FIZ_konw2)

FIZ_lab1 = mod.Group(23, "Fizyka LAB 1 Środa", start=11.15, end=12.45, capacity=10, day=3, slots=0)
FIZ_lab2 = mod.Group(24, "Fizyka LAB 2 Środa", start=13.00, end=14.45, capacity=10, day=3, slots=0)
FIZ_lab3 = mod.Group(25, "Fizyka LAB 3 Środa", start=13.00, end=14.45, capacity=10, day=3,slots=0)

fizyka_issp_3.add_group(FIZ_lab1)
fizyka_issp_3.add_group(FIZ_lab2)
fizyka_issp_3.add_group(FIZ_lab3)

#I PRACOWNIA FIZ
pracownia_fiz = mod.Subject("Pracownia FIZ", obligatory=True)
PRAC_lab1 = mod.Group(31, "Pracownia Fizyczna 1 Czwartek", start=10.30, end=12.45, capacity=10, day=4, slots=0)
PRAC_lab2 = mod.Group(32, "Pracownia Fizyczna 2 Czwartek", start=8.00, end=10.15, capacity=10, day=4, slots=0)
PRAC_lab3 = mod.Group(33, "Pracownia Fizyczna 3 Czwartek", start=8.00, end=10.15, capacity=10, day=4, slots=0)
PRAC_lab4 = mod.Group(34, "Pracownia Fizyczna 4 Czwartek", start=10.30, end=12.45, capacity=10, day=4, slots=0)

pracownia_fiz.add_group(PRAC_lab1)
pracownia_fiz.add_group(PRAC_lab2)
pracownia_fiz.add_group(PRAC_lab3)
pracownia_fiz.add_group(PRAC_lab4)

#JĘZYKI JEZELI BEDZIE TRZEBA


#METODY NUMERYCZNE
metody_numeryczne = mod.Subject("Metody Numeryczne", obligatory=True)
wyklad_mn = mod.Group(50,"Wykład - Metody Numeryczne", start=12.00, end=13.45, capacity=50, day=5, slots=50)

MN_lab1 = mod.Group(51, "Metody Numeryczne LAB 1 Wtorek", start=8.15, end=10.00, capacity=12, day=2, slots=0)
MN_lab2 = mod.Group(52, "Metody Numeryczne LAB 2 Czwartek", start=13.00, end=14.45, capacity=12, day=4, slots=0)
MN_lab3 = mod.Group(53, "Metody Numeryczne LAB 3 Wtorek", start=16.15, end=17.45, capacity=12, day=3,slots=0)
metody_numeryczne.add_group([wyklad_mn, MN_lab1, MN_lab2, MN_lab3])

#PRACOWNIA ELEKTRONICZNA
pracownia_ele = mod.Subject("Pracownia ELE", obligatory=True)
PRAC_E_lab1 = mod.Group(61, "Pracownia Elektroniczna 1 Środa", start=13.00, end=15.15, capacity=8, day=3, slots=0)
PRAC_E_lab2 = mod.Group(62, "Pracownia Elektroniczna 2 Czwartek", start=13.00, end=15.15, capacity=8, day=4, slots=0)
PRAC_E_lab3 = mod.Group(63, "Pracownia Elektroniczna 3 Czwartek", start=10.30, end=12.45, capacity=8, day=4, slots=0)
PRAC_E_lab4 = mod.Group(64, "Pracownia Elektroniczna 4 Czwartek", start=8.00, end=10.15, capacity=8, day=4, slots=0)
pracownia_ele.add_group([PRAC_E_lab1, PRAC_E_lab2, PRAC_E_lab3, PRAC_E_lab4])

#PROGRAMOWANIE APLIKACJI INTERNETOWYCH
programowanie_ai = mod.Subject("Programowanie aplikacji internetowych", obligatory=True)
PAI_wyklad = mod.Group(70, "Wykład - PAI", 12.15, 13.00, 50, 2, 50)         # Wtorek
PAI_lab1   = mod.Group(71, "PAI Laboratorium 1 Wtorek", 10.15, 12.00, 12, 2, 0)  # Wtorek
PAI_lab2   = mod.Group(72, "PAI Laboratorium 2 Czwartek", 13.00, 14.45, 12, 4, 0) # Czwartek
PAI_lab3   = mod.Group(73, "PAI Laboratorium 3 Poniedziałek", 14.00, 15.45, 12, 1, 0) # Poniedziałek

programowanie_ai.add_group([PAI_wyklad, PAI_lab1, PAI_lab2, PAI_lab3])

#RACHUNEK PRAWDOPODOBIENSTWA
rachunek_pr = mod.Subject("Rachunek Prawdopodobienstwa", obligatory=True)


