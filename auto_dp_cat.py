from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests

# Define a user data directory path relative to the current working directory
current_dir = os.getcwd()
user_data_dir = os.path.join(current_dir, "dependency")  # Directory to store user data

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

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code
print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(20)  # Adjust sleep time as needed

# Function to change the display picture
def change_display_picture(image_path):
    try:
        print("Navigating to profile settings...")
        # Click on the profile picture at the top left corner
        profile_picture = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Profile']"))
        )
        profile_picture.click()
        time.sleep(2)

        print("Clicking on the camera icon...")
        # Click on the camera icon to change the profile picture
        camera_icon = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='View group profile photo']"))
        )
        camera_icon.click()
        time.sleep(2)

        print("Uploading the new profile picture...")
        # Input file field to upload the picture
        file_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(image_path)
        time.sleep(2)

        print("Saving the new profile picture...")
        final_save_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-icon='checkmark-large']"))
        )
        final_save_button.click()
        time.sleep(2)
        print("Profile picture updated successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to fetch a cat image and save it locally
def fetch_and_save_cat_image(save_path):
    api_key = os.getenv("CAT_API_KEY")  # Load API key from environment variable
    if not api_key:
        print("API key not found. Please set the CAT_API_KEY environment variable.")
        return None

    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        image_url = data[0]["url"]

        # Fetch the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(image_response.content)
            print(f"Cat image saved at {save_path}")
            return save_path
        else:
            print("Failed to fetch the image.")
            return None
    else:
        print("Failed to get response from the Cat API.")
        return None

# Set the local path to save the image
local_image_path = os.path.join(user_data_dir, "cat_image.jpg")

# Fetch a cat image and change the display picture
saved_image_path = fetch_and_save_cat_image(local_image_path)
if saved_image_path:
    change_display_picture(saved_image_path)

# Close the WebDriver
driver.quit()
