import requests
import customtkinter
from WAPTM1.Basic_Authentification import BasicAuthentification

class ParsingRobots:
    def parsing(self, entered_url, app):
        try:
            if not entered_url.startswith(('http://', 'https://')):
                entered_url = 'https://' + entered_url

            basic_auth = BasicAuthentification()
            s = None
            if basic_auth.check_basic_auth(entered_url):
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

            url = entered_url.rstrip('/') + '/robots.txt'
            response = s.get(url)
            if response.ok:
                return response.text
            else:
                print(f"Error {response.status_code}")
                return None

        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def getDisallowed(self, text, app):
        if not text:
            print("No content to parse")
            return

        robots = [line.strip() for line in text.splitlines() if "disallow" in line.lower()]
        if robots:
            print("\nDisallow directives found:")
            for robot in robots:
                label = customtkinter.CTkLabel(app, text=robot, fg_color="transparent")
                label.pack(pady=10)
        else:
            print("No 'Disallow' directives found.")
            label = customtkinter.CTkLabel(app, text="No 'Disallow' directives found.", fg_color="transparent")
            label.pack(pady=10)

def button_action1(entered_url, app):
    # Pass the entry widget itself, not its value
    url = entered_url.get()
    if not url:
        print("Please enter a URL")
        return
    p = ParsingRobots()
    text = p.parsing(url, app)
    if text:
        p.getDisallowed(text, app)

def main():
    app = customtkinter.CTk()
    app.title("Authentication App")
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