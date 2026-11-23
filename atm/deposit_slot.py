class DepositSlot:
    def is_envelope_received(self):
        response = input("Have you inserted the deposit envelope? (yes/no): ")

        if response.lower() == 'yes':
            return True
        return False