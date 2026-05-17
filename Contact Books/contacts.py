# 1. Add a contact (name, phone, email)
# 2. View all contacts
# 3. Search for a contact
# 4. Delete a contact
# 5. Save to JSON file
import json
from  rich import print
while True:
    print("[white on red]Your Contact Module:")
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
                 with open("Contact Books/contacts.json","r") as file:
                    contacts = json.load(file)
                except (json.JSONDecodeError,FileNotFoundError):
                    print("[bold red]You don't have any contacts saved![/bold red]")
                    contacts= []    
                for contact in contacts:
                       print(f"[bold]Name:[/bold] {contact['name']}")
                       print(f"[bold]Phone:[/bold] {contact['phoneNumber']}")
                       print("──────────────")
            case 2:
                user_Contact = int(input("Enter User's phone number:"))
                user_Name = input("Enter full name!")
                new_Contact = {
                    "name":user_Name,
                    "phoneNumber":user_Contact
                    }
                try:
                    with open("Contact Books/contacts.json","r") as file:
                        contacts = json.load(file)
                except FileNotFoundError: 
                         contacts = []  
                contacts.append(new_Contact)  
                with open ("Contact Books/contacts.json","w") as file:
                    #file.dump(contacts,file,indent = 4) #! json.dump ho yar  
                     json.dump(contacts,file,indent =4)           
            case 3:
                pass
            case 4:
                print("Exited successfully!")
                break  # ← exits the while loop
    except ValueError:
        # This now ONLY catches menu choice inputs that aren't numbers
        print("[bold red]Use a valid menu number![/bold red]")
