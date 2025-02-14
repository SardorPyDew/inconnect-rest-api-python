from Inconnect.core import PyInconnect

# Initialize the PyInconnect client with your API key
API_KEY = "your_api_key_here"
mail_client = PyInconnect(api_key=API_KEY)

# 1. Sending a basic email
response = mail_client.send_email(
    name="John Doe",
    from_email="john@example.com",
    to_email="recipient@example.com",
    subject="PyInconnect Email Test",
    message="This is a simple email sent using PyInconnect"
)

# 2. Sending an email with HTML content (HTML as a message)
html_content = "<h1>Hello!</h1><p>This is an email in HTML format.</p>"
response = mail_client.send_email(
    name="John Doe",
    from_email="john@example.com",
    to_email="recipient@example.com",
    subject="HTML Email Test",
    message=html_content,  # HTML message
)

# 3. Sending an email using a predefined template
template_id = "123456"
variables = {"username": "John", "discount_code": "SAVE20"}
response = mail_client.send_email_with_template(
    from_email="john@example.com",
    from_name="John Doe",
    to_email="recipient@example.com",
    subject="Email With Template",
    template_id=template_id,
    variables=variables
)