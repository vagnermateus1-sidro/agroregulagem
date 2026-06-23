"""
Servidor local para instalar o VM AgroRegulagem PRO no iPhone.
Execute este arquivo e siga as instruções na tela.
"""
import http.server, socketserver, socket, os, threading, webbrowser

PORTA = 8080
PASTA = os.path.dirname(os.path.abspath(__file__))

def ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"
    finally:
        s.close()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PASTA, **kwargs)
    def log_message(self, fmt, *args):
        pass  # silenciar logs

os.chdir(PASTA)
ip = ip_local()
url = f"http://{ip}:{PORTA}"

print("=" * 52)
print("  VM AgroRegulagem PRO — Servidor Local")
print("=" * 52)
print()
print(f"  Acesse no iPhone (Safari):")
print()
print(f"  >>> {url} <<<")
print()
print("  Passo a passo no iPhone:")
print("  1. Conecte o iPhone na mesma rede WiFi do PC")
print("  2. Abra o Safari (obrigatório — não Chrome)")
print(f"  3. Digite o endereço: {url}")
print("  4. Toque no ícone de compartilhar (quadrado com seta)")
print("  5. Toque em 'Adicionar à Tela de Início'")
print("  6. Confirme e pronto — ícone na tela inicial!")
print()
print("  Pressione CTRL+C para encerrar o servidor.")
print("=" * 52)

with socketserver.TCPServer(("", PORTA), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor encerrado.")
