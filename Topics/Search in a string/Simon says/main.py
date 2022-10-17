def what_to_do(instructions):
    key = "Simon says"
    if instructions.startswith(key):
        return "I " + instructions[11:]
    elif instructions.endswith(key):
        return "I " + instructions[:11]
    else:
        return "I won't do it!"
