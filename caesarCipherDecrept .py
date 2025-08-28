message = 'KhorrRpduPrkdphg'
SYMBOLS= 'ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890?!'
for key in range(len(SYMBOLS)):
    translated=''
    for symbol in message :
        if symbol in SYMBOLS:
            symbolindix=SYMBOLS.find(symbol)
            translatedindix = symbolindix - key
            if translatedindix < 0 :
                translatedindix = translatedindix + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedindix]
        else:
            translated = translated + symbol
    print('key #%s: %s' % (key , translated)) 