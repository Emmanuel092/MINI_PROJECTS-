def madlib():
    properties = input("what property did you buy?:")
    who = input("who did you buy this property with?:")
    task = input("what task are you going to do?:")
    day = input("When did you make a list of names and dates ?:")
    authority = input("who did you notify about your findings?:")
    paragraph = f"We bought a {properties}, {who} and I. {who} is in charge of the new  \
               construction – converting the kitchen in to the master bedroom for instance, while I'm on {task}.\
               The previous owner papered EVERY wall and CEILING! Removing it is brutal, but oddly satisfying. The best feeling  \
               is getting a long peel, similar to your skin when you're peeling from a sunburn. I don't know about you but I kinda \
               make a game of peeling, on the hunt for the longest piece before it rips.Under a corner section of paper in every  \
               room is a person’s name and a date. Curiosity got the best of me one night when I Googled one of the names and  \
               discovered the person was actually a missing person, the missing date matching the date under the wallpaper!  \
               {day}, I made a list of all the names and dates. Sure enough each name was for a missing person with dates \
               to match. We notified the {authority} who naturally sent out the crime scene team. I overhead one tech say yup, its \
                human . Human? What's human? Ma'am, where is the material you removed from the walls already?  \
                This isn't wallpaper you were removing."

    print(paragraph)


if __name__ == "__main__":
    madlib()
