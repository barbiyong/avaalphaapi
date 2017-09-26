'''wrapper.py get datafrom blob to dataframe'''
import io
import requests

import pandas as pd

def get_stock(name, start=None, end=None, indicators=None, tf='1h'):
    ''' get_stock function '''
    def get_ohlc(name):
        ''' get only ohlc function '''
        key = '?sv=2017-04-17&ss=b&srt=co&sp=rl&se=2017-12-31T19:24:13Z&st=2017-08-09T11:24:13Z&spr=https&sig=eIzdj9tJg5tkLHtDtfr7Or5ckH5M%2B4t73bFhMOo%2F3eQ%3D'
        path = 'https://mkaxstorage18867.blob.core.windows.net/api/'
        path = path + tf + '/' + 'ohlc/' + name
        dir_list = [2016, 2017]
        tmp_df_list = []
        for i, year in enumerate(dir_list):
            url = path + '/' + str(year) + '/' + '_data' + key
            tmp_data = requests.get(url).content
            tmp_df = pd.read_csv(io.StringIO(tmp_data.decode('utf-8')))
            tmp_df_list.append(tmp_df)
        ohlc = pd.DataFrame().append(tmp_df_list)
        return ohlc.reset_index(drop=True)
    def get_ohlc_indicators(name):
        ''' get ohlc with indicators function '''
        df = get_ohlc(name)
        for i in indicators:
            indicatior_name, period = indicator_delimiter(i)
            df = pd.concat([df, get_indicator(name, indicatior_name, period)], axis=1)
        return df.T.groupby(level=0).first().T
    def get_indicator(stock_name, indicatior_name, period):
        ''' get indicator function '''
        key = '?sv=2017-04-17&ss=b&srt=co&sp=rl&se=2017-12-31T19:24:13Z&st=2017-08-09T11:24:13Z&spr=https&sig=eIzdj9tJg5tkLHtDtfr7Or5ckH5M%2B4t73bFhMOo%2F3eQ%3D'
        path = 'https://mkaxstorage18867.blob.core.windows.net/api/'
        if indicatior_name == 'macd':
            path = path + tf + '/' + indicatior_name + '/' + '12/26/9' + '/' + stock_name
        else:
            path = path + tf + '/' + indicatior_name + '/' + str(period) + '/' + stock_name
        dir_list = [2016, 2017]
        tmp_df_list = []
        for i, year in enumerate(dir_list):
            url = path + '/' + str(year) + '/' + '_data' + key
            tmp_data = requests.get(url).content
            tmp_df = pd.read_csv(io.StringIO(tmp_data.decode('utf-8')))
            tmp_df_list.append(tmp_df)
        indi = pd.DataFrame().append(tmp_df_list)
        return indi.reset_index(drop=True)
    def indicator_delimiter(name):
        ''' dilimit indicator name '''
        if type(name) == str:
            name = name.split('_', 1)
            indicatior_name = name[0]
            try:
                period = name[1]
            except:
                period = None
        elif type(name) == tuple:
            indicatior_name = name[0]
            try:
                period = name[1]
            except:
                period = None
        return indicatior_name, period
    def windowed(df, start, end):
        ''' slice data '''
        try:
            if start is not None:
                df = df[(df['Date'] > start)]
            if end is not None:
                df = df[(df['Date'] < end)]
        except:
            if start is not None:
                df = df[(df['date'] > start)]
            if end is not None:
                df = df[(df['date'] < end)]
        return df.reset_index(drop=True)

    if start is None and end is None and indicators is None:
        # get only all ohlc
        return get_ohlc(name)
    elif (start is not None or end is not None) and indicators is None:
        return windowed(get_ohlc(name), start, end)
    elif start is None and end is None and indicators is not None:
        # all ohlc + indicators
        return get_ohlc_indicators(name)
    elif (start is not None or end is not None) and indicators is not None:
        return windowed(get_ohlc_indicators(name), start, end)
