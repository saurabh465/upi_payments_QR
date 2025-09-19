import qrcode

# Taking UPI Id
upi_id = input("Enter your UPI Id: ")

# UPI link (universal, without name)
upi_url = f'upi://pay?pa={upi_id}&cu=INR'

# Generate QR
qr = qrcode.make(upi_url)

# Save QR
qr.save('upi_qr.png')

# Show QR
qr.show()

print("\n✅ QR Code generated successfully!")
