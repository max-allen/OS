---
layout: page
title: Web Servers Guide
permalink: /networking/web-servers/guide
---

# Web Servers

Web servers handle HTTP requests. As the name implies, they can be used to
serve content, but they have a variety of other use cases such as load
balancing, caching, and SSL termination.

## How to Use

Use this guide to reinforce mental models, compare to another system component
like an application server, or to reference use cases. Refer to a tool specific
quick reference for help with using a specific tool.

### When You'll Use

- **Publicly Accessible Resources (Deploying):** Web servers are most relevant
  when it's time to deploy a service that needs to be reachable by a client
  communicating over the public internet.

### Use Cases

- **Serving Content**: Serving content is the operative use case of web servers
  traditionally. Content may be static (e.g HTML/images stored on a host) or dynamic (e.g. JSON response from a web application framework).

- **Restricting Access**: Limiting which clients have access to the service's resources.

- **Load Balancing**: Distributing request traffic across separate instances of
the service.

### Examples
<!-- TODO: add usage statistics image -->
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)

### Resources 📚

- [web server (wiki)](https://en.wikipedia.org/wiki/Web_server)

- [proxy vs reverse proxy (stack overflow)](https://stackoverflow.com/questions/224664/whats-the-difference-between-a-proxy-server-and-a-reverse-proxy-server/366212#366212)
  - Good descriptions of proxy types with simple, illustrative examples
    detailing use cases. Lists popular modern examples.

- [web server usage statistics](https://w3techs.com/technologies/overview/web_server)