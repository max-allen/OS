---
layout: page
title: Proxy Servers Guide
permalink: /networking/proxy-servers/guide
---

# Proxy Servers

## How to Use

### When This Matters

Proxies should be relevant when it's time to deploy a service that needs to be
reachable by a client communicating over the public internet. It's more
simple (and less work) to make the service public, but the following use cases
wouldn't be unachievable:

- **Secure Access**: Limiting which clients have access to the service's resources.

- **Load Balancing**: Distributing request traffic across separate instances of
the service.

### Types

### Examples
<!-- TODO: add usage statistics image -->
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)

### Resources 📚

- [proxy server (wiki)](https://en.wikipedia.org/wiki/Proxy_server)

  - Short, high level overview. Start here.

- [proxy vs reverse proxy (stack overflow)](https://stackoverflow.com/questions/224664/whats-the-difference-between-a-proxy-server-and-a-reverse-proxy-server/366212#366212)
  - Good descriptions of proxy types with simple, illustrative examples
    detailing use cases. Lists popular modern examples.

- [web server usage statistics](https://w3techs.com/technologies/overview/web_server)