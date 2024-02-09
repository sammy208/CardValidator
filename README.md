# CardValidator

# About the code
This code includes a new function validateCardLength() that checks if the length of the provided card number is valid for the detected card type. If the length is valid, it returns true; otherwise, it returns false. This helps indicate whether the card number input is complete or not based on the expected lengths of various card types.
# Explanation of the regular expressions:
 This explains how the code works on every card.
# visaRegex:
 This pattern starts with a 4 and is followed by 12 digits. Optionally, it can have 3 more digits at the end.
# mastercardRegex: 
 This pattern starts with 51-55 and is followed by 14 digits.
# amexRegex: 
 This pattern starts with 34 or 37 and is followed by 13 digits.
# discoverRegex:
 This pattern starts with 6011 or 65 and is followed by 12 digits.
 
These regex patterns capture the common formats of Visa, Mastercard, American Express, and Discover credit card numbers.
