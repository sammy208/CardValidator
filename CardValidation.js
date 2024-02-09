const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function validateCreditCardNumber(cardNumber) {
    // Regular expressions to match different credit card patterns
    const visaRegex = /^4[0-9]{12}(?:[0-9]{3})?$/;
    const mastercardRegex = /^5[1-5][0-9]{14}$/;
    const amexRegex = /^3[47][0-9]{13}$/;
    const discoverRegex = /^6(?:011|5[0-9]{2})[0-9]{12}$/;

    // Check if the card number matches any of the regex patterns
    if (visaRegex.test(cardNumber)) {
        return "Visa";
    } else if (mastercardRegex.test(cardNumber)) {
        return "Mastercard";
    } else if (amexRegex.test(cardNumber)) {
        return "American Express";
    } else if (discoverRegex.test(cardNumber)) {
        return "Discover";
    } else {
        return "Unknown";
    }
}

function validateCardLength(cardNumber) {
    // Object containing the lengths of different card types
    const cardLengths = {
        "Visa": [13, 16],
        "Mastercard": [16],
        "American Express": [15],
        "Discover": [16]
    };

    // Get the card type
    const cardType = validateCreditCardNumber(cardNumber);

    // If card type is unknown, return false
    if (cardType === "Unknown") {
        return false;
    }

    // Check if the card number length is valid for the card type
    const validLengths = cardLengths[cardType];
    return validLengths.includes(cardNumber.length);
}

rl.question('Please enter your credit card number: ', (cardNumber) => {
    // Validate the card type and length
    const cardType = validateCreditCardNumber(cardNumber);
    const isLengthValid = validateCardLength(cardNumber);

    // Display the results
    if (cardType !== "Unknown" && isLengthValid) {
        console.log("Card Type:", cardType);
        console.log("Your credit card number is valid!");
    } else {
        console.log("Invalid credit card number or unknown card type.");
    }

    rl.close();
});