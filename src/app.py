from src.models import Student, Ticket, TicketStatus
from src.validation import Validator, ValidationError
 
class App :
 
    s : dict[int, Student] = {}
    tickets : dict[int, Ticket] = {}
    next_ticket_id = 1
    validator = Validator()
 
    def add_student(self):
        '''Add a new student to Student class'''
        try:
            student_id = self.validator.validate_id(input("Enter the student ID : "))
            if student_id in self.s:
                print("ID already exist !")
                return
            name = self.validator.validate_name(input("Name : "))
            phone = self.validator.validate_phone(input("Phone : "))
            midterm = self.validator.validate_grade(input("Midterm grade (0-100) : "))
            final = self.validator.validate_grade(input("Final grade (0-100) : "))
        except ValidationError as e:
            print(f"Error: {e}")
            return
 
        self.s[student_id] = Student(student_id, name, phone, midterm, final)
        print("Student succesfully added !")
 
    def update_student(self):
        """Modify a choosen field."""
        try:
            student_id = self.validator.validate_id(input("Enter the ID of the student you want to modify : "))
        except ValidationError as e:
            print(f"Error: {e}")
            return
 
        if student_id not in self.s:
            print("No student correspond to that ID.")
            return
 
        print("Which field you want to modify ?")
        print("1) Name")
        print("2) Phone")
        print("3) Midterm")
        print("4) Final")
        field_choice = input("Choice : ").strip()
 
        student = self.s[student_id]
 
        try:
            if field_choice == "1":
                new_value = input("New name : ").strip().title()
                if new_value == "":
                    print("The name can't be empty.")
                    return
                student.name = new_value
 
            elif field_choice == "2":
                new_value = input("New phone number : ").replace("-", "").replace(" ", "")
                if not new_value.isdigit():
                    print("The phone number has to contain digits only.")
                    return
                student.phone = new_value
 
            elif field_choice == "3":
                new_value = self.validator.validate_grade(input("New midterm grade (0-100) : "))
                student.midterm = new_value
 
            elif field_choice == "4":
                new_value = self.validator.validate_grade(input("New final grade (0-100) : "))
                student.final = new_value
 
            else:
                print("Error !")
                return
        except ValidationError as e:
            print(f"Error: {e}")
            return
 
        print("Modification succesfully done !")
 
    def delete_student(self):
        """Delete a student from Student class by his/her ID."""
        try:
            student_id = self.validator.validate_id(input("Enter the ID of the student you want to delete : "))
        except ValidationError as e:
            print(f"Error: {e}")
            return
 
        if student_id not in self.s:
            print("No student found.")
            return
 
        del self.s[student_id]
        print("Student succesfully deleted !")
 
    def find_by_id(self):
        '''Find and display a student by ID'''
        try:
            student_id = self.validator.validate_id(input("Enter the student ID : "))
        except ValidationError as e:
            print(f"Error: {e}")
            return
 
        if student_id not in self.s:
            print("Student doesn't exist.")
            return
 
        student = self.s[student_id]
        print(f"ID      : {student.student_id}")
        print(f"Name    : {student.name}")
        print(f"Phone   : {student.phone}")
        print(f"Midterm : {student.midterm}")
        print(f"Final   : {student.final}")
        print(f"Term    : {student.term_grade():.1f}")
 
    def search_by_name(self):
        """Search students by name."""
        name = input("Enter name to search: ").strip().lower()
        found = False
 
        for student in self.s.values():
            if name in student.name.lower():
                print(f"ID      : {student.student_id}")
                print(f"Name    : {student.name}")
                print(f"Phone   : {student.phone}")
                print(f"Midterm : {student.midterm}")
                print(f"Final   : {student.final}")
                print(f"Term    : {student.term_grade():.1f}")
                found = True
 
        if not found:
            print("No student found with that name.")
 
    def create_service_ticket(self):
        """Add a ticket linked to an existing student."""
        try:
            student_id = self.validator.validate_id(input("Enter student ID: "))
 
            if student_id not in self.s:
                print("Error: Student ID not found. You must add the student first.")
                return
 
            category = input("Category (e.g. Academic): ").strip()
            description = input("Description: ").strip()
 
            if not category or not description:
                print("Fields cannot be empty.")
                return
 
            new_ticket = Ticket(self.next_ticket_id, student_id, category, description)
            self.tickets[self.next_ticket_id] = new_ticket
 
            print(f"Ticket #{self.next_ticket_id} created for {self.s[student_id].name}!")
            self.next_ticket_id += 1
 
        except ValidationError as e:
            print(f"Error: {e}")
 
    def list_tickets(self):
        """List tickets with an optional status filter."""
        print("\nFilter: 1) OPEN  2) RESOLVED  3) ALL")
        choice = input("Choice: ").strip()
 
        found = False
        for ticket in self.tickets.values():
            if choice == "1" and ticket.status != TicketStatus.OPEN:
                continue
            elif choice == "2" and ticket.status != TicketStatus.RESOLVED:
                continue
 
            student_name = self.s[ticket.student_id].name if ticket.student_id in self.s else "Unknown"
            print(f"{ticket} | Student: {student_name}")
            found = True
 
        if not found:
            print("No tickets to display.")
 
    def resolve_ticket(self):
        """Resolve an existing ticket with a note."""
        try:
            t_id = self.validator.validate_id(input("Enter Ticket ID to resolve: "))
        except ValidationError as e:
            print(f"Error: {e}")
            return
 
        if t_id not in self.tickets:
            print("Ticket not found.")
            return
 
        ticket = self.tickets[t_id]
        if ticket.status == TicketStatus.RESOLVED:
            print("Ticket is already resolved.")
            return
 
        note = input("Resolution note: ").strip()
        ticket.resolve(note)
        print(f"Ticket #{t_id} resolved.")
 
app = App()
