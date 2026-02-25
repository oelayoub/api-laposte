📦 La Poste Tracking Automation

🚀 Overview

This project automates the retrieval of delivery status for multiple tracking numbers using the La Poste Suivi API.

Instead of manually checking each tracking number, the script:
	•	Reads tracking numbers from a CSV file
	•	Calls the La Poste API
	•	Extracts delivery status information
	•	Logs execution details
	•	Exports structured results to a CSV file

⸻

🏗 Project Structure

tracking-laposte/
│
├── src/
│   ├── main.py           # Orchestrates execution
│   ├── api_laposte.py    # Handles API calls & parsing
│   ├── data_io.py        # CSV read/export logic
│   └── config.py         # Configuration & environment variables
│
├── .gitignore

🔐 API Key Setup

This project uses an environment variable for security.

You must define your API key before running the script.

macOS / Linux:
export LAPOSTE_API_KEY=your_api_key_here
Verify it is set
echo *LAPOSTE_API_KEY

▶️ How to Run

From the project root:
venv/bin/python src/main.py

🪵 Logging

The script uses Python’s built-in logging module:
	•	INFO → Execution progress
	•	WARNING → Failed tracking numbers
	•	Errors are logged inside the API layer

Logs are displayed in the terminal.

⸻

📄 Output

The script generates a structured CSV file containing:
	•	Tracking number
	•	Delivery status code
	•	Status label
	•	Date