import time
from plyer import notification
import Qalam.scrape as s

term, gpa, cgpa = s.PCResults()
notification.notify(
    title = f"{term} Result",
    message = f"GPA: {gpa}  CGPA: {cgpa}",
    app_icon = "Qalam/nust.ico",
    timeout = 10
)
term, amount = s.SemesterInvoice()
notification.notify(
    title = f"{term} Invoice",
    message = f"Total Amount:  Rs. {int(float(amount))}",
    app_icon = "Qalam/nust.ico",
    timeout = 10
)