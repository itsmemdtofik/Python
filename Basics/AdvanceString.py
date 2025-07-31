# Case conversion in user authentication
# Case-insensitive login system
stored_username = "AdminUser123"
user_input = "adminuser123"

if user_input.casefold() == stored_username.casefold():
    print("Login successful!")
else:
    print("Invalid username")
    
# Output: Login successful!
# Why casefold() instead of lower()?
# casefold() is more aggressive and handles special cases like German 'ß' converting to 'ss', making it better for case-insensitive comparisons.

# Data cleaning and validation
# Cleaning and validating user data
def clean_phone_number(phone):
    # Remove all non-digit characters
    cleaned = ''.join(filter(str.isdigit, phone))
    
    # Add country code if missing
    if not cleaned.startswith('1') and len(cleaned) == 10:
        cleaned = '1' + cleaned
        
    return cleaned

print(clean_phone_number("(123) 456-7890"))  # "11234567890"
print(clean_phone_number("+1 800-555-1234")) # "18005551234"


#Advanced String Format

# Dynamic report generation using format()
report_template = """
{title:-^40}
Name: {name:<20} Age: {age:>3}
Department: {department:^15}
Salary: ${salary:,.2f}
"""

employee = {
    'title': 'Employee Report',
    'name': 'Alice Johnson',
    'age': 34,
    'department': 'Engineering',
    'salary': 85432.50
}

print(report_template.format(**employee))

##Text processing pipelines
# Processing a document with multiple methods
document = """
  IMPORTANT NOTICE:
  
  Meeting at 3PM on 2023-12-15.
  Topics: Budget, Hiring, Q4 Results.
  Location: Conference Room 2B.
"""

processed = (
    document.strip()              # Remove leading/trailing whitespace
    .lower()                     # Convert to lowercase
    .replace("conference", "main") # Change room type
    .title()                     # Title case
    .expandtabs(2)               # Replace tabs with 2 spaces
    .splitlines()                # Split into lines
)

# Remove empty lines and strip each line
cleaned_lines = [line.strip() for line in processed if line.strip()]

print("\n".join(cleaned_lines))

##Password Strength Checker
def check_password_strength(password):
    requirements = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': not password.isalnum()
    }
    
    if all(requirements.values()):
        return "Strong password"
    
    missing = [req for req, met in requirements.items() if not met]
    return f"Weak password - missing: {', '.join(missing)}"

print(check_password_strength("Passw0rd!"))  # Strong password
print(check_password_strength("weak"))       # Weak password - missing: length, uppercase, digit, special

##File extension processing
# Comprehensive filename processor
def process_filename(filename):
    # Split filename and extension
    name, _, ext = filename.rpartition('.')
    
    # Validate extension
    valid_extensions = {'jpg', 'png', 'gif', 'pdf'}
    if not ext.lower() in valid_extensions:
        raise ValueError(f"Invalid file extension: {ext}")
    
    # Clean the name part
    clean_name = (
        name.strip()
        .lower()
        .replace(' ', '_')
        .encode('ascii', errors='ignore')
        .decode()
    )
    
    # Remove consecutive underscores
    while '__' in clean_name:
        clean_name = clean_name.replace('__', '_')
    
    return f"{clean_name}.{ext.lower()}"

print(process_filename("My Document 123.JPG"))  # "my_document_123.jpg"
print(process_filename("Annual Report.PDF"))    # "annual_report.pdf"

##Multiline text alignment
# Formatting multi-line text with proper alignment
def format_poem(poem):
    lines = poem.splitlines()
    max_length = max(len(line) for line in lines)
    
    formatted_lines = []
    for i, line in enumerate(lines):
        if i % 2 == 0:
            # Left align even lines
            formatted = line.ljust(max_length)
        else:
            # Right align odd lines
            formatted = line.rjust(max_length)
        formatted_lines.append(formatted)
    
    return '\n'.join(formatted_lines)

poem = """Roses are red
Violets are blue
Sugar is sweet
And so are you"""

print(format_poem(poem))