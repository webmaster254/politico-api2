import time

P_PARTIES = []
PARTY_COUNT = 1


class PParties:
    """ Methods to model party information """
    def __init__(self, party_reg_data):
        self.party_reg_data = party_reg_data

    def create_party(self):
        """ Validate, append, return custom message """
        global P_PARTIES, PARTY_COUNT
        msg = None
        party_already_present = False
        for each_party in P_PARTIES:
            if each_party["name"] == self.party_reg_data["name"]:
                party_already_present = True
        if party_already_present:
            msg = {
                "status": "Failed",
                "error": "Party already exists"
            }
        else:
            time_stamp = time.localtime(time.time())
            self.party_reg_data["id"] = PARTY_COUNT
            PARTY_COUNT += 1
            self.party_reg_data["registered on"] = time.asctime(time_stamp)
            P_PARTIES.append(self.party_reg_data)
            msg = {
                "Status": "Success",
                "data": [{
                    "id": self.party_reg_data["id"],
                    "name": self.party_reg_data["name"]
                    }]
                }
        return msg

    def check_for_expected_keys(self, list_of_expected_keys):
        """ (dict, list) -> bool
            Checks for dict-key equality
        """
        return list(self.party_reg_data.keys()) == list_of_expected_keys

    def check_for_any_empty_fields(self):
        """ (dict) -> bool
            checks for empty strings
        """
        msg = None
        if "" in self.party_reg_data.values():
            msg = False
        elif (
                self.party_reg_data["name"].isspace() or
                self.party_reg_data["hqAddress"].isspace() or
                self.party_reg_data["logoUrl"].isspace() or
                self.party_reg_data["Party members"] < 1
        ):
            msg = False
        else:
            msg = True
        return msg

    def check_for_expected_value_types(self):
        """ Check for expected value types"""
        msg = None
        if (
                isinstance(self.party_reg_data["name"], str) and
                isinstance(self.party_reg_data["hqAddress"], str) and
                isinstance(self.party_reg_data["logoUrl"], str) and
                isinstance(self.party_reg_data["Party members"], int)
        ):
            msg = True
        else:
            msg = False
        return msg

    def get_all_parties():
        """ get all parties """
        global P_PARTIES
        msg = None

        if P_PARTIES == []:
            msg = {
                "status": "200",
                "data": "The Party list is empty"
            }

        else:
            msg = {
                "status": "200",
                "data": P_PARTIES
            }

        return msg

    def check_id_exists(pid):
        """ Check that provided id """
        global P_PARTIES

        if pid in [party["id"] for party in P_PARTIES]:
            return True
        else:
            return False
    
    def fetch_a_party(pid):
        """ Fetch a political party by ID"""
        global P_PARTIES
        return [party for party in P_PARTIES if party['id'] == pid]

    def check_for_valid_party_name(name):
        """ check name is not empty string, space & longer than 1 charaster"""
        if isinstance(name, str):
            return len(name.strip()) < 1
        else:
            return False

    def edit_party(user_data, pid):
        """ Edit apolitical party """
        global P_PARTIES
        for party in P_PARTIES:
            if party['id'] == pid:
                party['name'] = user_data["name"]

        return [{"id": pid, "name": user_data["name"]}]