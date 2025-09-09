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

