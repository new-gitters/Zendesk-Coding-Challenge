import unittest
import sys
sys.path.insert(0, '../src/')
from request import get_list_tickets,get_single_ticket,authenticate
class TestAPI(unittest.TestCase):
    def test_get_list_tickets(self):
        self.assertEqual(get_list_tickets(1)['status_code'],200)
        self.assertNotEqual(get_list_tickets(-1)['status_code'],200)

    def test_get_single_ticket(self):
        self.assertEqual(get_single_ticket('https://zccadmin.zendesk.com/api/v2/tickets/8.json')['status_code'],200)
        self.assertNotEqual(get_single_ticket('https://zccadmin.zendesk.com/api/v2/tickets/0.json')['status_code'],200)
        self.assertNotEqual(get_single_ticket('https://zccadmin.zendesk.com/api/v2/tickets/-1.json')['status_code'],200)

    def test_authenticate(self):
        self.assertEqual(authenticate('zccadmin','98d75e177bfc788af652d53886bd388ab2847e6cea5add00441490ff311ae8d5')[0],200)
        self.assertNotEqual(authenticate('none','98d75e177bfc788af652d53886bd388ab2847e6cea5add00441490ff311ae8d5')[0],200)
        self.assertNotEqual(authenticate('zccadmin','none')[0],200)


if __name__=='__main__':
    unittest.main()