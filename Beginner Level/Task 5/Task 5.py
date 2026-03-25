# ══════════════════════════════════════════════
#   TASK 1: Simulating a Six-Sided Die Roll
# ══════════════════════════════════════════════

import random

rolls        = 20
count_six    = 0
count_one    = 0
count_double_six = 0
results      = []

print("=" * 45)
print("       🎲 DICE ROLLING SIMULATOR")
print("=" * 45)

for i in range(rolls):
    roll = random.randint(1, 6)
    results.append(roll)

    if roll == 6:
        count_six += 1
    if roll == 1:
        count_one += 1
    if i > 0 and results[i] == 6 and results[i - 1] == 6:
        count_double_six += 1

    print(f"  Roll {i+1:>2}: 🎲 {roll}")

print("=" * 45)
print("📊 Statistics After 20 Rolls:")
print(f"   🎯 Times rolled a 6        : {count_six}")
print(f"   1️⃣  Times rolled a 1        : {count_one}")
print(f"   🔥 Times rolled two 6s in a row: {count_double_six}")
print("=" * 45)


# ══════════════════════════════════════════════
#   TASK 2: Jumping Jacks Workout Routine
# ══════════════════════════════════════════════

print("\n" + "=" * 45)
print("       💪 JUMPING JACKS WORKOUT")
print("=" * 45)

total_jacks    = 100
set_size       = 10
completed      = 0

for set_num in range(1, (total_jacks // set_size) + 1):
    completed += set_size
    remaining  = total_jacks - completed

    print(f"\n  ✅ Set {set_num}: You just did {set_size} jumping jacks!")
    print(f"     Total completed so far: {completed}")

    # If all 100 are done, congratulate and stop
    if completed == total_jacks:
        print("\n" + "=" * 45)
        print("  🎉 Congratulations! You completed the workout!")
        print("=" * 45)
        break

    # Ask if tired
    tired = input("\n  😓 Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("  ⏭️  Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()

        if skip in ["yes", "y"]:
            print("\n" + "=" * 45)
            print(f"  🛑 You completed a total of {completed} jumping jacks.")
            print("=" * 45)
            break
        else:
            print(f"  💪 Great spirit! Keep going! {remaining} jumping jacks remaining.")

    else:
        print(f"  🔥 Amazing! {remaining} jumping jacks remaining. Keep it up!")