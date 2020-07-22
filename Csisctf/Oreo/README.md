# Oreo

Oreo was a web 100 challenge

On visiting the [website](http://chall.csivit.com:30243), there is a single line
```
My nephew is a fussy eater and is only willing to eat chocolate oreo. Any other flavour and he throws a tantrum.
```

Page source doesn't have anything intresting too.

On looking on the **Storage** tab in developers tool, we see a cookie **flavour** which is set to a base64 string decoding to the string **strawberry**.

As the page said that it likes chocolate, setting the cookie to base64 equivalent of the string **chocolate** gives us the flag.

```
csictf{1ick_twi5t_dunk}
```

Alternatively we can also use this **one liner**
```
python -c "from base64 import b64encode;import os; os.system('curl '+'http://chall.csivit.com:30243/ '+'--cookie flavour='+b64encode(b'chocolate').decode())"
```


