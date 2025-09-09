import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment
from WAPTM1.Basic_Authentification import BasicAuthentification
import customtkinter

class ParsingComments:
    def parsing(self, url, app):
        try:
            basic_auth = BasicAuthentification()
            s = None
            if basic_auth.check_basic_auth(url):
                dialog = customtkinter.CTkToplevel(app)
                dialog.title("Enter Credentials")
                dialog.geometry("500x300")
                dialog.grab_set()

                entered_username = customtkinter.CTkEntry(
                    dialog, width=400, placeholder_text="Enter the username",
                    text_color="blue", placeholder_text_color="white", justify="center"
                )
                entered_username.pack(pady=20)

                entered_password = customtkinter.CTkEntry(
                    dialog, width=400, placeholder_text="Enter the password",
                    text_color="blue", placeholder_text_color="white", justify="center",
                    show="*"
                )
                entered_password.pack(pady=20)

                def submit():
                    nonlocal s
                    username = entered_username.get()
                    password = entered_password.get()
                    s = basic_auth.self_authenticate(username, password)
                    dialog.destroy()

                button = customtkinter.CTkButton(
                    dialog, text="Submit Credentials", command=submit
                )
                button.pack(pady=20)

                app.wait_window(dialog)
                if s is None:
                    return None
            else:
                s = requests.Session()

            if s is None:
                return None

            response = s.get(url)
            if response.ok:
                return response.text
            else:
                print(f"Error {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Network error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def getComments(self, text, app):
        if not text:
            print("No content to parse")
            return
        soup = bs(text, "html.parser")
        comments = [text for text in soup.find_all(string=True) if isinstance(text, Comment)]
        for comment in comments:
            label = customtkinter.CTkLabel(app, text=comment, fg_color="transparent")
            label.pack(pady=20)

def button_action1(entered_url, app):
    url = entered_url.get()
    p = ParsingComments()
    text = p.parsing(url, app)
    if text:  # Only call if text is available
        p.getComments(text, app)

def main():
    app = customtkinter.CTk()
    app.title("Authentification app")
    app.geometry("600x400")
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    entered_url = customtkinter.CTkEntry(
        app, width=500, placeholder_text="Enter the URL",
        text_color="blue", placeholder_text_color="white", justify="center"
    )
    entered_url.pack(pady=20)

    button1 = customtkinter.CTkButton(
        app, text="Check URL", command=lambda: button_action1(entered_url, app)
    )
    button1.pack(pady=20)

    app.mainloop()

if __name__ == '__main__':
    main()