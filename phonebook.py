def main():
  phonebook_methods = {1: lookup_entry, 2: set_entry, 3: delete_entry, 4: list_entries}
  selection = 0
  phonebook = {}
  while selection != 5:
    print '''Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit'''
    selection = raw_input('What do you want to do (1-5)? ')
    if selection.isdigit():
      selection = int(selection)
    if selection in phonebook_methods:
      phonebook = phonebook_methods[selection](phonebook)
    elif selection != 5:
      print 'Invalid Selection'

def lookup_entry(phonebook):
  name = raw_input('Name: ').lower()
  if name in phonebook:
    print phonebook[name]
  else:
    print 'Invalid Name'
  return phonebook

def set_entry(phonebook):
  new_phonebook = phonebook.copy()
  name = raw_input('Name: ').lower()
  phone_num = raw_input('Phone Number: ')
  new_phonebook[name] = phone_num
  print 'Entry stored for ' + name.title()
  return new_phonebook

def delete_entry(phonebook):
  new_phonebook = phonebook.copy()
  name = raw_input('Name: ').lower()
  del new_phonebook[name]
  print 'Deleted entry for ' + name.title()
  return new_phonebook

def list_entries(phonebook):
  entry_list = ''
  for entry in phonebook:
    entry_list += 'Name: %s\nPhone: %s\n' % (entry.title(), str(phonebook[entry]))
  print entry_list[:-1]
  return phonebook

main()