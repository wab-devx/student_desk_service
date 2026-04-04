"""
Validation module for Student Service Desk.
Handles input cleaning and range checks.
"""


class ValidationError(Exception):
    """Raised when any input validation fails."""
    pass


class Validator:

    def validate_id(self, student_id):
        """Checks if ID is a valid integer."""
        try:
            return int(student_id)
        except ValueError:
            raise ValidationError("Student ID must be a numeric integer.")

    def validate_name(self, name):
        """Strips whitespace and formats name to Title Case."""
        if not name.strip():
            raise ValidationError("Name cannot be empty.")
        return name.strip().title()

    def validate_phone(self, phone):
        """Removes non-digit characters and validates numeric content."""
        clean_phone = phone.replace(" ", "").replace("-", "")
        if not clean_phone.isdigit():
            raise ValidationError("Phone must contain digits only.")
        return clean_phone

    def validate_grade(self, grade_value):
        """Validates that grades are numeric and between 0-100."""
        try:
            val = float(grade_value)
        except ValueError:
            raise ValidationError("Grade must be a numeric value.")
        if not (0 <= val <= 100):
            raise ValidationError("Grade must be between 0 and 100.")
        return val
    

    
