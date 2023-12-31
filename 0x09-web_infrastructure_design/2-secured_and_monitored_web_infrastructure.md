<h1>Description</h1>
This is a 3-server web infrastructure that is secured, monitored, and serves encrypted traffic.

<h2>Specifics About This Infrastructure</h2>
<b>What are firewalls for?</b>
The firewalls are for protecting the network (web servers, anyway) from unwanted and unauthorized users by acting as an intermediary between the internal network and the external network and blocking the incoming traffic matching the aforementioned criteria.

<b>Why is the traffic served over HTTPS?</b>
HTTPS is a secure version of the HTTP protocol, which is the protocol used to transfer data over the web. When a website uses HTTPS, it means that all communication between the web server and the client’s web browser is encrypted and secure. HTTPS primarily assists in protecting the privacy of users’ personal information and preventing attackers from intercepting and altering the data that is transmitted between the server and the client

<b>The purpose of the SSL certificate.</b>
The SSL certificate is for encrypting the traffic between the web servers and the external network to prevent man-in-the-middle attacks (MITM) and network sniffers from sniffing the traffic which could expose valuable information. The SSL certs ensure privacy, integrity, and identification.

<b>What monitoring is used for?</b>
The monitoring clients are for monitoring the servers and the external network. They analyse the performance and operations of the servers, measure the overall health, and alert the administrators if the servers are not performing as expected. The monitoring tool observes the servers and provides key metrics about the servers' operations to the administrators. It automatically tests the accessibility of the servers, measures response time, and alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues.

<h2>Issues With This Infrastructure</h2>
<b>Why terminating SSL at the load balancer level is an issue?</b>
Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted.

<b>Why having only one MySQL server capable of accepting writes is an issue?</b>
Having one MySQL server is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.

<b>Why having servers with all the same components (database, web server and application server) might be a problem</b>
Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup such as this is not easily scalable.
