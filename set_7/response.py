import validator_collection
import validator_collection.errors

try:
    mail = input("What's your email address? ")

    email_address = validator_collection.email(mail)

    if email_address == mail:
        print("Valid")

except validator_collection.errors.InvalidEmailError:
    print("Invalid")