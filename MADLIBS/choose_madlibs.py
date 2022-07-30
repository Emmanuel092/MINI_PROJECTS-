from all_madlibs import code, horror_story, script,harry_potter

import random

if __name__ == "__main__":
    choice = random.choice([horror_story, code, script, harry_potter])
    choice.madlib()
