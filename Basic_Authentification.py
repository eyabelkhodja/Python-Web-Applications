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

def main ():
    url = input ("Enter the URL: ")
    basic_auth= BasicAuthentification()
    if basic_auth.check_basic_auth(url):
        print ("Uses Basic Authentification")
    else:
        print ("Does not use Basic Authentification")

if __name__ == '__main__':
        main()