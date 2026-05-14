# Модуль 2. Класс Character

## Описание
Модуль реализует класс `Character`, наследующий от абстрактного класса `Unit`. Персонаж имеет привязку к игровому классу (`warrior`, `mage`, `hunter`).

## Что сделано

### 1. Создан класс Character, наследующий переменные класса Unit
```python
class Character(Unit):
    def __init__(self, character_class, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        super().__init__(strength, dexterity, constitution,
                         wisdom, intelligence, charisma)