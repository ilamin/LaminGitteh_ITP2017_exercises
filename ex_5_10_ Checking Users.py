print("CHECKING USERS")
current_users=['lamin', 'brian', 'asoka','stuu', 'jeff']
new_users=['lamin', 'vibe', 'ian', 'brian', 'bagus']
for i in new_users:
    if i in current_users:
        print("Sorry " + i + ", please enter another username.")
    else:
        print("The username " + i + " , is available")
if 'new_users' in current_users:
    print("The username, ", new_users, "is not available")