def send_message(message):
    from twilio.rest import Client

    client = Client("ACe2ef31a4d09f9846afcd486586495973", "8d2e36f767db9c4948d5ad81a03e933d")

    numbers=["+917202964175","+918690909695"]
    names=["Hardeep","Ahmed"]

    for i in range(2):
        m=("Hello {} ".format(names[i]))+message
        client.messages.create(to=numbers[i], 
                            from_="+13092711496", 
                            body=(m))
