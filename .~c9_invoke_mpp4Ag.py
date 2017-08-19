from flask import Flask, flash, redirect, render_template, request, session, url_for
import re

import helpers

# configure application
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/check", methods=["GET","POST"])
def check():
    if request.method == "POST":
        cardType = request.form.get("cardType")
        Account = request.form.get("Account")
        #check that the user input an account number
        if not Account:
            return render_template("invalid.html")
        #check that the user selected a card type
        if not cardType:
            return render_template("invalid.html")

        #remove any dashes from the card number, will also ensure tha the number is never negative
        for letter in Account:
            Account = re.sub('[-]', '', Account)
        #make sure that the account number provided is all numbers
        if not Account.isdigit():
            return render_template("invalid.html")
        Account = str(Account)
        length = len(Account)
        one_numbers = int(Account[:1])
        two_numbers = int(Account[:2])
        four_numbers = int(Account[:4])

        # http://validcreditcardnumbers.info/?p=9
        # check that the length and first digits match for the credit card entered
        check = helpers.check(cardType, length, one_numbers, two_numbers, four_numbers)
        if check == False:
            return render_template("invalid2.html")
        else:
            Luhn = helpers.Luhn(Account)
            if Luhn == True:
                return render_template("valid.html")
            else:
                return render_template("invalid.html")
    else:
        return render_template("index.html")

