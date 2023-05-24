# Define rules for evaluating employee performance
rules = {
    "rule1": {
        "condition": "completed assigned tasks",
        "action": "satisfactory performance"
    },
    "rule2": {
        "condition": "met deadlines",
        "action": "excellent performance"
    },
    "rule3": {
        "condition": "received positive feedback",
        "action": "outstanding performance"
    },
    # Add more rules as needed
}

# Define the knowledge base
knowledge_base = {
    "completed assigned tasks": False,
    "met deadlines": False,
    "received positive feedback": False,
    # Add more conditions as needed
}

# Function to evaluate the rules and perform actions
def evaluate_rules():
    for rule in rules.values():
        condition = rule["condition"]
        action = rule["action"]
        
        if condition in knowledge_base and knowledge_base[condition]:
            if action not in knowledge_base:
                knowledge_base[action] = True
                print(f"The employee performance is: {action}")
        
# Main program loop
while True:
    # Get user input
    user_input = input("Enter a performance factor ('quit' to exit): ")
    
    # Check if user wants to quit
    if user_input.lower() == "quit":
        break
    
    # Update knowledge base with user input
    if user_input in knowledge_base:
        knowledge_base[user_input] = True
    else:
        print("Invalid performance factor.")
    
    # Evaluate rules and perform actions
    evaluate_rules()
    print(knowledge_base)
