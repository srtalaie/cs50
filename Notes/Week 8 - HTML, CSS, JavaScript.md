## Routers
- Computers/Servers connected via Wired/Wireless connections that allow data to flow between systems anywhere
- Multiple paths this data can be routed to its desired destination

## TCP/IP
- **TCP/IP** - protocols that let computers know how to move data from one point to another
  - **IP** - Internet Protocol, how the computers know how to address each other. IP dictates that every computer on the internet has a unique address (#.#.#.#). Each number is 0-255 or 8 bits or 32 bits total. This only allows for 4 billion addresses so there is a newer version which allows for more (**ipv4** vs **ipv6**).
  - **TCP** - Transfer Control Protocol. Set of conventions that distinguish one type of service over the internet from another. These come in the form of unique numbers (ex/ 80 = HTTP, 443 = HTTPS). TCP also allows you to fragment media into multiple pieces so if a **Router** drops a packet (or does not receive a piece of fragmented info) the destination computer knows what is missing and can ask for the missing data to be sent again.

## DNS
- **DNS** - Domain Name System, a collection of servers on the internet that convert **domain names** into **IP addresses**. Acts as a phonebook that ties an **IP address** to an easily readable/recognizable string, i.e. a **Domain Name**. Inside these servers is contains Key/Value pairs in the form of domain names and associated IP addresses.

## HTTP
- **HTTP** - Hypertext Transfer Protocol. The set of rules for transferring files such as text, images, sound, video and other multimedia files over the web.
  - https :// www . example . com / folder / file.html
    - **https** - protocol your computer should use when accessing content at that address
    - **www** - host name
    - **example** - domain name
    - **com** - Top Level Domain name
    - **folder** - folder sitting under the parent directory of the server hosting the domain name
    - **file.html** - the content in that folder that is being accessed at the address
  - **HTTP** uses english verbs to tell the computer what to do with the information that is being sent or is being hosted on the server ex/ GET or POST
- [Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## curl

```
$ curl -I https://www.harvard.edu/
```

- The output of running the above is all of the headers when visiting the above site.

## Search
```
GET /search?q=cats
```
- "?" is convention to pass user input. Google itself supports "q" as query. So the above is a google search for "cats"

## HTML
- **HyperText Markup Language (HTML)** - languages in which web pages themselves are written. Not a programming language itself. 2 important features:
	- **Tags** - 
	- **Attributes** - 