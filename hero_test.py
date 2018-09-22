
import pytest
import io
import sys
import SuperHeroes

# Helper Function


def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()

# Test Abilities Class


def test_ability_instance():
    # Test instantiation without error
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 300)
    assert big_strength


def test_ability_name():
    # Test for Correct Name
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 300)
    assert big_strength.name == "Overwhelming Strength"


def test_ability_update_attack():
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 300)
    big_strength.update_attack(400)
    test_runs = 100
    attack = 0
    for _ in range(0, test_runs):
        attack += big_strength.attack()
    assert attack <= (400 * test_runs) and attack >= (200 * test_runs)


def test_ability_attack():
    # Test for correct attack value
    test_runs = 100
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 400)
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack <= 400 and attack >= 200

# Test Weapons Class


def test_weapon_instance():
    big_stick = SuperHeroes.Weapon("Overwhelming Stick", 200)
    assert "Weapon" in str(big_stick)


def test_weapon_attack():
    big_stick = SuperHeroes.Weapon("Overwhelming Stick", 200)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_stick.attack()
        assert attack <= 200 and attack >= 0

# Test Heroes Class


def test_hero_instance():
    Athena = SuperHeroes.Hero("Athena")
    assert Athena


def test_hero_add_ability():
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 300)
    Athena = SuperHeroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_add_multi_ability():
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 300)
    speed = SuperHeroes.Ability("Lightning Speed", 500)
    Athena = SuperHeroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    Athena.add_ability(speed)
    assert len(Athena.abilities) == 2
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_attack_ability():
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 30000)
    athena = SuperHeroes.Hero("Athena")
    assert athena.attack() == 0
    athena.add_ability(big_strength)
    attack = athena.attack()
    assert attack <= 30000 and attack >= 15000


def test_hero_attack_weapon():
    big_strength = SuperHeroes.Ability("Overwhelming Strength", 200)
    Athena = SuperHeroes.Hero("Athena")
    Athena.add_ability(big_strength)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack <= 200 and attack >= 0


def test_hero_multi_weapon_attack():
    strength = SuperHeroes.Weapon("Overwhelming Strength", 200)
    sword_of_truth = SuperHeroes.Weapon("Sword of Truth", 700)
    Athena = SuperHeroes.Hero("Athena")
    Athena.add_ability(strength)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2

    test_runs = 100
    for _ in range(0, test_runs):
        attack = Athena.attack()
        assert attack <= 900 and attack >= 0


def test_hero_weapon_ability_attack():
    quickness = SuperHeroes.Ability("Quickness", 1300)
    sword_of_truth = SuperHeroes.Weapon("Sword of Truth", 700)
    Athena = SuperHeroes.Hero("Athena")
    Athena.add_ability(quickness)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2
    attack_avg(Athena, 0, 2000)


def attack_avg(object, low, high):
    test_runs = 100
    for _ in range(0, test_runs):
        attack = object.attack()
        assert attack <= high and attack >= low

# Test Teams


def test_team_instance():
    team = SuperHeroes.Team("One")
    assert team


def test_team_name():
    team = SuperHeroes.Team("One")
    assert team.name == "One"


def test_team_hero():
    team = SuperHeroes.Team("One")
    jodie = SuperHeroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert len(team.heroes) == 1
    assert team.heroes[0].name == "Jodie Foster"


def test_team_remove_hero():
    team = SuperHeroes.Team("One")
    jodie = SuperHeroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert team.heroes[0].name == "Jodie Foster"
    team.remove_hero("Jodie Foster")
    assert len(team.heroes) == 0


def test_team_remove_unlisted():
    # Test that if no results found return 0
    team = SuperHeroes.Team("One")
    jodie = SuperHeroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    code = team.remove_hero("Athena")
    assert code == 0


def test_team_remove_empty_list():
    team = SuperHeroes.Team("One")
    assert team.remove_hero("Athena") == 0


def test_find_hero():
    team = SuperHeroes.Team("One")
    jodie = SuperHeroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    hero = team.find_hero("Jodie Foster")
    assert hero.name == "Jodie Foster"


def test_find_unlisted_hero():
    team = SuperHeroes.Team("One")
    jodie = SuperHeroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert team.find_hero("Alexa") == 0


def test_find_empty_hero():
    team = SuperHeroes.Team("One")
    assert team.find_hero("Alexa") == 0


def test_print_heroes():
    team = SuperHeroes.Team("One")
    jodie = SuperHeroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    athena = SuperHeroes.Hero("Athena")
    team.add_hero(athena)
    output_string = capture_console_output(team.view_all_heroes)

    assert "Jodie Foster" in output_string
    assert "Athena" in output_string
