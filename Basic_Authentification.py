import requests

class BasicAuthentification():
    def check_basic_auth(self, url):
        try:
            response = requests.get(url)
            if response.status_code==401:
                basic_auth=response.headers.get("WWW-Authenticate","")
                if "Basic" in basic_auth:
                    return True
                else:
                    return False
            else:
                return False
        except:
            print (f"Error while connecting to {url}")
            return False

    def self_authenticate (self, username, password):
        session =requests.Session()
        session.auth=(username,password)
        return session

def main ():
    url = input ("Enter the URL: ")
    basic_auth= BasicAuthentification()
    if basic_auth.check_basic_auth(url):
        print ("Uses Basic Authentification")
        username = input ("Enter the username: ")
        password = input("Enter the password: ")
        s = basic_auth.self_authenticate(username,password)
        response = s.get(url)
        if response.ok:
            print("Successful authentification")
        else:
            print("Failed authentification")
    else:
        print ("Does not use Basic Authentification")

if __name__ == '__main__':

        main()