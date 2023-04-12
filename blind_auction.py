print("Welcome to the blind auction!\n---------------------\n")


auction_objects = {"Thor's hammer": 300, "Angel dust": 300}


def auction():
    objects_goes_to = {}
    for key, value in auction_objects.items():
        print(f"{key}. Starting bid is {value}.")
        name = input("What is your name? ")
        bid = int(input("What's your bid: $"))

        if bid > value:
            auction_objects.update({key: bid})
            objects_goes_to[name] = key
        else:
            print("You can't bid less than the starting price of the auctioned object.")

        any_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
        while any_other_bidder == "yes":
            other_name = input("What is your name? ")
            other_bid = int(input("What's your bid: $"))
            if other_bid > bid:
                auction_objects[key] = other_bid
                del objects_goes_to[name]
                objects_goes_to[other_name] = key
                bid = other_bid
            any_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
        if any_other_bidder == "no":
            continue
    print("The auction has ended. The following objects have been sold:")
    for name, object_name in objects_goes_to.items():
        print(f"{name} bought {object_name} for ${auction_objects[object_name]}")


auction()
