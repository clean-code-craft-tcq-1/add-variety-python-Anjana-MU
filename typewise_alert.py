import numbers

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  elif value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

coolingType_limits = {
        'PASSIVE_COOLING' : {'lowerLimit':0 , 'upperLimit' : 35},
        'HIGH_ACTIVE_COOLING' : {'lowerLimit' : 0 , 'upperLimit' : 45},
        'MED_ACTIVE_COOLING' : {'lowerLimit' : 0 , 'upperLimit' : 40}}

breachType_email_recepient = {
        'TOO_LOW': {'recepient': "low.b@c.com"},
        'TOO_HIGH': {'recepient': "High.b@c.com"}}


def classify_temperature_breach(coolingType, temperatureInC):
    if validate_input(coolingType, temperatureInC):       
        range = coolingType_limits[coolingType]
        return infer_breach(temperatureInC, range['lowerLimit'], range['upperLimit'])
    else:
        return 'Improper Input'

def validate_input(coolingType, temperatureInC):
    return (coolingType.upper() in coolingType_limits.keys() and isinstance(temperatureInC, numbers.Number))    
        
    
def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    if not breachType == "NORMAL" and validate_alertTarget(alertTarget, breachType):
       return(alertTarget_type[alertTarget](breachType))
    else:
        return 'Improper Input'
       
def validate_alertTarget(alertTarget, breachType):
  if alertTarget in alertTarget_type.keys() and breachType != 'Improper Input':
    return True
  return False


def send_to_console(breachType):
  print(f'BreachType is:, {breachType}')
  return True
  
def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return True   

def send_to_email(breachType):
   print(f"Hello: {breachType_email_recepient[breachType]['recepient']}\n Breach is: {breachType}")
   return True
    
alertTarget_type = {
        'email': send_to_email,
        'controller' : send_to_controller,
        'console' : send_to_console
        }
