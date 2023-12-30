<h1>Description</h1>

A simple web infrastructure that hosts a website, reachable via www.foobar.com. 
There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.

<h2>Specifics About This Infrastructure</h2>

<b>What a server is.</b>
A server is a computer hardware or software that provides services to other computers, usually called clients.

<b>The role of the domain name.</b>
To provide a human-friendly alias for an IP Address. The IP address and domain name alias is mapped in the Domain Name System (DNS). For example, the domain name www.Google.com is easier to recognize and remember than 191.193.174.192. 

<b>The type of DNS record www is in www.foobar.com.</b>
www.foobar.com uses an A record. This can be checked by running dig www.foobar.com.
Note: the results might be different but for the infrastructure in this design, an A record is used.
Address Mapping record (A Record)—also known as a DNS host record, stores a hostname and its corresponding IPv4 address.

<b>The role of the web server.</b>
The web server is software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error message.

<b>The role of the application server.</b>
To install, operate, and host applications and associated services for end users, IT services, and organizations and facilitate the hosting and delivery of high-end consumer or business applications

<b>The role of the database.</b>
To maintain a collection of organized information that can easily be accessed, managed, and updated

<b>What is the server using to communicate with the computer of the user requesting the website?</b>
Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

<h1>Issues With This Infrastructure</h1>
There are multiple SPOF (Single Point Of Failure) in this infrastructure.
For example, if the MySQL database server is down, the entire site would be down.

<b>Downtime when maintenance needed.</b>
When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.

<b>Cannot scale if there's too much incoming traffic.</b>
It would be hard to scale this infrastructure because one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of requests.
