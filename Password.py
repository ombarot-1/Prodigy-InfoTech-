import re

def password(password):
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password) is not None
    lower = re.search(r'[a-z]', password) is not None
    numbers = re.search(r'[0-9]', password) is not None
    special_char = re.search(r'[\W_]', password) is not None
    
    strength = sum([length, upper, lower, numbers, special_char])
    
    if strength == 5:
        complexity = 'Very High'
    elif strength == 4:
        complexity = 'High'
    elif strength == 3:
        complexity = 'Moderate'
    elif strength == 2:
        complexity = 'Low'
    elif strength == 1:
        complexity = 'Very Low'
    
    feedback = []
    if not length:
        feedback.append('Password should be at least 8 characters long.')
    if not upper:
        feedback.append('Password should contain at least 1 uppercase letter.')
    if not lower:
        feedback.append('Password should contain at least 1 lowercase letter.')
    if not numbers:
        feedback.append('Password should contain at least 1 digit.')
    if not special_char:
        feedback.append('Password should contain at least 1 special character.')

    return complexity, feedback

pw = input('Enter your password: ')
complexity, feedback = password(pw)

print(f'Complexity of Password: {complexity}')

if feedback:
    print('-: Feedback :-')
    for f in feedback:
        print(f"->{f}")