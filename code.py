import web
import re
import logging 

urls = ('/', 'index',
        '/r/?', 'run',)
        
        
render = web.template.render('templates/', globals={'re':re})
app = web.application(urls, globals())
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = web.database(dbn='mysql', db='test', user='root', pw='')
logger.info(db)

result = db.query("SELECT datetime", _test=True)
logger.info(result)

class index:
    def GET(self):
        args = web.input(s='')
        print(args)
        return render.index(args.s)

class run:
    def GET(self):
        args2 = web.input(r='')
        print(args2)
        return render.run(args2.r)        

if __name__ == '__main__':
    app.run()
    logger.info('Init')
