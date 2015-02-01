# jne

![Screenshoot](https://dl.dropboxusercontent.com/u/18755263/Screenshot-Bandara.png)

a python script to check JNE courier for price and track your package with your airwaybill code.

just run ```python jne.py``` and you will get the clue how this thing work.


first, you need a **api_key** and **username** to use this things, or you want to do
some scrapping things? if that so, just take a look at `constant.py` on the `src` directory,
a sample scrapper script also include, take a look at `parser.py`.


# requirement

you will need,
- python 2.7.x
- requests `pip install requests`
- tabulate `pip install tabulate`
- lxml, for parsing things up. this one is conditional btw.

that's it.


# Disclaimer

I, doesnt give any warranty, doesn't take any responsibly for all.

this thing came up as I was bored on a saturday night and I try to waste some time
on something that quietly set me to braingasm.

so, here is the source code. enjoy!

or, you need me to do "something"? sure, just drop me an email then. :)


# License

```
The MIT License (MIT)

Copyright (c) 2015 Widnyana Putra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
