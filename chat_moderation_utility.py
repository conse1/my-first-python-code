def send_alert():
    print("The system is active. Test passed")
while True:
    morgen = input("enter word: ")
    shtern = morgen.lower()
    if shtern == "stop":
        break
    else:
        send_alert()
