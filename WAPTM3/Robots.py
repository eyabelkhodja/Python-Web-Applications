import requests
from WAPTM1.Basic_Authentification import BasicAuthentification

class ParsingRobots:
    def parsing(self, entered_url):
        try:

            if not entered_url.startswith(('http://', 'https://')):
                entered_url = 'https://' + entered_url

            basic_auth = BasicAuthentification()
            session = requests.Session()

            if basic_auth.check_basic_auth(entered_url):
                username = input("Enter username: ")
                password = input("Enter password: ")
                session = basic_auth.self_authenticate(username, password)

            url = entered_url.rstrip('/') + '/robots.txt'

            response = session.get(url)
            print(f"Successfully fetched {url}")
            return response.text

        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None


    def getDisallowed(self, text):
        if not text:
            return

        robots = [line.strip() for line in text.splitlines() if "disallow" in line.lower()]
        if robots:
            print("\nDisallow directives found:")
            for robot in robots:
                print(robot)
        else:
            print("No 'Disallow' directives found.")

def main():
    p = ParsingRobots()
    url = input("Enter URL (e.g., https://example.com): ").strip()
    text = p.parsing(url)
    if text:
        p.getDisallowed(text)

if __name__ == '__main__':
    main()