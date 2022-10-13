def ema_5(data):
    try:
        data['ema'] = data['Close'].ewm(span=5).mean()
        return data['ema']
    except:
        print('Not sufficient data')

def ema_strat():
    pass