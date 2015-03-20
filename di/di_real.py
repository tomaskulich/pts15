
class IncidentChecker:
    """
        warning: this is just a pseudocode. Neither DB driver nor urllib are used exactly this way.
    """
    
    def __init__(self, host, port, user, pwd, incident_list_url, incident_details_url):
        self.conn = DB.createConnection(host, port, user, pwd)
        self.incident_list_url = incident_list_url
        self.incident_detaiuls_url = incident_details_url


    def can_perform_action(self, username, action):
        """
            todo is this ok?
        """
        user_id = self.conn.execute('SELECT id FROM user_table WHERE name = %s' % username)
        incidents = json.load(urllib.request.urlopen("%s/%s"%(self.incident_list_url, user_id)).read().decode('utf-8'))
        last_incidents = [i for i in incidents if newer_than_month(i)]
        if len(last_incidents) > 5:
            return False
        full_incidents = []
        for incident in last_incidents:
            full_incidents.add(json.load(urllib.request.urlopen("%s/%s"%
                (self.incident_details_url, incident['id'])).read().decode('utf-8')))
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

