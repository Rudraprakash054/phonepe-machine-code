from solution import Issue, Agent, IssueStatusType

# Issue creation
I1 = Issue.createIssue("T1", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser1@test.com")
I2 = Issue.createIssue("T2", "Mutual Fund Related", "Purchase Failed", "Unable to purchase Mutual Fund", "testUser2@test.com")
I3 = Issue.createIssue("T3", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser2@test.com")

# Agent creation
A1 = Agent.addAgent("agent1@test.com", "Agent 1", ["Payment Related", "Gold Related"])
A2 = Agent.addAgent("agent2@test.com", "Agent 2", ["Payment Related"])

# Assign customer issue to agent
assign_I1 = Issue.assignIssue("I1")
assign_I2 = Issue.assignIssue("I2")
assign_I3 = Issue.assignIssue("I3")

# Fetch issues based on the filter criteria
Issue.getIssue({"email": "testUser2@test.com"})
Issue.getIssue({"type": "Payment Related"})

# Update the status of an issue
Issue.updateIssue("I2", IssueStatusType.INPROGRESS, "Waiting for payment confirmation")

# Reslove issue
Issue.resolveIssue("I3", "Payment Failed debited amount will get reversed")

# View the agent work history
Agent.viewAgentsWorkHistory()