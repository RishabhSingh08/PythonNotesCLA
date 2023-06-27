import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

notes = []

while True:
    # Display menu options
    print(Fore.GREEN + Style.BRIGHT)
    choice = input("[🗒 ADD]\n[👀VIEW]\n\n").lower()
    print(Style.RESET_ALL)

    if choice == 'add':
        # Add a new note
        print(Fore.YELLOW)
        newNote = input('📝 ')
        print(Style.RESET_ALL)
        notes.append(newNote)
        print(Fore.GREEN + Style.BRIGHT + '✅ Note Added!')
        print(Style.RESET_ALL)

    elif choice == 'view':
        # View existing notes
        print()
        print(Fore.CYAN + Style.BRIGHT + '---------- Notes ----------')
        print(Style.RESET_ALL)
        for note in notes:
            noteId = notes.index(note) + 1
            print(f"{noteId}: {note}")
        print()
        print(Fore.CYAN + Style.BRIGHT + '---------------------------')
        print(Style.RESET_ALL)

        # Handle delete or edit options
        choice2 = input(Fore.GREEN + Style.BRIGHT +
                        "[❌ DELETE]\n[🔓 EDIT]\n\n").lower()
        print(Style.RESET_ALL)

        if choice2 == "delete":
            try:
                # Delete a note
                delIndex = input(Fore.YELLOW + 'ID of note: ')
                print(Style.RESET_ALL)
                if delIndex.lower() == 'all':
                    # Delete all notes
                    notes.clear()
                    print(Fore.RED + '💥 Deleted all notes')
                    print(Style.RESET_ALL)
                    continue

                delIndex = int(delIndex)
                if not (delIndex in range(1, len(notes) + 1)):
                    print(Fore.RED + 'Invalid note ID.')
                    print(Style.RESET_ALL)
                    continue

                delIndex -= 1  # Adjusting index for zero-based indexing

                print(Fore.RED + '🗑 Note Deleted!')
                print(f"'{notes[delIndex]}'")
                print(Style.RESET_ALL)
                del notes[delIndex]

            except ValueError:
                print(Fore.RED + 'Invalid input. Please enter a valid note ID or "all".')
                print(Style.RESET_ALL)
                continue

        elif choice2 == "edit":
            try:
                # Edit a note
                editId = int(input(Fore.YELLOW + 'ID of note: '))
                print(Style.RESET_ALL)
                if not (editId in range(1, len(notes) + 1)):
                    print(Fore.RED + 'Invalid note ID.')
                    print(Style.RESET_ALL)
                    continue

                editId -= 1  # Adjusting index for zero-based indexing

                print(Fore.YELLOW + f"\nEditing Note: {notes[editId]}")
                notes[editId] = input("New Note: ")
                print(Fore.GREEN + '🔒 Note Edited!')
                print(Style.RESET_ALL)

            except ValueError:
                print(Fore.RED + 'Invalid input. Please enter a valid note ID.')
                print(Style.RESET_ALL)
                continue

    else:
        # Handle invalid choices
        print(Fore.RED + 'Invalid choice. Please choose "add" or "view".')
        print(Style.RESET_ALL)
