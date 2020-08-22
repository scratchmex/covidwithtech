import json
import phonenumbers as pn
from phonenumbers.phonenumberutil import region_code_for_number


def get_country(data):
    # data: Twilio Request
    # country code is in mayus, e.g. MX
    country = data.get("Field_country_Value")
    if not country:
        number = data.get("UserIdentifier").replace("whatsapp:", "")
        number = pn.parse(number)
        country = region_code_for_number(number)

    return country
