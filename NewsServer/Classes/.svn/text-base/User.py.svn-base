from NewsServer import cnx
from NewsServer.Classes.RoleList import RoleList


class User(object):
    '''
    This class represents a row from the "user_view" database view
    '''
    
    def __init__(self, *args, **kwargs):
        '''
        Constructor - order of attributes must match database output
        '''
        
        self.user_id, self.username, self.email, self.password_hash, self.first_name, self.last_name, self.about_me, self.create_time, self.last_login, self.last_modified = args
        
        #self.user_id = args[0]
        #self.username = args[1]
        #self.email= args[2]
        #self.password_hash = args[3]
        #self.first_name = args[4]
        #self.last_name = args[5] 
        #self.about_me = args[6] 
        #self.create_time = args[7]
        #self.last_login = args[8]
        #self.last_modified = args[9]
        
        self.roles = []
        dog = cnx.cursor()
        dog.callproc("get_roles_by_user_id", (self.user_id,))
        results = dog.fetchall()
        dog.close()
        
        if results == None:
            self.roles.append('none')
        else:
            for role in results:
                self.roles.append(role[0])
    
    @classmethod
    def byEmail(cls,email):
        "Query the database by email, and return values to the constructor"
        dog = cnx.cursor()
        dog.callproc("get_user_by_email", (email,) )
        result = dog.fetchone()
        dog.close()
        return cls(*result)
    
    @classmethod
    def byId(cls,user_id):
        "Query the database by email, and return values to the constructor"
        dog = cnx.cursor()
        dog.callproc("get_user_by_id", (user_id,) )
        result = dog.fetchone()
        dog.close()
        return cls(*result)