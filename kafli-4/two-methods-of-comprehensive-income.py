#! python3

# given values
salesRevenue=800000
costOfGoodsSold=600000
operatingExpenses = 90000
unrealizedGainNetOfTax = 30000

# computed values
grossProfit = 0
netIncome = 0
comprehensiveIncome = 0

# calculations
grossProfit = salesRevenue - costOfGoodsSold
netIncome = grossProfit - operatingExpenses
comprehensiveIncome = netIncome + unrealizedGainNetOfTax

# Illustration 4.21
print(f"One statement approach:")

print(f"Statement of Comprehensive Income")
print(f"For the Year ended December 31, 2022")
print(f"Sales Revenue       {salesRevenue}")
print(f"Cost of goods sold  {costOfGoodsSold}")
print(f"Gross profit        {grossProfit}")
print(f"Operating expenses  {operatingExpenses}")
print(f"Net income          {netIncome}")
print(f"Other comprehensive income")
print(f""Unrealized holding gain on nontrading equity \n securities, net of tax   {unrealizedGainNetOfTax}")
print(f"Comprehensive income {comprehensiveIncome}")

# Illustration 4.22
print(f"Two statement approach:")

print(f"Income Statement")
print(f"For the Year ended December 31, 2022")
print(f"Sales Revenue       {salesRevenue}")
print(f"Cost of goods sold  {costOfGoodsSold}")
print(f"Gross profit        {grossProfit}")
print(f"Operating expenses  {operatingExpenses}")
print(f"Net income          {netIncome}")

print(f"Comprehensive Income Statement")
print(f"For the Year ended December 31, 2022")
print(f"Net income          {netIncome}")
print(f"Other comprehensive income")
print(f""Unrealized holding gain on nontrading equity \n securities, net of tax   {unrealizedGainNetOfTax}")
print(f"Comprehensive income {comprehensiveIncome}")
