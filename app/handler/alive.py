import tornado.web
from datetime import datetime
from logs.logging_setup import setup_logging

logger = setup_logging("AliveHandler", "logs/alive.log")

class AliveHandler(tornado.web.RequestHandler):
    async def get(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Requisição recebida em {current_time}. A aplicação está funcionando.")

        try:
            self.set_status(200)
            self.write({"status": "OK"})
        except Exception as e:
            logger.error(f"Erro ao responder à requisição: {e}")
            self.set_status(500)
            self.write({"error": "Erro ao responder à requisição"})