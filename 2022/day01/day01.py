def top_three(elves_list):
    gold = max(elves_list)
    elves_list.remove(gold)
    silver = max(elves_list)
    elves_list.remove(silver)
    bronze = max(elves_list)
    elves_list.remove(bronze)
    return gold + silver + bronze



with open("input_day01.txt") as f:
    lines = f.readlines()
current_elf = 0
all_elves = []
for i in lines:
    if i.strip() == '':
        all_elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(i.strip())
print(all_elves)
print(top_three(elves_list=all_elves))


