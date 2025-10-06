import os

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def read_numbers_file():
    """Membaca file numbers.txt dan return list of contacts"""
    contacts = []
    if not os.path.exists("numbers.txt"):
        return contacts

    with open("numbers.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            if line.strip() != "":
                contacts.append(line.strip())
    return contacts

def read_blacklist_file():
    """Membaca file blacklist.txt dan return set of blacklisted numbers"""
    blacklisted = set()
    if not os.path.exists("blacklist.txt"):
        return blacklisted

    with open("blacklist.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            if line.strip() != "":
                # Extract nomor saja (untuk support format: nomor atau nomor - nama)
                parts = line.strip().split('-', 1)
                number = parts[0].strip()
                blacklisted.add(number)
    return blacklisted

def extract_number(contact_line):
    """Extract nomor dari format: nomor atau nomor - nama"""
    parts = contact_line.split('-', 1)
    return parts[0].strip()

def filter_blacklisted_numbers():
    """
    Filter nomor di numbers.txt yang ada di blacklist.
    Return: (filtered_contacts, removed_count, all_blacklisted)
    """
    contacts = read_numbers_file()
    blacklisted = read_blacklist_file()

    if not contacts:
        print(style.RED + "Error: numbers.txt is empty!" + style.RESET)
        return [], 0, True

    if not blacklisted:
        print(style.GREEN + "No blacklisted numbers found. Proceeding with all contacts." + style.RESET)
        return contacts, 0, False

    # Filter contacts
    filtered_contacts = []
    removed_contacts = []

    for contact in contacts:
        number = extract_number(contact)
        if number not in blacklisted:
            filtered_contacts.append(contact)
        else:
            removed_contacts.append(contact)

    # Show removed contacts
    if removed_contacts:
        print(style.YELLOW + f"\n⚠️  Found {len(removed_contacts)} blacklisted number(s):" + style.RESET)
        for contact in removed_contacts:
            print(style.RED + f"  ❌ {contact}" + style.RESET)

    # Check if all numbers are blacklisted
    all_blacklisted = len(filtered_contacts) == 0

    if all_blacklisted:
        print(style.RED + "\n❌ All numbers in numbers.txt are blacklisted!" + style.RESET)
        print(style.RED + "Process cancelled. No messages will be sent." + style.RESET)
        return [], len(removed_contacts), True

    # Update numbers.txt dengan filtered contacts
    if removed_contacts:
        with open("numbers.txt", "w", encoding="utf8") as f:
            for contact in filtered_contacts:
                f.write(contact + "\n")
        print(style.GREEN + f"\n✅ Removed {len(removed_contacts)} blacklisted number(s) from numbers.txt" + style.RESET)
        print(style.GREEN + f"📋 {len(filtered_contacts)} contact(s) remaining for blast" + style.RESET)

    return filtered_contacts, len(removed_contacts), False

def move_to_blacklist():
    """
    Memindahkan semua nomor dari numbers.txt ke blacklist.txt setelah blast selesai
    """
    contacts = read_numbers_file()

    if not contacts:
        print(style.YELLOW + "No contacts to move to blacklist." + style.RESET)
        return

    # Check if blacklist.txt needs newline at the end
    needs_newline = False
    if os.path.exists("blacklist.txt"):
        with open("blacklist.txt", "rb") as f:
            f.seek(0, 2)  # Go to end of file
            size = f.tell()
            if size > 0:
                f.seek(size - 1)  # Go to last byte
                last_char = f.read(1)
                needs_newline = last_char != b'\n'

    # Append new contacts to blacklist
    with open("blacklist.txt", "a", encoding="utf8") as f:
        if needs_newline:
            f.write("\n")
        for contact in contacts:
            f.write(contact + "\n")

    print(style.GREEN + f"\n✅ Moved {len(contacts)} contact(s) to blacklist.txt" + style.RESET)

    # Clear numbers.txt
    with open("numbers.txt", "w", encoding="utf8") as f:
        f.write("")

    print(style.GREEN + "✅ Cleared numbers.txt" + style.RESET)

if __name__ == "__main__":
    print(style.BLUE + "=" * 60)
    print("BLACKLIST CHECKER")
    print("=" * 60 + style.RESET)

    filtered, removed, all_blacklisted = filter_blacklisted_numbers()

    if all_blacklisted:
        print(style.RED + "\n❌ Cannot proceed with blast." + style.RESET)
    else:
        print(style.GREEN + f"\n✅ Ready to blast {len(filtered)} contact(s)" + style.RESET)
