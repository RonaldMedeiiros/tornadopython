import tornado.web
from datetime import datetime
from logs.logging_setup import setup_logging
from db_connection import transactions_collection

# Configuração de logging
logger = setup_logging("TransactionsByDataHandler", "logs/transactions_by_data.log")

class TransactionsByDataHandler(tornado.web.RequestHandler):
    async def get(self):
        try:
            initial_datetime = self.get_argument('initial_datetime')
            final_datetime = self.get_argument('final_datetime')
            page = int(self.get_argument('page'))
            per_page = int(self.get_argument('per_page'))

            initial_datetime = datetime.strptime(initial_datetime, '%d/%m/%Y %H:%M:%S')
            final_datetime = datetime.strptime(final_datetime, '%d/%m/%Y %H:%M:%S')

            cursor = transactions_collection.find({
                'datahora_salvamento_dt': {
                    '$gte': initial_datetime,
                    '$lte': final_datetime
                }
            }).skip((page - 1) * per_page).limit(per_page)

            data = [{
                '_id': str(doc['_id']),
                'amount': doc['amount'],
                'original_amount': doc['original_amount'],
                'fees': doc['fees'],
                'datahora_salvamento_dt': doc['datahora_salvamento_dt'].strftime('%d/%m/%Y %H:%M:%S'),
                'datahora_salvamento_timestamp': doc['datahora_salvamento_timestamp'],
                'created_at_dt': doc['created_at_dt'].strftime('%d/%m/%Y %H:%M:%S'),
                'updated_at_dt': doc['updated_at_dt'].strftime('%d/%m/%Y %H:%M:%S')
            } for doc in cursor]

            total_items = transactions_collection.count_documents({
                'datahora_salvamento_dt': {
                    '$gte': initial_datetime,
                    '$lte': final_datetime
                }
            })
            total_pages = (total_items // per_page) + 1

            response = {
                'data': data,
                'actual_page': page,
                'total_pages': total_pages,
                'total_items': total_items
            }

            self.write(response)
        except Exception as e:
            logger.error(f"Erro ao processar a requisição: {e}")
            self.set_status(500)
            self.write({"error": "Erro ao processar a requisição"})