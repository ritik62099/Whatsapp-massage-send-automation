import pywhatkit as kit
import pandas as pd
import time

# Read phone numbers and names from the Excel file
excel_file = "contacts.xlsx"  # Replace with your Excel file path
df = pd.read_excel(excel_file)

df.columns = df.columns.str.strip()  # Remove extra spaces in column names

# Replace with actual column names
number_col = "Numbers"
name_col = "Name"

# Clean and format data
df = df[[number_col, name_col]].dropna()  # Remove NaNs
df[number_col] = df[number_col].astype(str).str.replace(r'\.0$', '', regex=True)  # Remove .0
df[number_col] = df[number_col].apply(lambda x: x if x.startswith("+") else "+91" + x)  # Add country code

# Time interval between messages (in seconds)
interval = 10

# 💬 Main Function to send WhatsApp messages (text only)

def send_whatsapp_message(df, delay):
    for index, row in df.iterrows():
        name = row[name_col]
        number = row[number_col]
        
        # 📝 Customize your message here (multi-line supported)
#         message = f"""Hello {name}! 👋

# Yeh ek test message hai WhatsApp automation ka.
# Umeed hai sab badhiya ho!

# - Aapka dost"""


        
        message = f""" Enter your message here"""

        print(f"Sending message to {name} ({number})...")

        try:
            kit.sendwhatmsg_instantly(number, message)

        except Exception as e:
            print(f"Failed to send message to {name} ({number}): {e}")

        time.sleep(delay)

# ✅ Call the function
send_whatsapp_message(df, interval)


# 📸 OPTIONAL: Send image instead of text
# Uncomment the below code if you want to send an image instead of a message

'''
def send_image_message(df, delay, image_path):
    for index, row in df.iterrows():
        name = row[name_col]
        number = row[number_col]

        # 🖼 Caption with name
        caption = f"Hello {name}!\nYeh rahi tumhari photo 📷"

        print(f"Sending image to {name} ({number})...")

        try:
            kit.sendwhats_image(number, image_path, caption=caption)

        except Exception as e:
            print(f"Failed to send image to {name} ({number}): {e}")

        time.sleep(delay)

# 📸 Call this instead if you want to send images:
# send_image_message(df, interval, "photo.jpg")
'''
