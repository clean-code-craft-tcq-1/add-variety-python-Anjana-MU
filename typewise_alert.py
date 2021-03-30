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


def classify_temperature_breach(coolingType, temperatureInC):
    if validate_input(coolingType, temperatureInC):       
        range = coolingType_limits[coolingType]
        return infer_breach(temperatureInC, range['lowerLimit'], range['upperLimit'])
    else:
        return 'Improper Input'

def validate_input(coolingType, temperatureInC):
    return (coolingType.upper() in coolingType_limits.keys() and isinstance(temperatureInC, numbers.Number))    
        
    
def check_and_alert(alertTarget, breachType):
    if not breachType == "NORMAL":
        alertTarget_type[alertTarget](breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')

def make_email(recepient):
    def send_to_email(breachType):
        print(f'To: {recepient}')
        print(f'Hello {recepient}, {breachType}')
    return send_to_email
    
alertTarget_type = {
        'email': make_email("a.b@c.com"),
        'controller' : send_to_controller
        }
