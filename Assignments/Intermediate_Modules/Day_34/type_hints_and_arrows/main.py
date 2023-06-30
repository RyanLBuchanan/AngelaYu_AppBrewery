# Age declaration as integer
# age: int
# name: str
# height: float
# is_human: bool

# Type hint for output
def police_check(age: int) -> bool:
    if age > 16:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(12))
