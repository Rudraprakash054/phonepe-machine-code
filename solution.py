from typing import List, Dict
from helper import IssueStatusType

import random

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
    
    @staticmethod 
    def assignIssue(issue_id: str) -> None:
        '''
        Assign a customer issue to agent
        '''
        for agent in Agent._agents.values():
            if not agent._active_issue():
                agent.issues.append(Issue._issues[issue_id])
                print(f'Issue {issue_id} assigned to Agent {agent.agent_id}')
                return
        
        random_agent = random.choice(list(Agent._agents.values()))
        random_agent.issues.append(Issue._issues[issue_id])
        print(f'Issue {issue_id} added to waitlist of Agent {random_agent.agent_id}')

    @staticmethod
    def getIssue(filter_param: Dict[str, str]) -> None:
        '''
        Fetch issues based on the filter parameters
        '''
        if filter_param:
            for issue in Issue._issues.values():
                if filter_param.get('email') and filter_param['email'] == issue.email:
                    print(issue.__dict__)
                elif filter_param.get('type') and filter_param['type'] == issue.issue_type:
                    print(issue.__dict__)

    @staticmethod
    def updateIssue(issue_id: str, status: str, resolution: str) -> None:
        '''
        Update the status of an issue
        '''
        issue = Issue._issues.get(issue_id)
        if issue:
            issue.status = status
            issue.resolution = resolution
            print(f'{issue.issue_id} status updated to {issue.status}')

    @staticmethod
    def resolveIssue(issue_id: str, resolution: str) -> None:
        '''
        Resolve an issue
        '''
        issue = Issue._issues.get(issue_id)
        if issue:
            issue.status = IssueStatusType.CLOSED
            issue.resolution = resolution
            print(f'{issue.issue_id} issue marked resolved')


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

    def _active_issue(self) -> bool:
        '''
        Check whether the issue is open or in-progress state
        '''
        for issue in self.issues:
            if issue.status in [IssueStatusType.OPEN, IssueStatusType.INPROGRESS]:
                return True
        return False
    
    @staticmethod
    def viewAgentsWorkHistory() -> None:
        '''
        Get the work history details of agents
        '''
        for agent in Agent._agents.values():
            issue_ids = [issue.issue_id for issue in agent.issues]
            print(f'{agent.agent_id} -> {issue_ids}')