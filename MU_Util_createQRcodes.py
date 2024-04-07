import qrcode
import vobject

def create_vcard_qr(name, surname, phone, email, url):
    # Create a vCard
    vcard = vobject.vCard()
    vcard.add('n').value = vobject.vcard.Name(family=surname, given=name)
    vcard.add('fn').value = f"{name} {surname}"
    vcard.add('tel').value = phone
    vcard.add('tel').type_param = 'CELL'
    vcard.add('email').value = email
    vcard.add('url').value = url

    # Convert the vCard to a string
    vcard_str = vcard.serialize()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_str)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    img.save("contact_qr.png")

# Example usage
create_vcard_qr("Fabio", "Bertellotti", "'+393892882181", "fabio.bertellotti@gmail.com", "http://mecenaite.it")
