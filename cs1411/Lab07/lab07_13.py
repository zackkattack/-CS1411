def payment(P):

    try:
        if P >= 20 or P <= 1000:
            return " Sucess."
        elif p < 20:
            return "Retry. Your payment is less than the minimum payment due."
        elif p > 1000:
            return "Retry. Your payment is greater than the minimum payment due."
    except ValueError:
        return "Retry, not a valit input"
