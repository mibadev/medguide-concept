# medguide Chatbot Assistant for Hospital Specific Clinical Guidelines

We believe in the use of chatbots in everyday clinical practice and have developed medguide as a proof-of-concept chatbot to simplify the management and use of hospital-specific guidelines.

## ⚙️ Chatbot Structure

Currently the chatbot is build for Slack but can be ported to other plattforms like Mattermost or RocketChat without any problems. 
To ensure an easy setup and scalable setup the chatbot accesses a Google Sheet as main database via API and supports a variaty of media formats than can be served by the chatbot to the user


## 🧾 Requirements
✳️ Slack Workspace Admin Access
✳️ Google Sheet API
✳️ Google Sheet Access
✳️ Server to Deploy the Code [e.g. AWS EC2 Instance]

### Python Dependencies
	Python V-3.X
	oauth2client.service_account
	slack_bolt
	gspread



## 🛠️ Deployment
1. Activate G-Sheets API following the Docs: https://gspread.readthedocs.io/en/latest/oauth2.html
2. Add the G-Sheet "client_email" as Contributor with Full Access on your Google Sheet
3. Download the JSON File with Credentials to access the Google Sheet Database
4. Generate an APP TOKEN on your Slack Workspace (see Slack Docs) and enter in python executable
5. Generate a BOT TOKEN on your Slack Workspace (see Slack Docs) and enter in python executable
6. Replace all elements written in [] in the executables
7. Start Python Executable on Local or Server
