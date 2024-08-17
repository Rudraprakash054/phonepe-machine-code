# Customer Issue Resolution System

PhonePe processes a vast number of transactions every day, wherein some transactions may fail (enter a FAILED state) or remain in a PENDING state due to various reasons such as bank or NPCI issues, or internal PhonePe errors. To handle such cases efficiently, a resolution system is needed, where customers can log their unsuccessful transactions and raise complaints against them.
The system must categorize customer issues into several types, such as payment-related, mutual fund-related, gold-related, or insurance-related. Different customer service agents will have their specific expertise based on the issue type, whom the system will assign the issues by marking them waiting in case all agents are busy.
The customer service agents can work on one issue at a time and update its status, and once it is resolved, the agent will receive another issue.

### The solution should incorporate the following features:

- Customers can log a complaint against any unsuccessful transaction.
- Customer Service Agents can search for customer issues with issue ID or customer details (email).
- Agents can view their assigned issues and mark them resolved once they are resolved.
- System should assign the issue to agents based on an assigning strategy.
- System should allow the admin to onboard new agents.
- System should allow the admin to view the agent's work history.

### Implementation requirements 

Your solution should implement the following functions. Feel free to use the representation for objects you deem fit for the problem and the provided use cases. The functions are ordered in the decreasing order of importance (highest to lowest). We understand that you may not be able to complete the implementation for all the functions listed here. So try to implement them in the order in which they are declared down below.

```
createIssue(transactionId, issueType, subject, description, email)
addAgent(agentEmail, agentName ,List<issueType>)
assignIssue(issueId) // -> Issue can be assigned to the agents based on different strategies. For now, assign to any one of the free agents.
getIssues(filter) // -> issues against the provided filter
updateIssue(issueId, status, resolution)
resolveIssue(issueId, resolution)
viewAgentsWorkHistory() // -> a list of issue which agents worked on
```

### Example:

```
createIssue("T1", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser1@test.com");
>>> Issue I1 created against transaction "T1"

createIssue("T2", "Mutual Fund Related", "Purchase Failed", "Unable to purchase Mutual Fund", "testUser2@test.com");
>>> Issue I2 created against transaction "T2"

createIssue("T3", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser2@test.com");
>>> Issue I3 created against transaction "T3"


addAgent("agent1@test.com", "Agent 1", Arrays.asList("Payment Related", "Gold Related"));
>>> Agent A1 created

addAgent("agent2@test.com", "Agent 2", Arrays.asList("Payment Related"));
>>> Agent A2 created


assignIssue("I1")
>>> Issue I1 assigned to agent A1

assignIssue("I2")
>>> Issue I2 assigned to agent A2

assignIssue("I3")
>>> Issue I3 added to waitlist of Agent A1


getIssue({"email": "testUser2@test.com"});
>>> I2 {"T2", "Mutual Fund Related", "Purchase Failed", "Unable to purchase Mutual Fund", "testUser2@test.com", "Open"},
 I3 {"T3", "Payment Related", "Payment Failed", "My payment failed but money is debited", , "testUser2@test.com", "Open"}

getIssue({"type": "Payment Related"});
>>> I1{"T1", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser1@test.com", "Open"},
 I3 {"T3", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser1@test.com", "Open"}


updateIssue("I3", "In Progress", "Waiting for payment confirmation");
>>> I3 status updated to In Progress


resolveIssue("I3", "PaymentFailed debited amount will get reversed");
>>> I3 issue marked resolved


viewAgentsWorkHistory()
>>> A1 -> {I1, I3}, 
    A2 -> {I2}
```