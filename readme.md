

```python
from avaalphaapi import get_stock
```


```python
get_stock?
```


```python
stock_name = 'ADVANC'
start_date = '2017-06-14 12:00:00'
end_date = '2017-07-14 12:00:00'
indicators = ['macd','ema_25', 'rsi_7']
```


```python
get_stock(name=stock_name, start=start_date).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>adj_close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-06-14 14:00:00</td>
      <td>173.0</td>
      <td>173.5</td>
      <td>173.0</td>
      <td>173.5</td>
      <td>71400</td>
      <td>173.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-06-14 15:00:00</td>
      <td>173.5</td>
      <td>174.0</td>
      <td>173.0</td>
      <td>173.5</td>
      <td>1106200</td>
      <td>173.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-06-14 16:00:00</td>
      <td>173.5</td>
      <td>174.5</td>
      <td>173.5</td>
      <td>174.5</td>
      <td>919300</td>
      <td>173.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-06-15 09:00:00</td>
      <td>173.5</td>
      <td>174.0</td>
      <td>173.5</td>
      <td>174.0</td>
      <td>44000</td>
      <td>174.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-06-15 10:00:00</td>
      <td>173.5</td>
      <td>174.5</td>
      <td>173.5</td>
      <td>174.5</td>
      <td>662000</td>
      <td>174.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_stock(name=stock_name, end=end_date).tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>adj_close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1852</th>
      <td>2017-07-13 15:00:00</td>
      <td>187.0</td>
      <td>187.0</td>
      <td>186.5</td>
      <td>186.5</td>
      <td>331600</td>
      <td>187.0</td>
    </tr>
    <tr>
      <th>1853</th>
      <td>2017-07-13 16:00:00</td>
      <td>187.0</td>
      <td>187.5</td>
      <td>186.5</td>
      <td>187.0</td>
      <td>1605200</td>
      <td>186.5</td>
    </tr>
    <tr>
      <th>1854</th>
      <td>2017-07-14 09:00:00</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>188.0</td>
      <td>188.5</td>
      <td>407100</td>
      <td>187.0</td>
    </tr>
    <tr>
      <th>1855</th>
      <td>2017-07-14 10:00:00</td>
      <td>188.0</td>
      <td>188.5</td>
      <td>188.0</td>
      <td>188.0</td>
      <td>813400</td>
      <td>188.5</td>
    </tr>
    <tr>
      <th>1856</th>
      <td>2017-07-14 11:00:00</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>188.0</td>
      <td>188.5</td>
      <td>1790900</td>
      <td>188.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_stock(name=stock_name, end=end_date).tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>adj_close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1852</th>
      <td>2017-07-13 15:00:00</td>
      <td>187.0</td>
      <td>187.0</td>
      <td>186.5</td>
      <td>186.5</td>
      <td>331600</td>
      <td>187.0</td>
    </tr>
    <tr>
      <th>1853</th>
      <td>2017-07-13 16:00:00</td>
      <td>187.0</td>
      <td>187.5</td>
      <td>186.5</td>
      <td>187.0</td>
      <td>1605200</td>
      <td>186.5</td>
    </tr>
    <tr>
      <th>1854</th>
      <td>2017-07-14 09:00:00</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>188.0</td>
      <td>188.5</td>
      <td>407100</td>
      <td>187.0</td>
    </tr>
    <tr>
      <th>1855</th>
      <td>2017-07-14 10:00:00</td>
      <td>188.0</td>
      <td>188.5</td>
      <td>188.0</td>
      <td>188.0</td>
      <td>813400</td>
      <td>188.5</td>
    </tr>
    <tr>
      <th>1856</th>
      <td>2017-07-14 11:00:00</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>188.0</td>
      <td>188.5</td>
      <td>1790900</td>
      <td>188.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_stock(name=stock_name, indicators=indicators).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>adj_close</th>
      <th>close</th>
      <th>ema_25</th>
      <th>high</th>
      <th>low</th>
      <th>macd_12_26_9</th>
      <th>macdhist_12_26_9</th>
      <th>macdsignal_12_26_9</th>
      <th>open</th>
      <th>rsi_7</th>
      <th>volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-06-15 12:00:00</td>
      <td>163.5</td>
      <td>163</td>
      <td>157.247</td>
      <td>163.5</td>
      <td>162.5</td>
      <td>-0.180899</td>
      <td>-0.0541909</td>
      <td>-0.126708</td>
      <td>163.5</td>
      <td>7.69231</td>
      <td>800200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-06-15 14:00:00</td>
      <td>163</td>
      <td>163</td>
      <td>157.27</td>
      <td>163.5</td>
      <td>162.5</td>
      <td>-0.291492</td>
      <td>-0.131828</td>
      <td>-0.159665</td>
      <td>163</td>
      <td>7.69231</td>
      <td>1412600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-06-15 15:00:00</td>
      <td>163</td>
      <td>162</td>
      <td>157.29</td>
      <td>163</td>
      <td>162</td>
      <td>-0.45459</td>
      <td>-0.23594</td>
      <td>-0.21865</td>
      <td>162.5</td>
      <td>7.69231</td>
      <td>896500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-06-15 16:00:00</td>
      <td>162</td>
      <td>162.5</td>
      <td>157.352</td>
      <td>163</td>
      <td>162</td>
      <td>-0.417649</td>
      <td>-0.159199</td>
      <td>-0.25845</td>
      <td>162.5</td>
      <td>5.6294</td>
      <td>2133500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-06-16 09:00:00</td>
      <td>162.5</td>
      <td>161</td>
      <td>157.321</td>
      <td>161.5</td>
      <td>160.5</td>
      <td>-0.34406</td>
      <td>-0.0684887</td>
      <td>-0.275572</td>
      <td>160.5</td>
      <td>33.4089</td>
      <td>736300</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_stock(name=stock_name, start=start_date, end=end_date, indicators=indicators).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>adj_close</th>
      <th>close</th>
      <th>ema_25</th>
      <th>high</th>
      <th>low</th>
      <th>macd_12_26_9</th>
      <th>macdhist_12_26_9</th>
      <th>macdsignal_12_26_9</th>
      <th>open</th>
      <th>rsi_7</th>
      <th>volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-06-14 14:00:00</td>
      <td>173</td>
      <td>173.5</td>
      <td>178.377</td>
      <td>173.5</td>
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>173</td>
      <td>NaN</td>
      <td>71400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-06-14 15:00:00</td>
      <td>173.5</td>
      <td>173.5</td>
      <td>178.387</td>
      <td>174</td>
      <td>173</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>1106200</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-06-14 16:00:00</td>
      <td>173.5</td>
      <td>174.5</td>
      <td>178.357</td>
      <td>174.5</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>919300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-06-15 09:00:00</td>
      <td>174.5</td>
      <td>174</td>
      <td>178.368</td>
      <td>174</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>44000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-06-15 10:00:00</td>
      <td>174</td>
      <td>174.5</td>
      <td>178.378</td>
      <td>174.5</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>173.5</td>
      <td>NaN</td>
      <td>662000</td>
    </tr>
  </tbody>
</table>
</div>


