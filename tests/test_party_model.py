import unittest
from app.api.v1.models.party_model import PParties


class TestPParties(unittest.TestCase):
    """ Testscase for PoliticalParties"""
    def setUp(self):
        """ Init test variable"""
        self.test_data = PParties({
            "name": "kenya",
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg",
            "Party members": 500
        })

    def test_empty_field_check(self):
        """ Test for empty string in value field"""
        empty_str = PParties({
            "name": "",
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg",
            "Party members": 500
        })
        self.assertTrue(
            self.test_data.check_for_any_empty_fields(), msg="Should be True"
        )
        self.assertFalse(
            empty_str.check_for_any_empty_fields(), msg="Should be False"
        )

    def test_expected_value_types(self):
        """ Check value(datatypes) types of user data"""
        wrong_value_types = PParties({
            "name": 12,
            "hqAddress": "kicc,nairobi",
            "logoUrl": "/kenya.jpeg",
            "Party members": 225
        })
        self.assertTrue(
            self.test_data.check_for_expected_value_types(),
            msg="Should be True"
        )
        self.assertFalse(
            wrong_value_types.check_for_expected_value_types(),
            msg="Should be False"
        )

    def test_create_party_return_msg(self):
        """ Test a political party is created"""
        self.assertDictEqual(
            {'Status': 'Success', 'data': [{'id': 1, 'name': 'kenya'}]},
            self.test_data.create_party()
        )

    def test_creating_a_party_twice(self):
        """ Test a political pary cannot be created twice """
        self.test_data.create_party()
        self.assertDictEqual(
            self.test_data.create_party(),
            {'status': 'Failed', 'error': 'Party already exists'}
        )


if __name__ == "__main__":
    unittest.main()
