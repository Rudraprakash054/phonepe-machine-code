from helper import IssueStatusType

class Issue:
    # Class attributes
    _issues = {}
    _next_id = 1

    # constructor
    def __init__(self, transaction_id: str, issue_type: str, subject: str, description: str, email: str) -> None:
        self.transaction_id = transaction_id
        self.issue_type = issue_type
        self.subject = subject
        self.description =