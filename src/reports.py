from src.app import app
 
def class_report():
    students = app.s
    if not students:
        print("No students enrolled.")
        return
    size = len(students)
    avg = sum(s.term_grade() for s in students.values()) / size
    top = max(students.values(), key=lambda s: s.term_grade())
    print(f"Class size    : {size}")
    print(f"Average grade : {avg:.1f}")
    print(f"Top student   : ({top.student_id}) {top.name} --> {top.term_grade():.1f}")
 