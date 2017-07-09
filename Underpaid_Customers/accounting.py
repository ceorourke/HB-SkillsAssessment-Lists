melon_cost = 1.00

def underpaid_report(filename):
    """Prints out a list of customer who've underpaid or overpaid"""

    #opens the file
    customer_orders = open(filename)

    #iterates through each line in the file
    for line in customer_orders:
        #strips the white space off the end
        line = line.rstrip()
        #splits at the | delimiter and stores it in a new list
        words = line.split("|")

        #stores the customer name
        customer_name = words[1]
        #stores customer's first name by splitting the full name
        customer_first = customer_name.split(" ")[0]
        #stores the number of melons purchased
        customer_melons = float(words[2])
        #stores the amount the customer paid
        customer_paid = float(words[3])

        #calculates the expected payment
        customer_expected = customer_melons * melon_cost

        #check if the customer overpaid
        if customer_expected < customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected)
            print "{} has overpaid for their melons.".format(customer_first)

        #checks if the customer underpaid
        elif customer_expected > customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected)
            print "{} has underpaid for their melons.".format(customer_first)

    #closes the file
    customer_orders.close()

#calls the function
underpaid_report("customer-orders.txt")