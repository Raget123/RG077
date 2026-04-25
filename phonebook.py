class Contact:
    def __init__(self):
        self.phonebook = {}

    # Input Number
    def inputcontact(self, name, number):
        if not number.isdigit():
            raise ValueError("Input The Number in Digit!")
        if len(number) > 12:
            raise ValueError("Number Over The Limit!")
        if name in self.phonebook:
            return "Name Is On Your Phonebook!"

        self.phonebook[name] = {
            "num": number,
            "ctg": ["Contact"]
        }
        return "Entering Into Contacts Successfully"

    # Add Category
    def contactcategory(self, name, category):
        category = category.capitalize()
        if name not in self.phonebook:
            return "The Name Not In Phonebook!"
        if category in self.phonebook[name]["ctg"]:
            return "The Contact Already In The Category"

        self.phonebook[name]["ctg"].append(category)
        return "Contact Enter Into Category!"

    # Change Name
    def namechange(self, name, newname):
        if name not in self.phonebook:
            return f"{name} not found"
        if newname in self.phonebook:
            return "Duplicate name!"

        self.phonebook[newname] = self.phonebook.pop(name)
        return "Name updated"

    # Show all
    def contactbook(self):
        print("| Contact Name | Contact Number |".center(64))
        print("-" * 35 .center(64))
        for k, v in self.phonebook.items():
            print(f"| {k:<12} | {v['num']:<14} |".center(64))

    # 🔍 Search by name + category
    def contactsearch(self, name, category="Contact"):
        category = category.capitalize()
        found = False

        print("| Contact Name | Contact Number |".center(64))

        for k, v in self.phonebook.items():
            if name.lower() in k.lower() and category in v["ctg"]:
                print(f"| {k:<12} | {v['num']:<14} |".center(64))
                found = True

        if not found:
            print("No matching contact found")

    # 🔍 Search by category
    def categorysearch(self, category):
        category = category.capitalize()
        found = False

        print("| Contact Name | Contact Number |".center(64))

        for k, v in self.phonebook.items():
            if category in v.get("ctg", []):
                print(f"| {k:<12} | {v['num']:<14} |".center(64))
                found = True

        if not found:
            print("The Category Not In Your Phonebook")