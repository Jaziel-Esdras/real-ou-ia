#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser


PROJECT_DIR = Path(__file__).resolve().parent


class GameRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIR), **kwargs)


with ThreadingHTTPServer(("127.0.0.1", 0), GameRequestHandler) as server:
    url = f"http://127.0.0.1:{server.server_port}/index.html"
    print(f"Jogo aberto em {url}\nPressione Ctrl+C para encerrar.", flush=True)
    try:
        browser_opened = webbrowser.open(url)
    except webbrowser.Error as error:
        print(f"Não foi possível abrir o navegador automaticamente: {error}", flush=True)
        browser_opened = False
    if not browser_opened:
        print(f"Abra este endereço no navegador: {url}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.", flush=True)
