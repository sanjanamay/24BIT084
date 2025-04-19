name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")
address = input("Enter Address: ")
vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD
"""
filename = "contact.vcf"
with open(filename, 'w') as file:
    file.write(vcard)

print(f"vCard created successfully and saved as {filename}")
