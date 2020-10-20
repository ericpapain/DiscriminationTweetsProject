# Target encoding 
def encoding_target(y):
    '''
        y : DataFrame of one column shape
    '''
    for i in range(y.shape[0]):
        if y[i] == 'none':
            y[i] = 0 
        else:
            y[i] = 1 
    return y.astype('int')

# Convert Emojis 
def convert_emojis(text): 
    '''
        text : string 
    '''
    import emoji
    text = emoji.demojize(text)
    text = text.replace('_','')
    return text.replace(':','')