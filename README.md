# Checkout

[![CI](https://github.com/anshumaan-10/checkout/actions/workflows/build-push.yaml/badge.svg)](https://github.com/anshumaan-10/checkout/actions/workflows/build-push.yaml)
[![Docker Hub](https://img.shields.io/docker/v/anshumaan10/checkout?label=Docker%20Hub)](https://hub.docker.com/r/anshumaan10/checkout)

Part of the [k8s-security-lab](https://github.com/anshumaan-10/k8s-security-lab) — a hands-on Kubernetes security research environment.

---

## What Is This

A background polling worker that continuously fetches transactions from the [payment-api](https://github.com/anshumaan-10/payment-api) service. Demonstrates internal cluster service-to-service communication.

---

## Behaviour

- Polls `$PAYMENT_API_URL` every 5 seconds
- Logs transaction count on success
- Exits with code `1` after 3 consecutive failures (Kubernetes will restart it)

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `PAYMENT_API_URL` | `http://payment-api:8080/transactions` | URL to poll |

---

## Quick Start

```bash
# Requires payment-api to be running
docker compose up  # from k8s-security-lab root
```

---

## Security Properties

| Property | Value |
|---|---|
| Run as root | No — `uid=1000` (appuser) |
| Privilege escalation | Disabled |
| Read-only filesystem | Yes |
| Image | Multi-stage — no build tools in final image |
