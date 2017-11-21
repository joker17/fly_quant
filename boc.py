def initialize(context):
    g.security = '600570.SS'

    set_universe([g.security])

def handle_data(context, data):
    if g.security not in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)
    pass