from abc import ABC, abstractmethod


class Unit(ABC):
    """Абстрактный класс игрового юнита."""

    def __init__(self, strength, dexterity, constitution, wisdom,
                 intelligence, charisma):
        """Инициализация базовых характеристик."""
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        """Расчёт максимального здоровья."""
        pass

    @abstractmethod
    def calculate_damage(self):
        """Расчёт урона."""
        pass

    @abstractmethod
    def calculate_defense(self):
        """Расчёт защиты."""
        pass


class Character(Unit):
    """
    Класс персонажа с привязкой к игровому классу.
    """

    def __init__(self, character_class, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        """
        Инициализация персонажа.

        Args:
            character_class: класс персонажа (warrior, mage, hunter)
            strength, dexterity, constitution, wisdom, intelligence, charisma: характеристики
        """
        super().__init__(strength, dexterity, constitution,
                         wisdom, intelligence, charisma)
        self.character_class = character_class
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """Расчёт максимального здоровья персонажа."""
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self):
        """Расчёт урона в зависимости от класса."""
        if self.character_class.lower() == "warrior":
            return self.strength * 2.2 + self.constitution // 3
        elif self.character_class.lower() == "mage":
            return self.intelligence * 2.5 + self.wisdom // 2
        elif self.character_class.lower() == "hunter":
            return self.dexterity * 1.9 + self.strength // 3
        else:
            return 0

    def calculate_defense(self):
        """Расчёт защиты в зависимости от класса."""
        if self.character_class.lower() == "warrior":
            return self.constitution * 1.8 + self.strength // 4
        elif self.character_class.lower() == "mage":
            return self.wisdom * 1.3 + self.intelligence // 6
        elif self.character_class.lower() == "hunter":
            return self.dexterity * 1.6 + self.constitution // 5
        else:
            return 0
class Spell(ABC):
    """Абстрактный класс заклинания."""

    def __init__(self, name, damage, mana_cost):
        """Инициализация заклинания: название, урон, стоимость маны."""
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        """Применить заклинание (вернуть урон или эффект)."""
        pass


class Unit(Unit):
    """Расширенный класс Unit с поддержкой заклинаний и маны."""

    def __init__(self, strength, dexterity, constitution, wisdom,
                 intelligence, charisma):
        super().__init__(strength, dexterity, constitution,
                         wisdom, intelligence, charisma)
        self.spells = []
        self.mana = 0

    def add_spell(self, spell):
        """Добавить заклинание в список."""
        self.spells.append(spell)

    def cast_spell(self, index):
        """
        Применить заклинание по индексу.

        Если маны достаточно - вычесть стоимость и вернуть урон.
        Если не хватает - вывести сообщение.
        """
        if index < 0 or index >= len(self.spells):
            print("Неверный индекс заклинания")
            return

        spell = self.spells[index]

        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        else:
            print("Недостаточно маны")
            return


class Character(Character, Unit):
    """Расширенный класс Character с поддержкой маны."""

    def __init__(self, character_class, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        super().__init__(character_class, strength, dexterity, constitution,
                         wisdom, intelligence, charisma)
        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_mana(self):
        """
        Расчёт максимальной маны в зависимости от класса.
        Воин: интеллект + сила // 2
        Маг: интеллект * 3 + мудрость
        Охотник: ловкость * 1.5 + мудрость // 2
        """
        if self.character_class.lower() == "warrior":
            return self.intelligence + self.strength // 2
        elif self.character_class.lower() == "mage":
            return self.intelligence * 3 + self.wisdom
        elif self.character_class.lower() == "hunter":
            return int(self.dexterity * 1.5 + self.wisdom // 2)
        else:
            return 0


class Fireball(Spell):
    """Огненный шар — конкретное заклинание."""

    def __init__(self):
        super().__init__(name="Огненный шар", damage=35, mana_cost=15)

    def cast(self):
        """Применение заклинания — возвращает урон."""
        return self.damage


class MagicMissile(Spell):
    """Магический снаряд — конкретное заклинание."""

    def __init__(self):
        super().__init__(name="Магический снаряд", damage=5, mana_cost=8)

    def cast(self):
        """Применение заклинания — возвращает урон."""
        return self.damage


class Knife(Spell):
    """Ядовитый кортик — заклинание."""

    def __init__(self):
        super().__init__(name="Ядовитый кортик", damage=5, mana_cost=10)

    def cast(self):
        """Применение заклинания — возвращает урон."""
        return self.damage


class Axe(Spell):
    """Встречная спираль — заклинание."""

    def __init__(self):
        super().__init__(name="Встречная спираль", damage=20, mana_cost=40)

    def cast(self):
        """Применение заклинания — возвращает урон."""
        return self.damage


class EchoSlash(Spell):
    """Эхо-удар — заклинание."""

    def __init__(self):
        super().__init__(name="Эхо-удар", damage=10, mana_cost=20)

    def cast(self):
        """Применение заклинания — возвращает урон."""
        return self.damage


class ReversePolarity(Spell):
    """Обратная полярность — ультимативное заклинание."""

    def __init__(self):
        super().__init__(name="Обратная полярность", damage=320, mana_cost=160)

    def cast(self):
        """Применение заклинания — возвращает урон."""
        return self.damage