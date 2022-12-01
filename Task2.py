import pyshorteners
import shelve


def link_input():
    a = input("Enter the link: ")
    if a[:8] != "https://":
        print("""The link shall begin with "https://" Спробуйте ще""")
        return link_input()
    else:
        return a


def webname():
    a = input("Name the website in a short way: ")
    if len(a) > 25:
        print("The title is too long, please give one under 25 symbols")
        return webname()
    else:
        return a

choice = input("Type a litte 'y' to shorten a link. If you want to find one directly, type any other symbol: ")

match choice:
    case "y":
        web_name = webname()
        link = link_input()
        with shelve.open("Links_Dict") as LinkShortener:
            LinkShortener[web_name] = link
            s = pyshorteners.Shortener().tinyurl.short(link)
            print("Your link has been shortened, you can copy it: ", s)


with shelve.open("Links_Dict") as LinkShortener:
    print("Below you can see the list of short names you used to shorten links")
    for key in LinkShortener.keys():
        print(key)
    print("In order to get the initial link, please type its given short name: ")
    given_name = input("Enter here: ")
    if given_name in LinkShortener.keys():
        print("Here your initial link", LinkShortener[given_name])
    else:
        print("The link is not found. You might have entered the shortname wrong.")
