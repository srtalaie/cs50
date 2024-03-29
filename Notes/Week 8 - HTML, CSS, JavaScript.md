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
- HTTP Server is just a program that responds to **requests** with **responses**

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
	- **Tags** - building blocks of html, keywords on a web page that define how your web browser must format and display your web page
	- **Attributes** - provide additional information about elements

## Document Object Model (DOM)
- **Document Object Model (DOM)** - A programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.

## Meta
- Key/Value pairs utilized for SEO

## CSS
- **Cascading Style Sheets (CSS)** - Used to style web pages like fonts, colors, etc.

## Frameworks
- A set of resources and tools for software developers to build and manage web applications, web services and websites, as well as to develop application programming interfaces (APIs)

## JavaScript
- Programming language, supports conditionals, loops, variables, etc.
- Built for the web

## Greet
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<script>

			function greet()
			{
				let name = document.querySelector('#name').value;
				alert(`Hello, ${name}`);
			}

		</script>
		<title>
			hello, title
		</title>
	</head>
	<body>
		<form onsubmit="greet(); return false;">
			<input autocomplete="off" autofocus placeholder="NAME" type="text" id="name">
			<button type="submit">Greet</button>
		</form>
	</body>
</html>
```

Cleaner Version:
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<title>
			hello, title
		</title>
	</head>
	<body>
		<form>
			<input autocomplete="off" autofocus placeholder="NAME" type="text" id="name">
			<button type="submit">Greet</button>
		</form>
		<script>
			document.querySelector('form').addEventListener('submit', function(event){
				let name = document.querySelector('#name').value;
				alert(`hello, ${name}`);
				event.preventDefault();
			});
		</script>
	</body>
</html>
```
- Order of operations loads the script before the html, so we are forced to add the script to the bottom of the code. Or you can do the following with a special event listener:
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<script>
			document.addEventListener('DOMContentLoaded', function(){
				document.querySelector('form').addEventListener('submit', function(event){
					let name = document.querySelector('#name').value;
					alert(`hello, ${name}`);
					event.preventDefault();
				});				
			});
		</script>
		<title>
			hello, title
		</title>
	</head>
	<body>
		<form>
			<input autocomplete="off" autofocus placeholder="NAME" type="text" id="name">
			<button type="submit">Greet</button>
		</form>
	</body>
</html>
```

- Including the js from outside the html file:

greet.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<script src="hello.js"></script>
		<title>
			hello, title
		</title>
	</head>
	<body>
		<form>
			<input autocomplete="off" autofocus placeholder="NAME" type="text" id="name">
			<button type="submit">Greet</button>
		</form>
	</body>
</html>
```
hello.js
```
document.addEventListener('DOMContentLoaded', function(){
	document.querySelector('form').addEventListener('submit', function(event){
		let name = document.querySelector('#name').value;
		alert(`hello, ${name}`);
		event.preventDefault();
	});				
});
```
