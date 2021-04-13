import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_breach_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 34) == "NORMAL")
    self.assertTrue(typewise_alert.classify_temperature_breach('HIGH_ACTIVE_COOLING',90) == "TOO_HIGH")
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -10) == "TOO_LOW")
    
  def test_improper_input(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('liquid_coolant', 36)== "Improper Input")
    self.assertTrue(typewise_alert.classify_temperature_breach('', None)== "Improper Input")
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', None)== "Improper Input")
    
  def test_check_and_alert(self):
    self.assertTrue(typewise_alert.check_and_alert('console',{'coolingType':'PASSIVE_COOLING'},70)== True)
    self.assertTrue(typewise_alert.check_and_alert('email',{'coolingType':'PASSIVE_COOLING'},70)== True)
    self.assertTrue(typewise_alert.check_and_alert('pdf',{'coolingType':'PASSIVE_COOLING'},70)== 'Improper Input')
    self.assertTrue(typewise_alert.check_and_alert(' ',{'coolingType':'PASSIVE_COOLING'},70)== 'Improper Input')

if __name__ == '__main__':
  unittest.main()
