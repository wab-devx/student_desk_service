class Student: 
    """Represents one student record.""" 
    def __init__(self, student_id: int, name: str, phone: str, midterm: int, final: int, next_ticket_id = 1): 
        self.student_id = student_id 
        self.name = name 
        self.phone = phone 
        self.midterm = midterm 
        self.final = final
        self.next_ticket_id = next_ticket_id

 
    def term_grade(self, w_mid=0.40, w_final=0.60) -> float: 
        """Return weighted term grade.""" 
        return self.midterm * w_mid + self.final * w_final 
 
    def __str__(self): 
        return (f"{self.student_id} | {self.name} | {self.phone} | " 
                f"midterm={self.midterm}, final={self.final}, term={self.term_grade():.1f}")
    
    
from enum import Enum 
 
class TicketStatus(Enum): 
    OPEN = "OPEN" 
    RESOLVED = "RESOLVED" 
 
class Ticket: 
    def __init__(self, ticket_id: int, student_id: int, category: str, description: str): 
        self.ticket_id = ticket_id 
        self.student_id = student_id 
        self.category = category 
        self.description = description 
        self.status = TicketStatus.OPEN 
        self.resolution_note = None 
 
    def resolve(self, note: str): 
        self.status = TicketStatus.RESOLVED 
        self.resolution_note = note.strip() 
 
    def __str__(self): 
        base = f"#{self.ticket_id} | student={self.student_id} | {self.category} | {self.status.value}" 
        return base + (f" | note={self.resolution_note}" if self.resolution_note else "") 


        