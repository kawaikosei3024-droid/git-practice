import sys
from datetime import datetime
def get_greeting():
    hour = datetime.now().hour
    if 5<= hour <12:
        return "Good morning"
    if 12<= hour <18:
        return "Hello"
    else:
        return "Good evening"
def greet(name: str) ->None:
    print(f"{get_greeting}, {name}!")
if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Git"
    greet(name)
    