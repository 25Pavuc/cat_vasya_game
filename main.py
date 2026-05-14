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