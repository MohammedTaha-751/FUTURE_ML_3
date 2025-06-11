import unittest
from chatbot.model import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = Chatbot(faq_path="data/faq.json")

    def test_return_policy(self):
        response, confidence = self.bot.get_response("What is your return policy?")
        self.assertIn("30 days", response)

    def test_contact_support(self):
        response, confidence = self.bot.get_response("How to reach support?")
        self.assertIn("support", response.lower())

    def test_shipping(self):
        response, confidence = self.bot.get_response("Do you deliver to other countries?")
        self.assertIn("ship", response.lower())

    def test_payment_methods(self):
        response, confidence = self.bot.get_response("What payments do you take?")
        self.assertTrue(any(word in response.lower() for word in ["paypal", "credit", "debit"]))

if __name__ == "__main__":
    unittest.main()
