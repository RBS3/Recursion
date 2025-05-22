def initiator(count):
    if count == 0:
        return
    print(f"Initiator: Initiating message {count}.")
    responder(count - 1)
#time complexity:o(n)
def responder(count):
    if count == 0:
        return
    print(f"Responder: Responding to message {count}.")
    initiator(count - 1)
#time complexity:o(n)