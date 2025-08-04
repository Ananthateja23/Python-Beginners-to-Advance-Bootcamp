from atm_machine_main.atm_main import AtmMachine
from atm_machine_main.db import Database

db = Database()

atm = AtmMachine()

if __name__ == "__main__":
    db.connection()
    atm.create_pin()
    atm.check_balance()