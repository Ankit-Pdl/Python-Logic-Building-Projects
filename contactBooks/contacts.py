import json
from rich import print

while True:
    print("[white on red]Your Contact Module:[/white on red]")
    print("1: Show Your Contacts")
    print("2: Add contact")
    print("3: Delete a contact")
    print("4: Exit")

    try:
        user_choice = int(input("Please enter your choice: "))

        match user_choice:
            case 1:
                print("Showing contacts...")
                try:
                    with open("contactBooks/contacts.json", "r") as file:
                        contacts = json.load(file)
                except (json.JSONDecodeError, FileNotFoundError):
                    print("[bold red]You don't have any contacts saved![/bold red]")
                    contacts = []

                for contact in contacts:
                    print(f"[bold]Name:[/bold] {contact['name']}")
                    print(f"[bold]Phone:[/bold] {contact['phoneNumber']}")
                    print("──────────────")

            case 2:
                try:
                    with open("contactBooks/contacts.json", "r") as file:
                        contacts = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    contacts = []

                user_Contact = int(input("Enter User's phone number: "))
                user_Name = input("Enter full name: ")

                found = False

                for contact in contacts:
                    if contact["name"] == user_Name:
                        print("[dark_violet]Contact exists! Updating number...[/dark_violet]")
                        contact["phoneNumber"] = user_Contact
                        found = True
                        break

                if not found:
                    new_Contact = {
                        "name": user_Name,
                        "phoneNumber": user_Contact
                    }
                    contacts.append(new_Contact)

                with open("contactBooks/contacts.json", "w") as file:
                    json.dump(contacts, file, indent=4)

                print("[white on green]Contact saved successfully![/white on green]")

            case 3:
                try:
                    with open("contactBooks/contacts.json", "r") as file:
                        contacts = json.load(file)

                    original_length = len(contacts)
                    user_delete_data = int(input("Enter the phone number you want to delete: "))
                    contacts = [c for c in contacts if c["phoneNumber"] != user_delete_data]

                    if len(contacts) < original_length:
                        with open("contactBooks/contacts.json", "w") as file:
                            json.dump(contacts, file, indent=4)
                        print("[white on green]Contact deleted successfully![/white on green]")
                    else:
                        print("[red]Contact not found.[/red]")

                except (FileNotFoundError, json.JSONDecodeError):
                    print("[bold magenta]Your contact list is empty![/bold magenta]")

            case 4:
                print("Exited successfully!")
                break

            case _:
                print("[bold red]Please enter a number between 1 and 4![/bold red]")

    except ValueError:
        print("[bold red]Use a valid menu number![/bold red]")