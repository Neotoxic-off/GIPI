import requests
from lib import status
from lib import colors
from verif import check

class settings:
    URL = "https://www.instagram.com/"
    USER = ""

def connection():
    s = requests.Session()
    return (s.get(url = "%s%s" % (settings.URL, settings.USER)))

def resume(posts, followers, following):
    print("%s %s: %s%s%s Posts | %s%s%s Followers | %s%s%s Following" % (
            status.info(),
            settings.USER,
            colors.cyan(),
            posts,
            colors.reset(),
            colors.cyan(),
            followers,
            colors.reset(),
            colors.cyan(),
            following,
            colors.reset()
        ))

def parse(resp):
    posts = None
    followers = None
    following = None
    i = 0
    content = resp.text.split(' ')
    content = list(filter(None, content))

    while i < len(content):
        if content[i] == "Followers," and followers == None:
            followers = content[i - 1].split('"')[1]
        elif content[i] == "Following," and following == None:
            following = content[i - 1]
        elif content[i] == "Posts" and posts == None:
            posts = content[i - 1]
        i += 1
    resume(posts, followers, following)

def scan():
    while settings.USER != 'exit':
        settings.USER = input("%s Username: " % status.input())
        if settings.USER == 'exit':
            print("\n%s Exiting" % status.working())
            exit(0)
        else:
            if check(settings.USER) == 0:
                try:
                    resp = connection()
                    if resp.status_code == 200:
                        print("\n%s Connection success" % (status.ok()))
                        parse(resp)
                    else:
                        print("\n%s Connection failed" % (status.error()))
                except:
                    print("\n%s Connection failed" % (status.error()))

scan()
