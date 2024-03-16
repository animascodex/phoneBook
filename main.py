from tkinter import *


class Contact:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    def __str__(self):
        return 'Name: {} Phone: {}'.format(self._name, self._phone)


class PhoneBook:
    def __init__(self, name):
        self._name = name
        self._contacts = []

    def addContact(self, contact):
        self._contacts.append(contact)

    def searchContact(self, name):
        for c in self._contacts:
            if c.name == name: return c
        return None

    def removeContact(self, name):
        c = self.searchContact(name)
        if c is None: return False
        self._contacts.remove(c)
        return True

    def updateContact(self, name, phone):
        c = self.searchContact(name)
        if c is None: return False
        c.phone = phone
        return True

    def __str__(self):
        contacts = [str(c) for c in self._contacts]
        contacts.sort()
        return 'Phone Book Owner Name: {}\n{}'.format(self._name, '\n'.join(contacts))


class GuiPhoneBook:
    def __init__(self, PhoneManagement):
        PhoneManagement.title("Phone Book Management System Kong Jia Ming (Z1910720)")
        # Create 3 Frames, for Entry Field, Button widgets and Message logs Respectively#
        PhoneManagement.geometry("720x400")
        self.var_1 = StringVar()
        Entry_Frame = Frame(PhoneManagement)
        Entry_Frame.grid(row=0, column=0)
        Entry_Frame.grid_rowconfigure(0, weight=1)
        Entry_Frame.grid_columnconfigure(0, weight=1)
        button_frame = Frame(PhoneManagement)
        button_frame.grid(row=1, column=0, sticky="nw")
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        message_frame = Canvas(PhoneManagement)
        message_frame.grid()
        scroll_y = Scrollbar(PhoneManagement, orient="vertical", command=message_frame.yview)
        scroll_y.grid(row=2, column=7, sticky="ns")
        message_frame.configure(yscrollcommand=scroll_y.set)
        # Create Widgets for Labels and Buttons
        self.the_Label1 = Label(Entry_Frame, text="Name:")
        self.the_Label2 = Label(Entry_Frame, text="Phone:")
        self.entry_1 = Entry(Entry_Frame)
        self.entry_2 = Entry(Entry_Frame)
        self.the_Label1.grid(row=0, column=1, sticky=E)
        self.the_Label2.grid(row=1, column=1, sticky=E)
        self.entry_1.grid(row=0, column=2, columnspan=2, sticky=N)
        self.entry_2.grid(row=1, column=2, columnspan=2, sticky=N)
        self.Phone_Search = Button(button_frame, text="Search", command=(self.Gui_Search))
        self.Phone_Update = Button(button_frame, text="Update", command=(self.Gui_Update))
        self.Phone_Remove = Button(button_frame, text="Remove", command=(self.Gui_Remove))
        self.Phone_Add = Button(button_frame, text="Add", command=(self.Gui_Add))
        self.Phone_Show = Button(button_frame, text="Show", command=(self.Gui_Show))
        self.Phone_Clear = Button(button_frame, text="Clear", command=(self.Gui_Clear))
        self.Phone_Search.grid(row=2, column=0, ipadx=30)
        self.Phone_Update.grid(row=2, column=1, ipadx=30)
        self.Phone_Remove.grid(row=2, column=2, ipadx=30)
        self.Phone_Add.grid(row=2, column=3, ipadx=30)
        self.Phone_Show.grid(row=2, column=4, ipadx=30)
        self.Phone_Clear.grid(row=2, column=5, ipadx=30)
        self.Phone_Log = Label(message_frame, textvariable=self.var_1, bg="white", width=100, height=20, anchor=NW,
                               justify=LEFT)
        self.Phone_Log.grid(row=4, columnspan=6)

    # Search Function
    def Gui_Search(self):
        User_Search = myFriends.searchContact(self.entry_1.get())
        if User_Search == None:
            display_string = "No Entry for " + self.entry_1.get()
        else:
            display_string = "Retrieved: " + str(User_Search)
        self.var_1.set(display_string)

    # Update Function
    def Gui_Update(self):
        User_Search = myFriends.searchContact(self.entry_1.get())
        User_Update = myFriends.updateContact(self.entry_1.get(), self.entry_2.get())
        if User_Update == False:
            display_string = "No Entry for " + self.entry_1.get()
        else:
            display_string = "Updated: " + str(User_Search) + "\n" + str(myFriends)
        self.var_1.set(display_string)

    # Remove Function
    def Gui_Remove(self):
        User_Search = myFriends.searchContact(self.entry_1.get())
        User_Remove = myFriends.removeContact(self.entry_1.get())
        if User_Remove == False:
            display_string = "No Entry for " + self.entry_1.get()
        else:
            display_string = "Removed: " + str(User_Search) + "\n" + str(myFriends)
        self.var_1.set(display_string)

    # Add Function
    def Gui_Add(self):
        User_Search = myFriends.searchContact(self.entry_1.get())
        if User_Search != None:
            display_string = "Existing entry for " + self.entry_1.get()
        else:
            myFriends.addContact(Contact(self.entry_1.get(), self.entry_2.get()))
            User_Search = myFriends.searchContact(self.entry_1.get())
            display_string = "Added: " + str(User_Search) + "\n" + str(myFriends)
        self.var_1.set(display_string)

    # Show Function
    def Gui_Show(self):
        display_string = str(myFriends)
        self.var_1.set(display_string)

    # Clear Function
    def Gui_Clear(self):
        display_string = ""
        self.var_1.set(display_string)
        self.entry_1.delete(0, "end")
        self.entry_2.delete(0, "end")


myFriends = PhoneBook('Jim')
myFriends.addContact(Contact('Peter', 9123123))
myFriends.addContact(Contact('Joe', 8123123))
myFriends.addContact(Contact('Amy', 6123231))

root = Tk()
b = GuiPhoneBook(root)

root.mainloop()
