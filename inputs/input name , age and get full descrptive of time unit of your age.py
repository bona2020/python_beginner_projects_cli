name = input('What is your Name? ').strip().title()
age = int(input('What\'s your Age? ').strip())
months = age*12
weeks = age *52
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('='*80)
print(f'''Hi, {name} here is a full unit detail of your age:
you have lived for 
{months} Months.
{weeks:,} Weeks.
{days:,} Days.
{hours:,} Hours.
{minutes:,} Minutes.
{seconds:,} Seconds.'''
)
print('='*80)