import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment
from WAPTM1.Basic_Authentification import BasicAuthentification

class ParsingComments():
    def parsing (self,url):
        try:
            basic_auth = BasicAuthentification()
            if basic_auth.check_basic_auth(url):
                username=input("Username")
                password=input("Password")
                s=basic_auth.self_authenticate(username,password)
            else:
                s=requests.Session()
            response = s.get(url)

            if response.ok:
                return(response.text)
            else:
                print (f"Error {response.status_code}")
                return None
        except Exception as e:
            print(e)

    def getComments (self, text):
        soup = bs(text,"html.parser")
        comments = [text for text in soup.find_all(string=True) if isinstance(text, Comment)]

        for comment in comments:
            print(comment)

def main ():
    p= ParsingComments ()
    url=input("Url")
    text=p.parsing(url)
    p.getComments(text)

if __name__=='__main__':
    main()
