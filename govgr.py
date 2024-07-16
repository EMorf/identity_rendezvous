from mechanize import Browser, Link, urlopen, HTMLForm
import re
import os
import sys


def load_envs():
    USERNAME = os.getenv("ID_USERNAME", None)
    PASSWORD = os.getenv("ID_PASSWORD", None)
    PERIFEREIA = os.getenv("PERIFEREIA", None)
    PERIFEREIAKI_ENOTITA = os.getenv("PENOTITA", None)
    IPIRESIA = os.getenv("IPIRESIA", None)

    all_attributes = [
        (USERNAME, "username", "ID_USERNAME"),
        (PASSWORD, "password", "ID_PASSWORD"),
        (PERIFEREIA, "περιφέρεια", "PERIFEREIA"),
        (PERIFEREIAKI_ENOTITA, "περιφερειακή ενότητα", "PENOTITA"),
        (IPIRESIA, "υπηρεσία", "IPIRESIA"),
    ]

    for item, text, env_var in all_attributes:
        if item is None:
            print(
                f"Δεν δώθηκε σωστά η μεταβλητή {text}, παρακαλώ ορίστε την ως enviromental variable {env_var}."
            )
            sys.exit(1)
    return USERNAME, PASSWORD, PERIFEREIA, PERIFEREIAKI_ENOTITA, IPIRESIA


def transition_to_main_page() -> list:
    br = Browser()
    br.open(
        "https://www.gov.gr/ipiresies/polites-kai-kathemerinoteta/ex-apostaseos-exuperetese-politon/id"
    )
    response: Link = br.find_link(text_regex=re.compile("Είσοδος στην υπηρεσία"))
    url = br.follow_link(response)
    return list(br.forms())


def follow_main_form_and_login(form: HTMLForm, uname: str, pword: str):
    form["username"] = uname
    form["password"] = pword
    print((urlopen(form.click()).read()).decode("utf-8"))


if __name__ == "__main__":
    # a,b,c,d,e = load_envs()
    form = transition_to_main_page()[0]
    follow_main_form_and_login(form, "test", "test")
