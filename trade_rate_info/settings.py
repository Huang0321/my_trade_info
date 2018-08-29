# import pymysql
#
#
# # 创建数据库连接对象
# connect = pymysql.connect(host='119.28.227.49',
#                           port=3306,
#                           user='admin',
#                           password='admin',
#                           db='trade_pair_data',
#                           cursorclass=pymysql.cursors.DictCursor)


# 配置api_key 和 api_secret
KEY_SECRET = {
    'okex': ('6a689877-06c6-48b3-a4e2-5ce3b5931cc4', '3028064C9FA41F4C97070E7681FA9888'),
    'bittrex': ('d92a7f5fa0ad45589eaa2b7e6eb73457', '2f44fcd470584dfcbb5b71b5ca34583c'),
    'binance': ('sNc8z2KHjfxdrxPZOeOvnlJXjgxHBbVqORUusv8oSWKRWFaZRDblk9bk6CfI1PpH',
                'FmXczpQ6WbUMgtcclYolSUGfsCeoYRzsudGKpx6cp72oNKZdWTMCJX7A10V1g14G'),
    'gateio': ('CA3B32BD-BBF7-4142-A8F0-B6F687AB5ED9',
               '19dcf709446f2638e927b3200b8337acadc3029d062f0d09a95caed907ad949c')
}


# 静态价格,便于计算交易市值, 单位：￥
BTC_VALUE = 43773
ETH_VALUE = 1916
USDT_VALUE = 6.86

SYMBOL = 'VET/USDT'

# 设置交易正反向利差
RATE_1 = 0.0035
RATE_2 = 0.0035

MAX_VOLUME = 200  # 单位： ETH gateio
MIN_VOLUME = 0.001  # 单位： ETH gateio