def effectiveness(x, y):
    # Bayes rule
    # P(cancer|positive) = P(positive|cancer)*P(cancer)/P(positive)
    # P(positive|cancer) = y/100
    # P(cancer) = x/100
    # P(positive) = P(positive|cancer)*P(cancer)+P(positive|non-cancer)*P(non-cancer)
    # P(positive|non-cancer) = (100-y)/100
    # P(non-cancer) = (100-x)/100
    return (y/100.0*x/100.0)/(x*y/10000.0)

print effectiveness(34, 49)
