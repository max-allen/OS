---
layout: page
title: Client Retry Strategies
permalink: /networking/client-retries/
---

# Client Retry Strategies

Common retry strategies for handling network failures:

- **Immediate Retry**: client immediately retries requests up to some threshold
  for failures.

- **Fixed Intervals**: client waits a fixed amount of time between each request.

- **Incremental Intervals**: client waits briefly to initially retry, then incrementally increases the time for subsequent retries.

- **Exponential Backoff**: client exponentially increases time between
  subsequent requests by some backoff factor.

- **Cancel (No Retry)**: client cancels the request. This is expected when
  retries have reached a failure threshold or the server response implies
  subsequent requests will be unsuccessful (e.g. `401 Unauthorized`).

Retrying a request makes sense if it's idempotent or the failure is possibly
transient.

Consider the scenario where a request has failed and returns `503 Service Unavailable`: perhaps the web server was unable to forward the request
because the application was restarting, and nothing was listening on the port.

