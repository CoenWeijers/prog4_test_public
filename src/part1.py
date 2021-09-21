def volume_kubus(x):
    """Return the volume of a cube

    Raise a RuntimeError exception with message "negatieve lengte" if x < 0.
    """
    if x < 0:
        raise RuntimeError("negatieve lengte")
    else:
        return x**3    


def minutes_in_day(x):
    """Return the number of minutes in x days

    Raise a custom NegativeDuration exception if x < 0.
    """
    #class NegativeDuration(RuntimeError):
    #pass
    #def minutes_in_day
    #if x < 0:
    #    raise NegativeDuration


def minutes_in_week(x):
    """Return the number of minutes in x weeks"""

    return x*24*7*60


def list_of_squares(n):
    """Return a list of the first n squares

    >>> list_of_squares(3)
    [0, 1, 4]
    """
    l = []
    lambda
    pass


def product_of_list(l):
    """Return the product of all numbers in the list

    >>> product_of_list([2,3,4])
    24
    """
    pass


def price_search(articles, name):
    """Return the price of the article in list articles

    >>> articles = [
        ["Doom", 25],
        ["Among Us", 5],
    ]
    >>> price_search("Doom")
    25
    """
    pass
