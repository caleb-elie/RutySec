# RUTYSec - Advanced Password Security & Cracking Tool

![RUTYSec](https://img.shields.io/badge/Security-Tool-blue?style=flat-square)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

## About RUTYSec
**RUTYSec** is a powerful password security tool designed to generate secure passwords, hash passwords, check if they’ve been leaked in data breaches, and perform dictionary attacks for penetration testing. Built with **Python**, it integrates **encryption, hashing, and OSINT techniques** to enhance password security assessments.

## Features
- **Generate strong passwords** (customizable length)
- **Hash passwords** using MD5, SHA-256, and SHA-512
- **Check password leaks** via Have I Been Pwned (HIBP) API
- **Dictionary attack** using a custom wordlist or the RockYou wordlist
- **AES encryption** used internally to secure stored sensitive data

## 🛠️ Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/RUTYSec.git
cd RUTYSec
```

### **2. Install Dependencies**
Ensure you have Python 3.8+ installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### **3. Run RUTYSec**
```bash
python rutySec.py
```

## Troubleshooting on Kali Linux
If you encounter issues running RUTYSec on Kali Linux, try the following fixes:
- Ensure Python 3 is the default version:
  ```bash
  python3 --version
  ```
  If not, use `python3` instead of `python` in commands.
- Install missing dependencies manually:
  ```bash
  pip3 install -r requirements.txt
  ```
- If `requests` or `pycryptodome` cause issues, install them explicitly:
  ```bash
  pip3 install requests pycryptodome
  ```
- If permissions cause issues, try running with sudo:
  ```bash
  sudo python rutySec.py
  ```
  ```
  # Clone the repository
git clone <repository_url>

# Navigate into the directory
cd RUTYSec

# List all files (dir for Windows, ls for Unix-like systems)
ls  # or 'dir' if on Windows

# View the file contents
cat rutySec.py  # or 'type rutySec.py' on Windows

# Then
nano rutySec.py
# Save: Ctrl + S
# Exit: Ctrl + X

# Run the script
python3 rutySec.py
```
## Usage
Upon running RUTYSec, you’ll be presented with the following menu:

**Options:**
1. Generate a Secure Password
2. Hash a Password
3. Check if Password is Leaked
4. Run Dictionary Attack
5. Exit

### Example Commands
#### Generate a Secure Password
```bash
python rutySec.py
# Choose option 1
# Enter length: 16
# Output: X7kP!m9qL2vR8tJn
```

#### Hash a Password
```bash
python rutySec.py
# Choose option 2
# Enter password: mypass
# Select algorithm: sha256
# Output: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

#### Check if Password is leaked
```bash
python rutySec.py
# Choose option 3
# Enter password: password123
# Output: This password has been leaked 100000 times
```

#### Dictionary Attack (Pentesting)
```bash
python rutySec.py
# Choose option 4
# Enter target hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
# Select algorithm: sha256
# Output: Password found: mypass
```

## Requirements
- Python 3.8+
- Internet connection (for password breach checking)
- A user-provided `password.txt` file or the RockYou wordlist (for dictionary attacks)
- Dependencies listed in `requirements.txt`:
  ```
  requests
  hashlib
  argparse
  pycryptodome
  ```

```bash
pip3 install -r requirements.txt
```

## Disclaimer
This tool is for educational and ethical hacking purposes only. Do not use it for illegal activities. The author is not responsible for any misuse.

## License
This project is licensed under the MIT License ([LICENSE](LICENSE)).

## Contributing
Pull requests and suggestions are welcome! Feel free to open issues for bugs and feature requests.

## Contact
**Creator:** [GitHub](https://github.com/caleb-elie)  
**X:** [@c4l3bpy](https://x.com/c4l3bpy)  
**Email:** programmingcaleb@gmail.com  

**RUTYSec: Make your security sturdy, protect your passwords.**

