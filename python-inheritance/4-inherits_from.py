def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
