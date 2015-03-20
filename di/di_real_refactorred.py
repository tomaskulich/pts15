
class IncidentChecker:
    """
        warning: this is just a pseudocode. Neither DB driver nor urllib are used exactly this way.
    """
    
    def __init__(self, user_id_provider, ilp, idp):
        self.uip = user_id_provider
        self.ilp = ilp
        self.idp = idp

    def can_perform_action(self, username, action):
        """
            todo is this ok?
        """
        user_id = self.uip(username)
        incidents = self.ilp(user_id)
        last_incidents = [i for i in incidents if newer_than_month(i)]
        if len(last_incidents) > 5:
            return False
        full_incidents = []
        for incident in last_incidents:
            full_incidents.add(self.idp(incident['id']))
        for incident in full_incidents:
            if incident['action'] == action:
                return False
        return True











    #def get_user_by_name(self, name):
    #    return self.conn.execute('SELECT * FROM user_table WHERE name = %s' %name)


        roles = self.conn.execute('''SELECT * FROM user_table JOIN role_table ON
            (user_table.user_id = role_table.user_id) WHERE user_name = %s''', user_name)

        stronger = self.conn.execute('''SELECT * FROM role_order''') 




    ...

