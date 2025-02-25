import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
                    <html>
                        <body>
                            <h1>Teste Databuild</h1>
                            <p><a href="/alive">/alive</a></p>
                            <p><a href="/read_tpv">/read_tpv</a></p>
                            <p><a href="/transactions_by_data">/transactionsbydata</a></p>
                        </body>
                    </html>''')