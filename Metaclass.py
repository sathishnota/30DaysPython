import re

class NamingConventionMeta(type):
    def __new__(cls, name, bases, dct):
        # Enforce PascalCase (starts with uppercase letter, no underscores)
        if not re.match(r'^[A-Z][a-zA-Z0-9]+$', name):
            raise TypeError(f"❌ Class name '{name}' must be in PascalCase format.")
        print(f"✅ Creating class '{name}' with NamingConventionMeta")
        return super().__new__(cls, name, bases, dct)

# ✅ This will work
class MyGoodClass(metaclass=NamingConventionMeta):
    pass
