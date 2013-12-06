from NewsServer import cnx

class RoleList(object):
    '''
    Represents the list of roles assigned to a user_id
    '''


    def __init__(self, user_id):
        '''
        Constructor
        '''
        dog = cnx.cursor()
        dog.callproc('get_roles_by_user_id', (user_id,) )
        results = dog.fetchall()
        dog.close()
        self.roles = []
        
        if results == None:
            self.roles.append('none')
        else:
            for role in results:
                self.roles.append(role[0])