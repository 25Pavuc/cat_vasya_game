# Модуль 1. Абстрактный класс Unit

## Описание
Модуль содержит абстрактный базовый класс `Unit`, который служит основой для всех игровых юнитов (персонажей, монстров и т.д.).

## Что сделано

### 1. Создан абстрактный класс Unit
```python
class Unit(ABC):
    def __init__(self, strength, dexterity, constitution, wisdom,
                 intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma