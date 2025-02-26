import tornado.web
from logs.logging_setup import setup_logging
from db_connection import transactions_collection

logger = setup_logging("TpvHandler", "logs/read_tpv.log")

class TpvHandler(tornado.web.RequestHandler):
    async def get(self):
        try:
            tpv = sum(doc['original_amount'] for doc in transactions_collection.find())
            response = {"TPV": round(tpv, 2)}

            self.set_status(200)
            logger.info(f"TPV calculado: {response}")
            self.write(response)
        except Exception as e:
            logger.error(f"Erro ao calcular TPV: {e}")
            self.set_status(500)
            self.write({"error": "Erro ao calcular TPV"})