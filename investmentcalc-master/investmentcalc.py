#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description='Calculate profit.')
parser.add_argument('annual_invest_amount', type=float)
parser.add_argument('years_of_investment', type=int)
parser.add_argument('percent_profit', type=float)
parser.add_argument('--initial_fund', dest='initial_fund', type=float,
  default=0)
parser.add_argument('-v', dest='verbose', type=int,
  default=0)

args = parser.parse_args()

total_value = args.initial_fund
total_fund= args.initial_fund
interest = 0
for year in range(args.years_of_investment):
  total_fund += args.annual_invest_amount
  total_value += args.annual_invest_amount
  interest = total_value * args.percent_profit/100
  total_value += interest
  percent_profit = ((total_value - total_fund) / total_fund
    ) * 100

  if (args.verbose == 1):
    print("year=" + str(year+1) + 
      ", total fund=" + "{:,.2f}".format(total_fund) +
      ", total value=" + "{:,.2f}".format(total_value) +
      ", percent profit=" + "{:,.2f}".format(percent_profit) + "%")

print("{:,.2f}".format(total_value))
