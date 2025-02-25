import tornado.ioloop
import tornado.web
from logs.logging_setup import setup_logging
from app.handler.alive import AliveHandler
from app.handler.read_tpv import TpvHandler
from app.handler.home import MainHandler
from app.handler.transactions_by_data import TransactionsByDataHandler

PORT = 8888

logger = setup_logging("Home", "logs/run.log")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/alive", AliveHandler),
        (r"/read_tpv", TpvHandler),
        (r"/transactions_by_data", TransactionsByDataHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    logger.info(f"Aplicação iniciada na porta {PORT}... http://localhost:{PORT}")
    tornado.ioloop.IOLoop.current().start()