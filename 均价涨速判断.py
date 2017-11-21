def initialize(context):
    #贵州茅台
    #g.security = '600519.SS'
    g.security = '002415.SZ'
    #g.security = '600570.SS'
    set_universe(g.security)
    log.info("start[%s] end[%s]" % (g.start, g.end))

def handle_data(context, data):
    se = g.security
    record(price=data[se].price)

    ma2 = data[se].mavg(2, 'close')
    ma4 = data[se].mavg(4, 'close')
    ma6 = data[se].mavg(6, 'close')
    ma8 = data[se].mavg(8, 'close')
    ma10 = data[se].mavg(10, 'close')
    open_price = data[se]['open']
    close_price = data[se]['close']
    #buy_cash = int(context.portfolio.capital_base/100) * 100 /10
    buy_amount = int(context.portfolio.starting_cash/open_price/100)*100 /10
    log.info("price[%s] [%s] [%s] [%s]" % (ma2, ma4, open_price, close_price))
    
    if ma2 > ma10 and ma2 > ma4:
        order(se, buy_amount)
        log.info("Buying %s[%s][%s]" % (se, buy_amount, context.portfolio.positions[se].amount))
    elif ma2 < ma4 and ma4 < ma6 and ma2 - ma4 < ma4 - ma6:
        order_target(se, -buy_amount) 
        log.info("Selling %s" % (se))
