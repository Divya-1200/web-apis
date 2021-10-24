import stripe

charge = stripe.Charge.retrieve(
  "ch_3JnxBw2eZvKYlo2C0jpKc9vq",
  api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
)
charge.save() # Uses the same API Key.