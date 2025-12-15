name = input('What is your name? ') .title().strip()
email = input('Enter Your Email please: ').strip().lower()
username =email[:email.index('@')] 
domain =email[email.index('@')+1:]
website = email[email.index('@')+1:]
print(f'''Hi, {name} 
your username is: "{username}" 
and your domain is: "{domain}"  
and your website is" https://{website}" ''')