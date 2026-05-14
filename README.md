# Модуль 3. Заклинания и мана

## Описание
Модуль добавляет в игру систему заклинаний и маны.

## Что сделано

### 1. Создан абстрактный класс Spell
```python
class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
    
    @abstractmethod
    def cast(self):
        pass