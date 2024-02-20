import math
import scipy

# This script can be used to calculate the price of European Currency Options

quotation = "EUR/USD"
spot_rate = 1.1743 # Spot rate EUR/USD
strike_price = 1.1770
us_1mth = 0.0025  # Home Currency
eur_1mth = -0.0019519  # Foreign Currency
volatility = 0.12 # equal to 12 %
expiration = 30 # Expiration is measured in days till expiration

def Black_Scholes_Foreign_Exchange(spot_rate, strike_price, us_1mth, eur_1mth, volatility, expiration, option):
    t = expiration / 365
    d1 = (math.log(spot_rate/strike_price) + ((us_1mth - eur_1mth + ((volatility ** 2) / 2)) * t))
    d2 = d1 - volatility * math.sqrt(t)
    if option == "call":
        price = math.e ** (-us_1mth * t) * spot_rate * (scipy.stats.norm.cdf(d1)) - math.e ** (-eur_1mth * t) \
                * strike_price * scipy.stats.norm.cdf(d2)
    elif option == "put":
        price = math.e ** (-us_1mth * t) * strike_price * (scipy.stats.norm.cdf(-d2)) - math.e ** (-eur_1mth * t) \
                * spot_rate * scipy.stats.norm.cdf(-d1)
    return price.round(3)

call_price = Black_Scholes_Foreign_Exchange(spot_rate, strike_price,us_1mth, eur_1mth, volatility, expiration, "call")
put_price = Black_Scholes_Foreign_Exchange(spot_rate, strike_price,us_1mth, eur_1mth, volatility, expiration, "put")

print(f"Call: {quotation} {call_price}")
print(f"Put: {quotation} {put_price}")
