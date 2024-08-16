from solution import Issue, Agent

# Issue creation
I1 = Issue.createIssue("T1", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser1@test.com")
I2 = Issue.createIssue("T2", "Mutual Fund Related", "Purchase Failed", "Unable to purchase Mutual Fund", "testUser2@test.com")

for issue in Issue._issues.values():
    print(issue.__dict__)

# agent creation
A1 = Agent.addAgent("agent1@test.com", "Agent 1", ["Payment Related", "Gold Related"])
A2 = Agent.addAgent("agent2@test.com", "Agent 2", ["Payment Related"])

for agent in Agent._agents.values():
    print(agent.__dict__)