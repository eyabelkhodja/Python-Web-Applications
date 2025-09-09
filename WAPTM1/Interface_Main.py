from Basic_Authentification import BasicAuthentification
import customtkinter

def button_action1(entered_url, app):
    url = entered_url.get()
    basic_auth = BasicAuthentification()

    if basic_auth.check_basic_auth(url):
        label = customtkinter.CTkLabel(app, text="Uses Basic Authentification", fg_color="transparent")
        label.pack(pady=20)

        entered_username = customtkinter.CTkEntry(app, width=500, placeholder_text="Enter the username", text_color="blue", placeholder_text_color="white", justify="center")
        entered_username.pack(pady=20)

        entered_password = customtkinter.CTkEntry(app, width=500, placeholder_text="Enter the password", text_color="blue", placeholder_text_color="white", justify="center", show="*")
        entered_password.pack(pady=20)

        button2 = customtkinter.CTkButton(
            app,
            text="Submit Credentials",
            command=lambda: button_action2(entered_username, entered_password, url, basic_auth, app)
        )
        button2.pack(pady=20)
    else:
        label = customtkinter.CTkLabel(app, text="Does not use Basic Authentification", fg_color="transparent")
        label.pack(pady=20)

def button_action2(entered_username, entered_password, url, basic_auth, app):
    username = entered_username.get()
    password = entered_password.get()

    s = basic_auth.self_authenticate(username, password)
    response = s.get(url)

    if response.ok:
        label = customtkinter.CTkLabel(app, text="Successful authentification", fg_color="transparent")
        label.pack(pady=20)
    else:
        label = customtkinter.CTkLabel(app, text="Failed authentification", fg_color="transparent")
        label.pack(pady=20)

def main():
    app = customtkinter.CTk()
    app.title("Authentification app")
    app.geometry("600x400")  # Increased height to accommodate more widgets
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    entered_url = customtkinter.CTkEntry(app, width=500, placeholder_text="Enter the URL", text_color="blue", placeholder_text_color="white", justify="center")
    entered_url.pack(pady=20)

    button1 = customtkinter.CTkButton(
        app,
        text="Check URL",
        command=lambda: button_action1(entered_url, app)
    )
    button1.pack(pady=20)

    app.mainloop()

if __name__ == '__main__':
    main()