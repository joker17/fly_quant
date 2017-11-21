def initialize(context):
    #贵州茅台
    #g.security = '600519.SS'
    g.security = '600570.SS'
    set_universe(g.security)
    log.info("start[%s] end[%s]" % (g.start, g.end))

def handle_data(context, data):
    se = g.security
    record(price=data[se].price)

    ma5 = data[se].mavg(5, 'close')
    ma10 = data[se].mavg(10, 'close')
    last_price = data[se]['price']
    
    buycash = context.portfolio.cash/10

    if ma5 > ma10:
        #order(se, 100)
        order_value(se, buycash)
        log.info("Buying %s[%s]" % (se, context.portfolio.positions[se].amount))
    elif ma5 < ma10 and context.portfolio.positions[se].amount > 0:
        order_target(se, 0)
        log.info("Selling %s" % (se))
    
    # 绘制股票价格
    #record(stock_price=data[se].close,high_price=data[se].high)
    # 绘制五日均线价格
    #record(ma5=ma5,ma10=ma10)
    # 绘制十日均线价格
    #record(ma10=ma10)
