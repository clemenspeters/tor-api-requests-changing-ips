# Web scraping with tor and different IPs

This is just an example how to make api requests from changing IP addresses.<br>
To use it just customize the script to make your own requests.<br>
This is just a technical prove of concept and may only be used in any illigal context.

## Sources / Credits: 
- https://boredhacking.com/tor-webscraping-proxy/
- https://medium.com/@jasonrigden/using-tor-with-the-python-request-library-79015b2606cb


## Requirements
1. Install Tor on your computer, for macs this can be accomplished
using homebrew `brew install tor`. You can then run it constantly 
in the background using the command `brew services start tor` or 
run it manually using the command `tor`.

2. Make sure you have firefox installed on your computer, this will be required
if you want to use the same selenium code above. You can use other browsers 
but the **my_proxy** method will need to change slightly

3. Install stem and requests Python libraries using the command
`pip install stem requests`

4. You will also need to update your `torrc` and restart Tor so that you can make
requests to the Tor controller. On a mac you can find your `torrc` file 
at `/usr/local/etc/tor/torrc.sample`. Rename it to torrc by doing 
`mv /usr/local/etc/tor/torrc.sample /usr/local/etc/tor/torrc` and 
then uncomment the following lines 
(I will copy the full torrc at the bottom of this post)

```
ControlPort 9051
CookieAuthentication 1
```

## Mac installation commands
```console
brew install tor
brew services start tor
pip install stem requests
mv /usr/local/etc/tor/torrc.sample /usr/local/etc/tor/torrc
vim /usr/local/etc/tor/torrc
```