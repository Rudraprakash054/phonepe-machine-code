from typing import List
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
        self.description = description
        self.email = email
        self.status = IssueStatusType.OPEN
        self.resolution = None
        self.issue_id = "I" + str(Issue._next_id)
        Issue._next_id += 1
    
    @staticmethod
    def createIssue(transaction_id: str, issue_type: str, subject: str, description: str, email: str) -> None:
        '''
        Create a customer issue
        '''
        issue = Issue(transaction_id, issue_type, subject, description, email)
        if issue:
            print(f'Issue {issue.issue_id} created against transaction {issue.transaction_id}')
            Issue._issues[issue.issue_id] = issue
            
class Agent:
    # Class attributes
    _agents = {}
    _next_id = 1

    # constructor
    def __init__(self, email: str, name: str, issue_types: List[str]) -> None:
        self.name = name
        self.issue_types = issue_types
        self.email = email
        self.agent_id = "A" + str(Agent._next_id)
        self.issues = []
        Agent._next_id += 1
    
    @staticmethod
    def addAgent(email: str, name: str, issue_types: List[str]) -> None:
        '''
        Create an agent
        '''
        agent = Agent(email, name, issue_types)
        if agent:
            print(f'Agent {agent.agent_id} created')
            Agent._agents[agent.agent_id] = agent