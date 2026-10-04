import os
from flask import Flask, request
import openai

app = Flask(__name__)

# WhatsApp AI Support Agent for Nurse Burnout Guide
FAQ_RESPONSES = {
    "price": "The Nurse Burnout Guide is $27. Payment link: your-payhip-link.com",
    "refund": "We have 30-day money back guarantee. Just email support@yourdomain.com",
    "download": "After payment, check your email spam folder for download link. Resend? Send your email.",
    "content": "Includes 50-page burnout recovery plan, shift checklists, self-care templates"
}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_msg = data.get('message', '').lower()
    
    # Auto-handle FAQs
    for key, response in FAQ_RESPONSES.items():
        if key in user_msg:
            return {"reply": response}
    
    # Fallback to OpenAI for complex queries
    # openai.api_key = os.getenv("OPENAI_KEY")
    # ai_reply = openai.ChatCompletion.create(...)
    
    return {"reply": "Hi! I'm your support assistant. How can I help with your Nurse Guide order? Type: price, refund, download, content"}

if __name__ == '__main__':
    app.run(port=5000)
