<h1>Description</h1>
A Distributed Web Infrastructure refers to the concept of distributing the components of a website across multiple servers or devices, rather than hosting everything on a single server. This can improve the performance and reliability of a website, as well as make it more resilient to outages or attacks.

<h2>Specifics About This Infrastructure</h2>

<b>Why add a Load balancer?</b>
Load balancers are used to distribute network traffic across multiple servers. This helps to ensure that no single server becomes overwhelmed with requests, improving the overall performance and reliability of the system.

<b>What distribution algorithm your load balancer is configured with and how it works?</b></br>

The HAProxy load balancer is configured with the Round Robin distribution algorithm. Each server takes turns handling requests. The load balancer sends the first request to the first server, the second request to the second server, and so on. After each round, it starts again.It's simple and fair. All servers get a chance to handle requests equally.
Good for distributing a consistent load across servers.

<b>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</b>
The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all nodes to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an Active-Passive setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.

<b>How a database Primary-Replica (Master-Slave) cluster works.</b>
In a database primary-replica cluster, one database server is designated as the primary server and is responsible for handling read and write operations. The other database servers, known as replica servers, continuously replicate the data from the primary server, ensuring that they always have an up-to-date copy of the data.

When a client wants to read or write data, it sends a request to the primary server. The primary server handles the request and then sends the updated data to the replica servers so that they can update their copies of the data. This ensures that all of the servers in the cluster have the same data, allowing for high availability and fault tolerance.

<b>The difference between the Primary node and the Replica node in regard to the application.</b>
The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.

<h2>Issues With This Infrastructure</h2>

<b>Where are SPOF?</b>
There are multiple SPOF (Single Point Of Failure).
For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.

<b>Security issues (no firewall, no HTTPS)</b>

The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.

<b>No monitoring.</b>

We have no way of knowing the status of each server since they're not being monitored.
