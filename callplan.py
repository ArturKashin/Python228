from customer import Customer

class CustomerFree(Customer):
    def record_call(self, call_type, minutes):
        if call_type == "Г" and minutes > 10:
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        super().record_call(call_type, minutes - bonus_minutes)


class CustomerTwice(Customer):
    def record_call(self, call_type, minutes):
        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0

        super().record_call(call_type, cheap_minutes / 2 + expensive_minutes * 2)
