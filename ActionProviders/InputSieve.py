class InputSieve:

    def __init__(self, sieve_type):
        self.sieve_type = sieve_type

    def get_move(self, events):
        deciding_event = None
        for e in events:
            if e.key in self.sieve_type.keys():
                deciding_event = e
        if deciding_event:
            return self.sieve_type[deciding_event.key]
        else:
            return None
