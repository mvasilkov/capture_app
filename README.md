capture_app
===

Capture files from network

Requirements
---

- [mitmproxy](https://mitmproxy.org)

Usage
---

```sh
mitmdump -p 2019 -q -s capture/capture_html_parts.py --anticache
chrome --proxy-server=localhost:2019
```

**Scanning**

```javascript
const VK_RIGHT = 0x27

setInterval(function () {
    document.dispatchEvent(new KeyboardEvent('keydown', { keyCode: VK_RIGHT }))
}, 2019)
```
