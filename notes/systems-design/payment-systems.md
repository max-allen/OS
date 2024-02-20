---
layout: page
title: Payment Systems
permalink: /systems-design/payment-systems
---

# Payment Systems

##### Sections
1. [Description](#description)
2. [Components](#components)
3. [Key Topics](#key-topics)

## Description

A payment system can mean different things to different people. To some, it
could mean a [Digital
Wallet](https://www.investopedia.com/terms/d/digital-wallet.asp), like Venmo or
Apple Pay. Others may think of a backend system that executes payments like
Stripe or Paypal. Consequently, this classification is a loose descriptor
that only coveys the general nature of the problem; specific requirements are
necessary to get a clear picture of system responsibilities.

A common thread among payment systems is **money movement** – the need to
facilitate the transfer of funds between at least two parties.

## Components

### Payment Service

Operative component. Processes user initiated or recurring payment events.
Updates data stores and communicates with complementary services.

May perform risk / compliance checks in conjunction with external service
provider. Initiates payment execution through payment service provider (PSP).

### Payment Service Provider (PSP)

External service that moves money between accounts. Stripe and Square are
industry examples.

### Card Schemes

Process credit card operations. Visa, Discover, MasterCard, etc. are examples.

### Ledger

Keeps record of all payment transactions. Important for bookkeeping and post
payment analysis. Provides end-to-end traceability and ensures consistency
throughout payment cycle. Likely implements [Double-entry accounting](https://en.wikipedia.org/wiki/Double-entry_bookkeeping).

### Wallet

Keeps merchant account balances. Useful for payment systems where payment is not
immediately moved between accounts of the transacting parties. May or may not be
present to the extent payment system leverages functionality of PSP.

## Key Topics

### Idempotency

Idempotent operations is a primary concern when designing payment systems. It's
imperative to guarantee that a customer won't be charged more than once,
irrespective of external factors like network errors or service provider
downtime. Operations should be repeated/retried as necessary, producing the same
result without any effects on the system. This implies **exactly-once
delivery:** each payment must be executed _at least_ once, and can be executed
_at most_ once.

#### Retry Strategies

The at-least once guarantee can be met with **retries**. A retry strategy should
consider the length of time to wait before retrying, and when the request should
be canceled with no further attempts. See [[client-retry-strategies]] for
example strategies.

#### Idempotency Key

The at-most guarantee can bet met with **idempotency key usage**. For web/mobile client-server communication,
[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) is commonly
used in request headers as an idempotency key (`<idempotency-key: key_value>`);
this is recommended by Stripe and Paypal. Alternatively, e-commerce websites
commonly use the id of shopping carts right before checkout.

### Internal Service Communication
Internal services can communicate **synchronously** or **asynchronously**:

#### Synchronous Communication (HTTP)

Synchronous communication via HTTP is the simpler design choice and may
work well at sufficiently small scale. As scale increases, long request response
cycles dependent on many services pose challenges:

- Performance subject to any service in the chain
- Poor failure isolation (if service fails, client wont receive response)
- Tight coupling. Sender needs to know recipient
- Hard to scale in the event of traffic increase

#### Asynchronous Communication (Message Queue)

Asynchronous communication via a Message Queue allows for an event-driven
strategy where payment events can be published as messages to the Queue, and
subsequently consumed by multiple subscribing services. This is particularly
well suited for payment systems, as a payment event may need to trigger
operations performed by supporting services like ledger, wallet, or analytics.

This approach trades complexity for scalability and failure resistance.

###  Handling Payment Failures

Payment failures can be handled with client retries as discussed in the section
on [idempotency](#retry-strategies). Two Queues can be utilized: one for
retryable failures (retry queue), and the other for canceled requests (dead
letter queue). The payment service will route failures to each queue in
accordance with the desired retry strategy.

The Dead letter queue is useful for debugging problematic events.

- Reliability / Fault Tolerance
- Handling Payment Processing Delays

- Security
- Reconciliation
- Executing Payments (PSP Integration)


### Industry Examples:
- [Uber](https://www.youtube.com/watch?v=5TD8m7w1xE0)
- [Shopify](https://help.shopify.com/en/manual/payments/shopify-payments)
- [Stripe](https://stripe.com/docs/api)


