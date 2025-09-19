# upi_payments_QR
This Python script allows a user to generate a QR code for a UPI payment using just their UPI ID. It utilizes the qrcode library to create and save the QR code, which can then be scanned by any UPI-compatible app (like Google Pay, PhonePe, Paytm, etc.) for quick payments.


🔍 How It Works:

User Input:

The script prompts the user to enter their UPI ID (e.g., username@bank).

Create UPI Payment URL:

It constructs a standard UPI payment URL using the format:

upi://pay?pa=<upi_id>&cu=INR


pa = Payee address (your UPI ID)

cu = Currency (INR)

Generate QR Code:

The script uses the qrcode library to generate a QR code from the UPI link.

Save and Display QR Code:

The QR code is saved locally as upi_qr.png.

It is also displayed in a pop-up window for immediate use.

Success Message:

Once the QR is created and saved, it prints:
✅ QR Code generated successfully!

🧰 Requirements:

Python installed on your machine

qrcode library (install via pip install qrcode[pil] if not already installed)

✅ Use Case:

This script is especially useful for:

Shopkeepers, freelancers, or small business owners

Creating printable UPI QR codes for payments without relying on third-party apps
