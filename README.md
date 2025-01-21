# WhatsApp Automation Scripts

This repository contains two Python scripts to automate tasks on WhatsApp Web using Selenium:

1. **Profile Picture Automation**: Changes the WhatsApp profile picture to a downloaded cat image from The Cat API.
2. **Message Sending Automation**: Sends an automated message to a specified contact.

## Features

### Profile Picture Automation
- Automatically downloads a random cat image from The Cat API.
- Updates the WhatsApp profile picture with the downloaded image.

### Message Sending Automation
- Automates sending messages to specific WhatsApp contacts.
- Allows customization of the contact name and message content.

## Requirements
- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (managed automatically via `webdriver_manager`)

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository/whatsapp-automation-scripts.git
   cd whatsapp-automation-scripts
   ```

2. **Install Dependencies**
   Install the required Python packages:
   ```bash
   pip install selenium webdriver-manager requests
   ```

3. **Run the Scripts**

### Profile Picture Automation

- Update the API key in the script:
  ```python
  api_key = "your_api_key"  # Replace with your The Cat API key
  ```
- Execute the script:
  ```bash
  python profile_picture_automation.py
  ```
- Scan the QR code displayed in the browser to log in to your WhatsApp account.

### Message Sending Automation

- Modify the `contact_name` and `message` variables in the script with the desired values:
  ```python
  contact_name = "John Doe"  # Replace with your contact's name
  message = "Hello, this is an automated message."  # Replace with your message
  ```
- Execute the script:
  ```bash
  python message_sending_automation.py
  ```

## Example Usage

### Profile Picture Automation
Automatically change your WhatsApp profile picture to a random cat image:
```python
api_key = "your_api_key"  # Replace with your The Cat API key
```

### Message Sending Automation
Send a message to a contact:
```python
contact_name = "John Doe"  # Replace with your contact's name
message = "Hello, this is an automated message."  # Replace with your message
```

## Notes
- Ensure that the contact name matches the display name on WhatsApp.
- Keep the `whatsapp_user_data` directory for session persistence to avoid repeated QR code scans.

## Disclaimer
This project is for educational purposes only. Use responsibly and ensure you comply with WhatsApp's terms of service.
