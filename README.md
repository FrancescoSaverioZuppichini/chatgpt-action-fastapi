# Chat GPT FastAPI Action
Little template

## Notes
**Vercel** is shit, its python support is crap and the doc is terrible. For instance, how do I fucking host a stupid static file? Who knows

At least this shit works now.

## Headers

Headers sent by openai

```python
Headers({'host': 'chatgpt-action-fastapi.vercel.app', 'content-type': 'application/json', 'x-real-ip': '93.34.232.117', 'x-vercel-proxied-for': '93.34.232.117', 'x-vercel-deployment-url': 'chatgpt-action-fastapi-nxo7nyha0-francescosaveriozuppichini.vercel.app', 'cache-control': 'no-cache', 'x-vercel-ip-latitude': '45.4317', 'x-vercel-forwarded-for': '93.34.232.117', 'forwarded': 'for=93.34.232.117;host=chatgpt-action-fastapi.vercel.app;proto=https;sig=0QmVhcmVyIGE5MTk5N2QwMWMyZGI1OWNkMjIxNTNlZjAyZmUzNmJlMzlkNGY1YTMyNDkxOThkOGVmNjI2NjA1ZmI0ZGFjYjE=;exp=1704551861', 'x-vercel-id': 'fra1::jldk7-1704551561785-8f8c9e289726', 'x-forwarded-for': '93.34.232.117', 'postman-token': 'f6419571-3a55-431b-b967-e2b01f1de7f0', 'x-vercel-ip-longitude': '10.9859', 'accept': '*/*', 'x-forwarded-host': 'chatgpt-action-fastapi.vercel.app', 'x-vercel-proxy-signature': 'Bearer a91997d01c2db59cd22153ef02fe36be39d4f5a3249198d8ef626605fb4dacb1', 'x-vercel-ip-country': 'IT', 'x-vercel-ip-country-region': '34', 'x-vercel-ip-timezone': 'Europe/Rome', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'PostmanRuntime/7.36.0', 'content-length': '21', 'x-vercel-ip-city': 'Verona', 'x-forwarded-proto': 'https', 'x-vercel-proxy-signature-ts': '1704551861'})
```