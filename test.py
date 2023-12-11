import http.client
import requests

response = requests.post("https://texlive.net/cgi-bin/latexcgi", files={"filename[]":"document.tex", "filecontents[]": open("./creatingWorksheets/pdfs/document.tex", 'rb'), "return":"pdf"})

with open("test.pdf", 'wb') as f:
    f.write(response.content)