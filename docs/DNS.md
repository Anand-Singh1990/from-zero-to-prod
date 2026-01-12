# DNS (Domain Name Server)

DNS tells computers what to do next when they’re given a name — often by pointing to another name, and eventually to an IP address.

## Step by Step Resolution Chain

```
Browser DNS Cache
       ↓
  OS DNS Cache
       ↓
Recursive Resolver (ISP / Google / Cloudflare)
       ↓
  Root DNS Server
       ↓
   TLD Server
       ↓
Authoritative DNS Server
```

**Note:** Response is cached everywhere, hence DNS is **eventually consistent**, not strongly consistent.

## DNS Records

- **A**: Maps domain name to IPv4 address
- **CNAME**: Maps name to another name (e.g., `api.example.com` → `example.com`). When someone asks for this domain, it returns the mapped name and keeps resolving until it gets an IP.
  - **Common reasons for name → name mapping:**
    1. Load balancers & CDNs
    2. Multi-service setups
    3. Branding
- **TTL**: Defines how long the record lives in the cache at different resolution chains



## DNS vs TLS/HTTPS

- **DNS** finds the server
- **TLS/HTTPS** secures the connection
- DNS never knows or cares if your server is up 

