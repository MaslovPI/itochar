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


if __name__ == "__main__":
    main()
