from database import  create_table, add_entry, get_entries

menu = """ Please select one of the following options:
1)  Add a new entry for today.
2) View entries.
3) Exit.
Your selection"""
welcome = "Welcome to programming diary!"

def prompt_new_entry():
	entry_content = input("What have you learned today?")
	entry_date = input("Enter the date: ")

	add_entry(entry_content, entry_date)


def view_entries(entries):
	for entry in entries:
        	print(f"{entry['1']}\n{entry['0']}\n\n")


print(welcome)
create_table()

def new_func(menu, prompt_new_entry, view_entries):
    while (user_input := input(menu)) !="3":
        if user_input == "1":
         prompt_new_entry()
        elif user_input == "2":
            view_entries(get_entries())    
        else:
            print("Invalid option, please try again!")

new_func(menu, prompt_new_entry, view_entries)