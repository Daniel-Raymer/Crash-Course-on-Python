def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@gmail.com", "Alex Deigo"),
                   ("shay@gmail.com", "Shay Brandt")]))