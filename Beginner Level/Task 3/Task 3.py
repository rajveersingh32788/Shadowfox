# ══════════════════════════════════════════════
#   Justice League - List Operations
# ══════════════════════════════════════════════

def display_league(step, description, league):
    print(f"\n{'='*50}")
    print(f"  STEP {step}: {description}")
    print(f"{'='*50}")
    for i, hero in enumerate(league):
        leader_tag = " 👑 LEADER" if i == 0 else ""
        print(f"  [{i}] {hero}{leader_tag}")
    print(f"  Total Members: {len(league)}")
    print(f"{'='*50}")


# ── Original List ────────────────────────────
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("\n" + "="*50)
print("       JUSTICE LEAGUE OPERATIONS")
print("="*50)

display_league(0, "Original Justice League", justice_league)


# ── Step 1: Count Members ────────────────────
print(f"\n{'='*50}")
print(f"  STEP 1: Total Members in the Justice League")
print(f"{'='*50}")
total_members = len(justice_league)
print(f"  Number of members: {total_members}")
print(f"{'='*50}")


# ── Step 2: Add Batgirl & Nightwing ──────────
justice_league.append("Batgirl")
justice_league.append("Nightwing")
display_league(2, "Batman Recruited Batgirl & Nightwing", justice_league)


# ── Step 3: Wonder Woman becomes Leader ──────
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
display_league(3, "Wonder Woman Moves to the Front as Leader", justice_league)


# ── Step 4: Separate Aquaman & Flash ─────────
aquaman_index = justice_league.index("Aquaman")
flash_index   = justice_league.index("Flash")

first_index   = min(flash_index, aquaman_index)

# Remove Superman temporarily
justice_league.remove("Superman")

# Recalculate positions after removal
aquaman_index = justice_league.index("Aquaman")
flash_index   = justice_league.index("Flash")
first_index   = min(flash_index, aquaman_index)

# Insert Superman between Flash and Aquaman
justice_league.insert(first_index + 1, "Superman")
display_league(4, "Superman Placed Between Flash & Aquaman", justice_league)


# ── Step 5: Replace with New Team ────────────
justice_league.clear()
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
display_league(5, "Superman Assembles a Brand New Team!", justice_league)


# ── Step 6: Sort Alphabetically ──────────────
justice_league.sort()
display_league(6, "Justice League Sorted Alphabetically", justice_league)

print(f"\n  BONUS PREDICTION REVEAL:")
print(f"  The new leader is: '{justice_league[0]}'")
print(f"  (Alphabetically first among: Cyborg, Green Arrow, Hawkgirl, Martian Manhunter, Shazam)")
print(f"{'='*50}\n")