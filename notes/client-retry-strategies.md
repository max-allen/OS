---
layout: page
title: Client Retry Strategies
permalink: /client-retry-strategies/
---

# Client Retry Strategies

Common retry strategies for handling network failures:

- **Immediate Retry**: client immediately resends a request.

- **Fixed Intervals**: wait a fixed amount of time between the time of the
  failed payment and a new retry attempt.

- **Incremental Intervals**: client waits for a short time for the first retry,
  and then incrementally increases the time for subsequent retries.

- **Exponential Backoff**: double the waiting time between retries after each
  failed retry. For example, when a request fails for the first time, we retry
  after 1 second; if it fails a second time, we wait 2 seconds before the next
  retry; if it fails a third time, we wait 4 seconds before another retry.

- **Cancel**: the client can cancel the request. This is a common practice when
  the failure is permanent or repeated requests are unlikely to be successful.

---
#### References 📚
- [System Design Interview Vol. 2](https://www.amazon.com/System-Design-Interview-Insiders-Guide/dp/1736049119)

