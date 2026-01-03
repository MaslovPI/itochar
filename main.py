from functions.equipment import generate_equipment
from functions.roll import roll, rollMultipleAccumulate


def main():
    strength = rollMultipleAccumulate(3, 6)
    dexterity = rollMultipleAccumulate(3, 6)
    willpower = rollMultipleAccumulate(3, 6)
    high = max(strength, dexterity, willpower)

    hit_protection = roll(6)
    print(f"Strength: {strength}")
    print(f"Dexterity: {dexterity}")
    print(f"Willpower: {willpower}")
    print(f"Highest Ability Score: {high}")
    print(f"Hit Protection: {hit_protection}")

    starter = generate_equipment(hit_protection, high)
    if starter:
        print(f"Starting package: {starter.content}")
        print(f"Has arcana: {starter.arcana}")


if __name__ == "__main__":
    main()
