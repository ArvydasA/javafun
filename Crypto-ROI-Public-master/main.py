import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

cardData = pd.read_csv('CardData.csv', header=0, encoding='utf-8-sig')
coinData = pd.read_csv('CoinData.csv', header=0, encoding='utf-8-sig')
baseCost = pd.read_csv('BaseCost.csv', header=0, encoding='utf-8-sig')
numCards = len(cardData.index)
numCoins = len(coinData.index)
baseCost1 = baseCost.at[0,'CPU Price'] + baseCost.at[0, 'Mobo Price'] + baseCost.at[0, 'SSD Price'] + baseCost.at[0, 'Case Price'] + baseCost.at[0, 'PSU Price'] + baseCost.at[0, 'RAM Price']
multCard = int(sys.argv[1])

powerCost = pd.Series()

for i in range (0, numCards):
    powerCost2 = pd.Series(((cardData.at[i, 'Power Consumption'] * 24 * baseCost.at[0, 'Power Cost']/1000) * multCard), index =[i])
    powerCost = powerCost.append(powerCost2)

costEquip = pd.Series()

for i in range (0, numCards):
    costEquip1 = pd.Series(baseCost1 + (cardData.at[i, 'Cost'] * multCard), index=[i])
    costEquip = costEquip.append(costEquip1)
costEquipdf = pd.DataFrame(costEquip, columns=['Initial Investment'])

dailyIncomedf = pd.DataFrame()

for j in range (0,numCoins):
    dailyIncome = pd.Series()
    for i in range (0,numCards):
        dailyIncome1 = pd.Series(((cardData.at[i, coinData.at[j, 'Coin'] + ' Hashrate'] * multCard) / coinData.at[j, 'Network Hashrate'] ) * (86400 / coinData.at[j, 'Block Time']) *
        coinData.at[j, 'Block Reward'] * coinData.at[j, 'Value in USD'] - powerCost[i], index=[i])
        dailyIncome = dailyIncome.append(dailyIncome1)
    dailyIncome1df = pd.DataFrame(dailyIncome, columns=[coinData.at[j, 'Coin'] + ' Daily Income'])
    dailyIncomedf = pd.concat([dailyIncomedf, dailyIncome1df], axis=1)
roidf = pd.DataFrame()

for j in range (0, numCoins):
    roi = pd.Series()
    for i in range (0,numCards):
        roi1 = pd.Series(costEquipdf.at[i, 'Initial Investment'] / (dailyIncomedf.at[i, coinData.at[j, 'Coin'] + ' Daily Income']), index=[i])
        roi = roi.append(roi1)
    roi1df = pd.DataFrame(roi, columns=[coinData.at[j, 'Coin'] + ' ROI'])
    roidf = pd.concat([roidf, roi1df], axis=1)

finaldf = pd.concat([cardData['Card'], costEquipdf, dailyIncomedf, roidf], axis=1)
print(finaldf)

ax = finaldf[['ETH ROI', 'ETC ROI', 'ZEC ROI']].plot(kind='bar', x=finaldf['Card'], title="Return-on-Investment " + sys.argv[1] + " Cards", figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("GPU",fontsize=12)
ax.set_ylabel("Days",fontsize=12)
plt.savefig("ROI" + sys.argv[1] + ".png")
