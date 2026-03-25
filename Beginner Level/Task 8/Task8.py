class Avenger:
    # Class variable - Captain America is the leader
    leader = "Captain America"
    
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
    
    def get_info(self):
        print("=" * 40)
        print(f"  🦸 SUPERHERO: {self.name}")
        print("=" * 40)
        print(f"  Age       : {self.age}")
        print(f"  Gender    : {self.gender}")
        print(f"  Super Power: {self.super_power}")
        print(f"  Weapon    : {self.weapon}")
        print(f"  Leader    : {'Yes 👑' if self.is_leader() else 'No'}")
        print("=" * 40)
        print()
    
    def is_leader(self):
        return self.name == Avenger.leader


# ── Creating the 6 Avengers ──────────────────────────────
super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]

captain_america = Avenger(
    name="Captain America",
    age=105,
    gender="Male",
    super_power="Super Strength",
    weapon="Shield"
)

iron_man = Avenger(
    name="Iron Man",
    age=48,
    gender="Male",
    super_power="Technology",
    weapon="Armor"
)

black_widow = Avenger(
    name="Black Widow",
    age=36,
    gender="Female",
    super_power="Superhuman Agility",
    weapon="Batons"
)

hulk = Avenger(
    name="Hulk",
    age=49,
    gender="Male",
    super_power="Unlimited Strength",
    weapon="No Weapon"
)

thor = Avenger(
    name="Thor",
    age=1500,
    gender="Male",
    super_power="Super Energy",
    weapon="Mjölnir"
)

hawkeye = Avenger(
    name="Hawkeye",
    age=47,
    gender="Male",
    super_power="Fighting Skills",
    weapon="Bow and Arrows"
)


# ── Display all Avengers ─────────────────────────────────
avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

print("\n" + "🌟" * 20)
print("       WELCOME TO THE AVENGERS TEAM")
print("🌟" * 20 + "\n")

for hero in avengers_team:
    hero.get_info()

# ── Check who is the leader ──────────────────────────────
print("\n🔍 Checking Leadership...\n")
for hero in avengers_team:
    if hero.is_leader():
        print(f"  👑 {hero.name} IS the leader of the Avengers!")
    else:
        print(f"  ✅ {hero.name} is a valued member but NOT the leader.")