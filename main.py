
CONNECTION_STRING = ""


class Item:
    def __init__(self, code, price):
        self.code = code
        self.price = price



class PostgresDatabaseInterface:
    def __init__(self, CONNECTION_STRING):
        self.ng = create_engine(CONNECTION_STRING)
        Base.metadata.bind = self.ng

    def _create_items(self, results):
        return [
            Item(code=q.code, price=q.price)
            for q in results
        ]

    def list(self, filters):
        DBSession = sessionmaker(bind=self.ng)
        session = DBSession
        query = ...

        return self._create_items(query.all())


# Usecase is considered as main business logic
# Usecase should not care about framework that is being used
# Usecase should not care about tools that are being used externally 
# In other words it should care more about data and methods of data based on bussiness needs
def item_list_usecase(repo, params):
    
    result = repo.list(params)
   
    return result


# Web framework should only convert data to needed format
# Web framework should just retrive and send data only 
@webframework.route('/items', methods=['GET'])
def items():
    repo = PostgresDatabaseInterface(CONNECTION_STRING)
    result = item_list_usecase(repo, request.args)

    return Response(
        json.dumps(result),
        mimetype='application/json',
        status=200
    )





# Web framework is external
# Web framework is not business logic
# You are not marketing django, flask or fiber!


# Databases are also considered as an external part of business
# Service that is being built is not serving database or any other technolgy
# If application is being served in postgres or mongo db user shold not be concerned
# And same for usecases! Usecases should not care about technologu that is being used for serving 




# Usecases should not communicate directly with databases or web frameworks
# It means usecases should not be decoupled with database of web framework
# 

# Developer should spend more time on business logic rather tan internal settinfs

