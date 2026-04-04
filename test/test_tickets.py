import unittest
from src.app import App
from src.models import TicketStatus
from src.validation import StudentNotFoundError

class TestTicketSystem(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.app.add_student(101, "Amina Ali", "77889900", 80, 90)

    def test_create_ticket_valid(self):
        t_id = self.app.create_ticket(101, "Support", "Portal access")  # "Accès portail"
        self.assertEqual(len(self.app.tickets), 1)

    def test_create_ticket_missing_student(self):
        with self.assertRaises(StudentNotFoundError):
            self.app.create_ticket(999, "Urgent", "Error")  # "Erreur"

    def test_resolve_ticket_logic(self):
        t_id = self.app.create_ticket(101, "Grade", "Review")  # "Revue"
        self.app.resolve_ticket(t_id, "Done.")  # "Fait."
        ticket = self.app.find_ticket_by_id(t_id)
        self.assertEqual(ticket.status, TicketStatus.RESOLVED)

