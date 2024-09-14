# Auto-Login Bot with Python

This repository contains a simple Python script that automates logging into a website using the Selenium library. It saves time and effort by automatically filling in credentials and clicking the login button for you.

## Features

- Automates login process for any website with username and password fields.
- Uses Selenium WebDriver to control Chrome and simulate user interaction.
- Simple and customizable for various websites.

## Prerequisites

Before running the script, make sure you have the following installed:

1. **Python 3.x**: Download from [here](https://www.python.org/downloads/).
2. **Google Chrome**: Download from [here](https://www.google.com/chrome/).
3. **ChromeDriver**: Download the ChromeDriver that matches your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract the file and note the location of `chromedriver.exe`.

## Installation

### Step 1: Clone the Repository

```terminal
git clone https://github.com/yourusername/Auto-Login-Bot.git
cd Auto-Login-Bot
```

### Step 2: Install Selenium

To install Selenium, use `pip`:

```terminal
pip install selenium
```

### Step 3: Set Up ChromeDriver

Download the appropriate version of ChromeDriver and place it in a known location. Update the `path` in the script with the correct location of your `chromedriver.exe` file.

## Usage

1. **Edit the script**: Update the following values in `autologin.py`:
   - `username`: Your username for the website.
   - `password`: Your password.
   - `url`: The login page URL for the website you want to automate.

2. **Run the script**:

```terminal
python autologin.py
```

The bot will:
- Open the Chrome browser.
- Navigate to the login page.
- Automatically fill in the username and password fields.
- Submit the form and log you in.

## Code Overview

The main steps in the code are:
- **Initialize Selenium WebDriver**: This controls the Chrome browser.
- **Navigate to the URL**: The bot opens the login page.
- **Locate Elements**: Using `By.ID` or other selectors to find username, password, and login button fields.
- **Fill in Credentials**: Sends the provided username and password to the respective fields.
- **Submit the Form**: Clicks the login button to complete the login process.

### Example

Here is a snippet from the code showing how the bot works:

```python
driver.find_element(By.ID, 'login_field').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.NAME, 'commit').click()
```

## Customization

You can customize the script to work with different websites by:
- Inspecting the login page and finding the correct `ID`, `Name`, or `CSS selector` for the username, password, and login button.
- Modifying the `startBot()` function to fit the new website's login structure.

## Troubleshooting

- **ChromeDriver Version Mismatch**: If you receive an error regarding ChromeDriver, ensure you have the correct version that matches your installed Chrome browser.
- **Element Not Found**: If elements are not found, inspect the page again and ensure you're using the correct `ID`, `Name`, or `Class` for the username and password fields.

## Contributing

Feel free to fork this repository, make your changes, and submit a pull request. Any contributions to improve this auto-login bot are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
