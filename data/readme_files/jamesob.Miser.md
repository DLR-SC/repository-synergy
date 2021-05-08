## Get rich: be Miserly

Miser is a Python library that can be used for writing scripts that'll help you
project costs and figure out how to accumulate money. It's in unstable alpha.

## Example

Here's a simple usage:

```python
from miser import *
from miser.scheduling import *
from miser.views import *
import random

m = Miser("test", 
          initialBalance = 3e3)

g = Goal(name = "bankity bank bank",
         amount = 20e3, # $16,000
         by = Date(2012, 9, 1)) # by Aug. 1, 2012

m.addGoal(g)

m.addTransactions(
    # Expenses
    Expense(name = "MATH322 tuition",
            amount = 1.3e3,
            on = Date(2012, 5, 29)),
                           
    Expense(name = "netflix",
            amount = 7.,
            on = MonthlyRecurring(15)), # 15th day of the month
                            
    Expense(name = "lunch",
            amount = 6.,
            on = DailyRecurring()),
                             
    Expense(name = "dinner",
            amount = 5.,
            on = WeeklyRecurring((SA, SU, TU, WE, FR))),
                              
    Expense(name = "breakfast",
            amount = 3.,
            on = DailyRecurring()),
                              
    Expense(name = "rent+utils",
            amount = 800.,
            on = MonthlyRecurring(29)),
                                 
    # Income
    Income(name = "job",
           amount = 2e3,
           on = MonthlyRecurring((7, 22))),
)

def unforeseen():
  """Return a random value in some range to simulate unforeseen expenses."""
  return random.gauss(300., 100.)

m.addTransaction(
    Expense(name = "unforeseen",
            amount = unforeseen,
            on = MonthlyRecurring(1))
)

def investment(principal, interest):
  """A generator that simulates an investment and interest on it, compounded
  monthly."""
  while True:
    principal *= (1 + interest)
    yield principal

m.addTransaction(
    Income(name = "Investment",
           amount = investment(1000, 0.07),
           on = MonthlyRecurring(1))
)

def summary(fromdt, todt):
  args = (m, fromdt, todt)
  GoalPrinter(*args)
  Histogram(*args)

if __name__ == '__main__':
  summary(Date(2012, 2, 1), Date(2012, 8, 15))
```

which produces

```
test: 2012-02-01 00:00:00 to 2012-08-15 00:00:00
Total saved: 28455.56

Goals:
Goal 'bankity bank bank' met with 13900.71 to spare!


Profile of expenses:

 rent+utils      -4800.00           ---------------------------------------------
 unforeseen      -1868.69           -----------------
 MATH322 tuition -1300.00           ------------
 lunch           -1182.00           -----------
 dinner          -705.00            ------
 breakfast       -591.00            -----
 netflix         -49.00
```

