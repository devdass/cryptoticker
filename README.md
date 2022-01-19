# cryptoticker
This is a project I had started in 2017 during the Bitcoin bull run. It pulls live price data from the Poloniex cryptocurrency exchange and displays them on a LED matrix display using a Raspberry Pi.

After some interest from traders I contemplated making a product out of it, but became busy with other things and would like to work on more exciting projects. The code is now publically available.

This project utilises the fantastic work of @hzeller:
https://github.com/hzeller/rpi-rgb-led-matrix

It is a work-in-progress.

The script is able to pull down live prices of cryptocurrency pairs on the poloniex exchange and have them scroll across the LED matrix display, just like that of a wall street stock ticker.

Note: I created this before people started saying "sats", hence the micro btc denominations.

![scrolling crypto pairs](https://github.com/devdass/cryptoticker/blob/main/4ticker.gif)

The code is also able to be altered to pull down RSS feeds from news sites and have headlines displayed at specific intervals.

![scrolling news feeds](https://github.com/devdass/cryptoticker/blob/main/news.gif)

To do:
- Improve readability
- Create webpage control panel
- Offer compatibility with other exchanges
