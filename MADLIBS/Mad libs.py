# Define variables to fill the blank spaces

reader = input("What is your name :")
books_or_stories = input("Do you prefer books or stories?:")


paragraph = f"Welcome {reader}! We have huge collection of short stories by many famous writers across the world  \
            Few handpicked {books_or_stories} from various categories are listed below for quick reference. We also \
            provided link  to editor’s pick {books_or_stories} in each category. Additionally under Kids and Children \
            category we have good moral lesson and bedtime {books_or_stories} for our little readers.We hope that you  \
            have  pleasant time at our club {reader} !Your comments matter to our writers Please do provide your  \
            invaluable feedback. "


if books_or_stories != "books" and books_or_stories != "stories":
    print("wrong input")
else:
    print(paragraph)