import pywhatkit as kit
# Send a WhatsApp message
phone_number = "+923109551403"  # Replace with recipient's phone number (include country code)
message = "Hello! This is an automated message sent using Python."
hour = 21  # Specify the hour in 24-hour format
minute = 30  # Specify the minute
try:
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")