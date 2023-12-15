---
layout: page
title: Web Servers Guide
permalink: /networking/web-servers/guide
---

# Web Servers

## How to Use

Use this guide to reinforce mental models, compare to another system component
like an application server, or to reference use cases. Refer to a tool specific
quick reference for help with using a specific tool.

### When You'll Use

Web servers are important when it's time to deploy a service that needs to be
reachable by a client communicating over the public internet. It's more
simple (and less work) to make the service public, but the following use cases
wouldn't be unachievable:

- **Secure Access**: Limiting which clients have access to the service's resources.

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