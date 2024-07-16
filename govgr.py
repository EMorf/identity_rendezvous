from mechanize import Browser, Link
import re

br = Browser()
br.open("https://www.gov.gr/ipiresies/polites-kai-kathemerinoteta/ex-apostaseos-exuperetese-politon/id")
response : Link = br.find_link(text_regex=re.compile("Είσοδος στην υπηρεσία"))
print(response.absolute_url)
response