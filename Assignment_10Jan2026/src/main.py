import subprocess
import add
import multiply
import next_number
import print_base_numbers
import tables
import log_baseN_num
import squareroot


print()
print()
print('Addition of two nos in the given Base("0123456","11","23"): '+add.add_two_numbers("0123456","11","23"))
print()
print()
print('Multiplication of two nos. in the given Base("01234","14","12"): '+add.add_two_numbers("01234","14","12"))
print()
print()
print('Next Number of the given base ("0123456789AB","BB"): '+next_number.next_number("0123456789AB","BB"))
print()
print()
tables.tables("0123456789AB")
print()
print()
print(f'{"*"*60}')
print("Print n digit numbers of the given base(base:12 3 digit numbers)")
print(f'{"*"*60}')
print_base_numbers.print_ndigit_no_in_base("0123456789AB",3)

Log_BaseN_Num.calbaselog(12,1000000)
SquareRoot.calsquareroot_guess(64)
print()
print()




