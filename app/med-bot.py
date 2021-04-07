import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = "[ENTER-BOT-TOKEN]"
SLACK_APP_TOKEN = "[ENTER-APP-TOKEN]"

creds_file = "creds.json"
excel_id = "[ID OF GOOGLE SHEET]"
sheet_name = "[ENTER NAME OF USED SHEET]"

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def name(event, say):
    text = event["text"].split()
    worksheet = readsheet()
    list_of_names = worksheet.get_all_values()
    for items in list_of_names:
        if "Name" in items:
            names = items[1:]
            for name_items in names:
                if text[1].lower() in name_items.lower():
                    find_name = re.compile(f"({name_items}$)", re.IGNORECASE)
                    cell = worksheet.find(find_name)
                    column_number = cell.col
                    values_list = worksheet.col_values(column_number)
                    for items in values_list:
                        if items == "":
                            pass
                        else:
                            say(f"{items}")
            else:
                pass


def access_sheet():
    """
    Access sheet according to sheet id provided.
    Returns the sheet object
    """
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(excel_id)
    return sheet

def readsheet():
    """
    Accepts sheet name to be read
    Returns sheet data object of the specified sheet.
    """
    sheet = access_sheet()
    worksheet = sheet.worksheet(sheet_name)
    # sheet_data = worksheet.get_all_values()
    return worksheet

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()