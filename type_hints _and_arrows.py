# age: int
# name: str
# height: float
# is_human = bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "they can drive"


if police_check("twelve"):
    print("you may pass")
else:
    print("pay a fine")
