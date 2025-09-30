import mod
import subjects

print("Grupy dla przedmiotu:", subjects.bazy_danych.name)
for group in subjects.bazy_danych.groups:
    print(f"- {group.name} (dzień {group.day}, {group.start}-{group.end}, capacity {group.capacity}, free slots {group.slots})")