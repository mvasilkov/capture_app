from pathlib import Path

from mitmproxy import http
from mitmproxy.addonmanager import Loader


class Capture:
    def load(self, loader: Loader):
        self.path: Path = Path('Captured Files').resolve()
        self.path.mkdir(parents=True, exist_ok=True)

    def should_capture(self, flow: http.HTTPFlow):
        raise NotImplementedError()

    def response(self, flow: http.HTTPFlow):
        saveas = self.should_capture(flow)
        if saveas is not None:
            print('Capture', flow.request.url, 'as', saveas)

            if saveas.endswith('.html'):
                contents = f'Content-Location: {flow.request.url}\n\n'.encode('utf-8')
                contents += flow.response.get_content(strict=True)
            else:
                contents = flow.response.get_content(strict=True)

            (self.path / saveas).write_bytes(contents)
