class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []

while True:
    emails = input()
    if emails == "Stop":
        break
    emails = emails.split()
    emails_list.append(Email(emails[0], emails[1], emails[2]))

send_indices = list(map(int, input().split(", ")))

for i in range(len(emails_list)):
    if i in send_indices:
        emails_list[i].send()

[print(email.get_info()) for email in emails_list]
