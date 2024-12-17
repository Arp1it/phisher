# Phishing Tool ⚠️  
**For Educational and Ethical Purposes Only**

## Overview
This is a Python-based phishing tool designed to demonstrate how phishing pages work. It leverages the Flask framework to host phishing templates locally and **Ngrok** to generate public URLs for accessibility.

> **⚠️ Disclaimer:**  
> This tool is strictly for **educational purposes** to raise awareness about cybersecurity threats. Do not use this tool for malicious purposes. Unauthorized use of phishing tools can lead to severe legal consequences.

---

## Features  
- Pre-built phishing templates for platforms like:  
  - Instagram  
  - Facebook  
  - Gmail  
  - Snapchat  
  - Telegram  
  - X (Twitter)  
- Custom redirect URL after credentials are captured  
- Ngrok integration for exposing localhost to the public  
- Simple setup and modular design  

---

## Requirements  
Ensure the following software and libraries are installed:  
- **Python** (>= 3.6)  
- Required Python modules (auto-installed):  
  - `flask`  
  - `pyngrok`  
  - `termcolor`  
  - `pyfiglet`  
  - `requests`  

---

## Installation and Usage

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Arp1it/phisher.git
   cd phisher
   ```

2. **Run the Tool**  
   Run the script using Python:  
   ```bash
   python3 main.py
   ```

3. **Choose Phishing Page Type**  
   Enter one of the following options when prompted:  
   - `insta` → Instagram  
   - `meta` → Facebook  
   - `gmail` → Gmail  
   - `snap` → Snapchat  
   - `tele` → Telegram  
   - `x` → Twitter  

4. **Provide a Custom Redirect URL**  
   After credentials are captured, victims will be redirected to this URL.

5. **Start Ngrok**  
   - You can choose to let the tool start Ngrok automatically.  
   - Provide your **Ngrok authtoken** when prompted.  
   - The tool will generate a **public URL** for your phishing page.

6. **Access Phishing Page**  
   Share the generated public URL responsibly for demonstration purposes.

---

## How It Runs in the Terminal  

### Starting the Tool  
When you start the tool, it displays ASCII art and options for phishing page selection:  
```plaintext
Used for education purpose Only! 
Python Phisher Initializing...

  _______  _______  _______  _______  _______ 
 (       )(  ___  )(  ___  )(  ____ \(  __   )
 | () () || (   ) || (   ) || (    \/| (  )  |
 | || || || |   | || |   | || (__    | | /   |
 | |(_)| || |   | || |   | ||  __)   | (/ /) |
 | |   | || |   | || |   | || (      |   / | |
 | )   ( || (___) || (___) || (____/\|  (__) |
 |/     \|(_______)(_______)(_______/(_______)

Enter port number here (Default port - 8096): 8080
Enter: insta
Enter Custom Url: https://example.com
```

### Ngrok and Public URL  
The tool will generate a public URL:  
```plaintext
Are you want we start ngrok or you start itself Y for yes N for no!: Y
Enter ngrok authtoken: YOUR_NGROK_AUTH_TOKEN

* Running on http://127.0.0.1:8080
Public URL: https://abcd1234.ngrok.io
```

### Capturing Credentials  
When a user submits credentials on the phishing page, the tool logs them:  
```plaintext
[+] User: example_user
[+] Password: example_password
```

---

## Notes  
- The tool logs captured credentials (username/password) in the terminal.  
- Custom **WhatsApp QR Phishing** and **OTP extraction** features are planned in future updates.

---

## Disclaimer ⚠️  
This project is intended for educational purposes **only**. Using this tool to target individuals without explicit consent is illegal and unethical. By using this tool, you agree that you will not use it for malicious activities.  

---

## Contributing  
Contributions for improving this tool are welcome. Create a pull request or open an issue for suggestions.

---

## Author  
**.Echo Cipher**  
[Nexus Shroud] 
[Arp1it](https://github.com/Arp1it)

---

**Stay Ethical, Stay Safe!**  
