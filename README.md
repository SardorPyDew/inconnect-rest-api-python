# Inconnect 📩

**Inconnect** is a lightweight and easy-to-use Python library for sending and receiving emails using SMTP and IMAP protocols.

## 🚀 Installation

You can install Inconnect via pip:

```bash
pip install Inconnect
```

To upgrade to the latest version:

```bash
pip install --upgrade Inconnect
```

---

## 🎯 Usage Guide

### ✉️ **Sending an Email using SMTP**
You can use `SMTPClient` to send emails securely.

```python
from Inconnect.core import PyInconnect

API_KEY = "your_api_key_here"
mail_client = PyInconnect(api_key=API_KEY)

# Send an email
mail_client.send_email(
    name="John Doe",
    from_email="john@example.com",
    to_email="recipient@example.com",
    subject="PyInconnect Email Test",
    message="This is a simple email sent using PyInconnect."
)

print("✅ Email sent successfully!")
```
---

## ⚙️ Configuration Parameters

### **SMTPClient Parameters**
| Parameter | Description | Required | Default |
|-----------|------------|----------|---------|
| `smtp_server` | The SMTP server address (e.g., `smtp.gmail.com`) | ✅ Yes | - |
| `port` | The SMTP port (`465` for SSL, `587` for TLS) | ❌ No | `587` |
| `username` | The email address used for authentication | ✅ Yes | - |
| `password` | The email account password | ✅ Yes | - |
| `use_tls` | Enables TLS encryption (`True` for security) | ❌ No | `True` |

### **IMAPClient Parameters**
| Parameter | Description | Required | Default |
|-----------|------------|----------|---------|
| `imap_server` | The IMAP server address (e.g., `imap.gmail.com`) | ✅ Yes | - |
| `port` | The IMAP port (`993` for SSL) | ❌ No | `993` |
| `username` | The email address used for authentication | ✅ Yes | - |
| `password` | The email account password | ✅ Yes | - |

---

## 🔍 Error Handling

If you encounter issues while sending emails, check the following:
- **Ensure the SMTP/IMAP server address is correct.**
- **Verify that your email and password are entered correctly.**
- **Confirm that the server supports TLS/SSL encryption if enabled.**
- **Some email providers (e.g., Gmail, Outlook) require "Less Secure Apps" to be enabled or an App Password to be used.**

For further troubleshooting, please open an issue on **[GitHub Issues](https://github.com/SardorPyDew)**.

---

## 🔗 Additional Features

- **Supports multiple recipients and attachments (coming soon!)**
- **Secure authentication with OAuth support (planned)**
- **Custom email filtering for IMAP (upcoming feature)**

Stay tuned for updates! 🚀

---

## 📝 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

🔥 **Start sending and receiving emails easily with Inconnect!**  
💡 **Project Repository:** [GitHub](https://github.com/SardorPyDew/inconnect-rest-api-python)

