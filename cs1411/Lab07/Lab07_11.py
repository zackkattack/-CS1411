def finalCost( cost, isMember):
    discount = .05
    if isMember:
        discount +=.1

    return (cost - (cost*discount))
