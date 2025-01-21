from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Define a user data directory path relative to the current working directory
current_dir = os.getcwd()
user_data_dir = os.path.join(current_dir, "whatsapp_user_data")  # Directory to store user data

# Ensure the directory exists
os.makedirs(user_data_dir, exist_ok=True)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--remote-debugging-port=9222")  # Use this port for debugging
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-gpu")  # Applicable for Windows OS only
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code
print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(20)  # Adjust sleep time as needed

# Function to send a message to a contact
def send_whatsapp_message(contact_name, message):
    try:
        print("Searching for the contact search box...")
        # Wait for the search box to be visible and click on it
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
        )
        print("Search box found. Clicking on it...")
        search_box.click()
        time.sleep(1)
        search_box.send_keys(contact_name)
        print(f"Typing contact name: {contact_name}")
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        print("Contact selected.")
        time.sleep(2)

        print(f"Typing message: {message}")
        # Type the message directly into the currently focused input
        driver.switch_to.active_element.send_keys(message)
        time.sleep(1)
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        print(f"Message sent to {contact_name}")
        time.sleep(1)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    contact_name = "Enter Contact Name Here"  # Replace with the contact's name as it appears on WhatsApp
    message = "Enter your message here."  # Replace with the message you want to send
    send_whatsapp_message(contact_name, message)

# Close the WebDriver
driver.quit()
