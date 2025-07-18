import re

# Read from sample.txt and extract emails
input_file = "sample.txt"
output_file = "emails.txt"

def extract_emails(text):
    # More robust regex pattern for email extraction
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    raw_emails = re.findall(pattern, text)
    # Strip trailing punctuation and remove duplicates
    cleaned_emails = set(email.strip(".,;:!()[]{}<>\"'") for email in raw_emails)
    return cleaned_emails

try:
    with open(input_file, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
    exit(1)
except Exception as e:
    print(f"Error reading '{input_file}': {e}")
    exit(1)

emails = extract_emails(content)

try:
    with open(output_file, "w") as f:
        for email in sorted(emails):
            f.write(email + "\n")
except Exception as e:
    print(f"Error writing to '{output_file}': {e}")
    exit(1)

print(f"Extracted {len(emails)} unique emails to {output_file}")
