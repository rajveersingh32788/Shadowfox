# ══════════════════════════════════════════════
#   TASK 1: Friends List & Tuples
# ══════════════════════════════════════════════

friends = ["Aditya", "Rahul", "Priya", "Sneha", "Vikram", "Ananya"]

# Create list of tuples: (name, length of name)
friends_tuples = [(name, len(name)) for name in friends]

print("=" * 45)
print("        👫 FRIENDS NAME & LENGTH")
print("=" * 45)
for name, length in friends_tuples:
    print(f"  {name:<12} --> Length: {length}")
print("=" * 45)


# ══════════════════════════════════════════════
#   TASK 2: Trip Expense Tracker
# ══════════════════════════════════════════════

your_expenses = {
    "Hotel"          : 1200,
    "Food"           : 800,
    "Transportation" : 500,
    "Attractions"    : 300,
    "Miscellaneous"  : 200
}

partner_expenses = {
    "Hotel"          : 1000,
    "Food"           : 900,
    "Transportation" : 600,
    "Attractions"    : 400,
    "Miscellaneous"  : 150
}


# ── Total Expenses ───────────────────────────
your_total     = sum(your_expenses.values())
partner_total  = sum(partner_expenses.values())

print("\n" + "=" * 45)
print("        ✈️  TRIP EXPENSE TRACKER")
print("=" * 45)

print("\n📋 Expense Breakdown:")
print(f"  {'Category':<18} {'You':>8} {'Partner':>10}")
print("  " + "-" * 38)
for category in your_expenses:
    print(f"  {category:<18} ₹{your_expenses[category]:>6}   ₹{partner_expenses[category]:>6}")

print("  " + "-" * 38)
print(f"  {'TOTAL':<18} ₹{your_total:>6}   ₹{partner_total:>6}")


# ── Who Spent More ───────────────────────────
print("\n" + "=" * 45)
print("💰 Total Expense Summary:")
print(f"   Your Total     : ₹{your_total}")
print(f"   Partner's Total: ₹{partner_total}")

if your_total > partner_total:
    print(f"\n   🏆 YOU spent more by ₹{your_total - partner_total}!")
elif partner_total > your_total:
    print(f"\n   🏆 YOUR PARTNER spent more by ₹{partner_total - your_total}!")
else:
    print("\n   🤝 Both of you spent equally!")


# ── Biggest Spending Difference ──────────────
print("\n" + "=" * 45)
print("📊 Category-wise Difference:")
print(f"  {'Category':<18} {'Difference':>10}")
print("  " + "-" * 30)

differences = {}
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    differences[category] = diff
    print(f"  {category:<18} ₹{diff:>6}")

# Find max difference category
max_diff_category = max(differences, key=differences.get)
max_diff_value    = differences[max_diff_category]

print("\n" + "=" * 45)
print("🔍 Biggest Spending Gap:")
print(f"   Category  : {max_diff_category}")
print(f"   Difference: ₹{max_diff_value}")
print(f"   You spent ₹{your_expenses[max_diff_category]} vs Partner's ₹{partner_expenses[max_diff_category]}")
print("=" * 45)