def initialize(context):
    #贵州茅台
    g.security = ['600519.SS', '000001.SS']
    set_universe(g.security)
    log.info("start[%s] end[%s]" % (g.start, g.end))

def handle_data(context, data):
    mt = g.security[0]
    ss = g.security[1]

    last_price1 = data[mt]['price']
    last_price2 = data[ss]['price']
    log.info("nowprice [%s][%s]" % (last_price1, last_price2))
    record(price=last_price)
