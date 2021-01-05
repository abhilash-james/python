import asms
import sys

OWN_PHONE_NUMBER = "918848901330"
ATEXT_APPLICATION_PASSWORD = "..."
RECIPIENT_PHONE_NUMBER = "919567254500"
MESSAGE_TO_SEND = 'Hello World!'

client = None
try:
        client = asms.SMS(phone = OWN_PHONE_NUMBER, password = ATEXT_APPLICATION_PASSWORD)
        if client.find_server():
                print("Found aText server: {}.".format(client.get_server_address()))
        else:
                print("Cannot find aText server in the local network. Exiting.", file = sys.stderr)
                exit(1)

        client.connect_to_server()

        response = client.send_sms(RECIPIENT_PHONE_NUMBER, MESSAGE_TO_SEND)
        if response.is_confirmed():
                print("OK: {}.".format(response.get_message()))
        else:
                print("Text sending error({}): {}".format(response.get_code().value, response.get_message()), file = sys.stderr)

except Exception as e:
        print("Execution error: {}.".format(e), file = sys.stderr)
        exit(1)
finally:
        if not client is None:
                client.close_server_connection()

exit(0)
   adb shell service call isms 5 s16 "com.android.mms" 
