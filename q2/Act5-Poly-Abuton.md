# Activity 5: Reflection Assignment

### 1. What do all the methods (`move()`, `special_move()`, `use()`) in the previous activities have in common?
They all use the exact same name to do different things across different classes. They act as a shared interface while hiding the unique inner code of each class behind one simple command.

### 2. How does this activity show polymorphism in a gaming context?
It shows how central game loops or inventory setups can run items and actions automatically. The main code doesn't need to know if an item is a healing potion or a speed boost, it just runs `.use()` and lets the object handle its own unique behavior.

### 3. Can you think of other examples where the same action behaves differently depending on the character or item?
An `attack()` method: A Knight swings a sword, a Mage fires a magic beam, and a Dragon breathes fire.
An `interact()` method: Clicking a chest opens it for loot, clicking an NPC opens a chat box or trading interface, and clicking a lever opens a secret gate.
