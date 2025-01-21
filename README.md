# WhatsApp Profile Picture Updater

This project automates the process of updating your WhatsApp profile picture with a random cat image fetched from an API. It uses Selenium for browser automation and The Cat API for fetching cat images.

## Features
- Automates login to WhatsApp Web.
- Fetches a random cat image from The Cat API.
- Updates your WhatsApp profile picture with the fetched cat image.

## Prerequisites

1. **Python**: Make sure Python 3.7 or higher is installed on your system.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: ChromeDriver must be compatible with your Chrome version (managed automatically by `webdriver-manager`).
4. **Environment Variable**: Set up your API key for The Cat API as an environment variable:
   - On Windows (Command Prompt):
     ```bash
     set CAT_API_KEY=your_api_key
     ```
   - On Linux/Mac (Terminal):
     ```bash
     export CAT_API_KEY=your_api_key
     ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/whatsapp-profile-updater.git
   ```
2. Navigate to the project directory:
   ```bash
   cd whatsapp-profile-updater
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up the `CAT_API_KEY` environment variable as described above.
2. Run the script:
   ```bash
   python whatsapp_profile_updater.py
   ```
3. Follow the on-screen instructions to scan the QR code and log in to WhatsApp Web.
4. The script will automatically fetch a random cat image and update your profile picture.

## Directory Structure

```plaintext
whatsapp-profile-updater/
├── dependency/          # Stores browser user data
├── whatsapp_profile_updater.py  # Main script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

## Dependencies
The project requires the following Python libraries:

- `selenium`
- `webdriver-manager`
- `requests`

These are listed in the `requirements.txt` file and can be installed with:
```bash
pip install -r requirements.txt
```

## Notes

- Ensure you log in to WhatsApp Web within the time limit provided by the script.
- The script will create a `dependency` folder in the project directory to store browser user data.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a suggestion for improvement.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Selenium](https://www.selenium.dev/)
- [The Cat API](https://thecatapi.com/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)

