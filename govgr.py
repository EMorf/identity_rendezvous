from mechanize import Browser, Link
import re




def transition_to_main_page() -> list:
    br = Browser()
    br.open(
        "https://www.gov.gr/ipiresies/polites-kai-kathemerinoteta/ex-apostaseos-exuperetese-politon/id"
    )
    response: Link = br.find_link(text_regex=re.compile("Είσοδος στην υπηρεσία"))
    url = br.follow_link(response)
    return list(br.forms())

if __name__ == "__main__":
    form = transition_to_main_page()[0]
    signin_list = form["username"]
    print(form.read())