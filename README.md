# Forum-Downloader
I just did it for a friend. (I am not a professional) my friend wanted to download some forum questions automatically. HTTack didn't give the expected results so I just made one. Hope you find it useful and message me if you have any questions

instruction(used AI to write the instruction because I was lazy) :

# Forum Scraper

This script logs into a forum, navigates through the pages, and downloads the content of specific forum questions to your local directory.

## Usage

1. **Setup**:
   - Ensure you have Python 3 installed.
   - Install the required packages using pip:
     ```bash
     pip install requests beautifulsoup4
     ```

2. **Configuration**:
   - Edit `forum_scraper.py` and replace the placeholders:
     ```python
     login_url = 'https://example.com/login'  # Example login URL
     login_payload = {
         'username': 'your_username',
         'password': 'your_password',
         'login': 'Login',
         'redirect': 'index.php',
         'sid': ''
     }
     ```

3. **Running the Script**:
   - Execute the script:
     ```bash
     python forum_scraper.py
     ```

## Limitations
- Ensure you have valid login credentials.
- Modify the `base_url` and other parameters as per your target forum's structure.
- The script assumes the forum's structure; it might require adjustments for different forums.

## License
This project is licensed under the CyberCop47 License.
