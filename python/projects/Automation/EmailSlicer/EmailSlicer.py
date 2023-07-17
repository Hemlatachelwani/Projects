email=input(" enter email :").strip()

user = email.split('@')[0]
domain = email.split('@')[1]

print("user ->",user," domain-->",domain)


username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f"user name is {username}  n domain is {domain}")


