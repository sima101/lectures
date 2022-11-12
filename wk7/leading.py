def main():
    pass

def leading_substrings(s):
    """Take string s as input and return a list of all 
    the substrings that start from the beginning.
    E.g., leading_substrings('bear') will return 
    ['b', 'be', 'bea', 'bear'].
    """
    return [s[:i+1] for i in range(len(s))]

if __name__ == "__main__":
    main()