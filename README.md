# Chat GPT FastAPI Action
Little template

## Notes
**Vercel** is shit but I f* looove it, but its python support is crap and the doc is terrible. For instance, how do I fucking host a stupid static file? Who knows

At least this shit works now.

## Headers

Headers sent by openai

```json
{
    "host": "chatgpt-action-fastapi.vercel.app",
    "content-type": "application/json",
    "x-real-ip": "23.102.140.124",
    "x-vercel-proxy-signature-ts": "1704551807",
    "forwarded": "for=23.102.140.124;host=chatgpt-action-fastapi.vercel.app;proto=https;sig=0QmVhcmVyIGJlM2Y3MDE3ZmZhMDQ2ZTE1ZjI2MmVhMWRhOWM3OGZiNzQ3YWEyZGQ5MDQ3MWIwMDIxM2EwYTliZWQwMTEwZWY=;exp=1704551807",
    "x-vercel-deployment-url": "chatgpt-action-fastapi-nxo7nyha0-francescosaveriozuppichini.vercel.app",
    "x-vercel-forwarded-for": "23.102.140.124",
    "x-forwarded-for": "23.102.140.124",
    "x-forwarded-host": "chatgpt-action-fastapi.vercel.app",
    "openai-ephemeral-user-id": "19b15bb5-f9cf-58eb-8f06-840d3dbd661b",
    "x-vercel-ip-latitude": "29.4227",
    "openai-gpt-id": "g-o1WpV3uQ0",
    "x-vercel-proxied-for": "23.102.140.124",
    "openai-conversation-id": "20ef780d-d805-5be6-8796-7a1737c38796",
    "x-vercel-proxy-signature": "Bearer be3f7017ffa046e15f262ea1da9c78fb747aa2dd90471b00213a0a9bed0110ef",
    "x-vercel-id": "cle1::d7jxv-1704551507000-4d96ae5b07e7",
    "traceparent": "00-0000000000000000e9320c8d028b014e-f65a2ea6f18033c0-01",
    "user-agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
    "x-vercel-ip-longitude": "-98.4927",
    "accept": "*/*",
    "x-forwarded-proto": "https",
    "x-datadog-sampling-priority": "1",
    "x-vercel-ip-country": "US",
    "x-vercel-ip-country-region": "TX",
    "x-datadog-trace-id": "16803506959445328206",
    "accept-encoding": "gzip, deflate",
    "x-datadog-tags": "_dd.p.dm=-1",
    "x-vercel-ip-timezone": "America/Chicago",
    "x-vercel-ip-city": "San%20Antonio",
    "x-datadog-parent-id": "17751552175785391040",
    "tracestate": "dd=s:1;t.dm:-1"
}

```
`openai-ephemeral-user-id'` seems to be the current user id
`openai-conversation-id` seems to be the current chat id
