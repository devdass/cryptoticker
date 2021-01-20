# cryptoticker
This is a project I had done in December 2017 during the Bitcoin bull run. It pulls live price data from the Poloniex cryptocurrency exchange and displays them on a LED matrix display using a Raspberry Pi.

People have expressed interested in me developing this into a product they could purchase which I contemplated but became busy with other things and would like to work on more exciting projects. The code is now publically available. I have also made some modifications and cut it down quite a bit in an effort to make it more understandable - I have not uploaded these changes yet, but I will soon.


My work utilises the fantastic work of @hzeller:
https://github.com/hzeller/rpi-rgb-led-matrix

This is a work-in-progress.

So far using my publicly available code, I am able to pull down live prices of multiple cryptocurrency pairs and have them scroll across the LED matrix display, just like that of wall street stock tickers.

![scrolling crypto pairs](https://github.com/devdass/cryptoticker/blob/main/4ticker.gif)

The code is also able to be alterd to pull down RSS feeds from news sites and have headlines displayed at specific intervals.

![scrolling news feeds](https://github.com/devdass/cryptoticker/blob/main/news.gif)

To do:
- Write documentation
- Make code more readable
- Develop webpage control panel
- Offer other exchange data
