import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
  def test_breach_type_normal(self):
    breachType = typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 34)
    self.assertTrue(breachType == "NORMAL")
    typewise_alert.check_and_alert('email',breachType)
    
  def test_breach_type_too_high(self):
    breachType = typewise_alert.classify_temperature_breach('HIGH_ACTIVE_COOLING', 46)
    self.assertTrue(breachType == "TOO_HIGH")
    typewise_alert.check_and_alert('controller',breachType)  
    
  def test_improper_input(self):
    breachType = typewise_alert.classify_temperature_breach('liquid_coolant', 36)
    self.assertTrue(breachType == "Improper Input")
    typewise_alert.check_and_alert('controller',breachType)
    
  def test_improper_value(self):
    breachType = typewise_alert.classify_temperature_breach('PASSIVE_COOLING', None)
    self.assertTrue(breachType == "Improper Input")
    typewise_alert.check_and_alert('email',breachType)

if __name__ == '__main__':
  unittest.main()
