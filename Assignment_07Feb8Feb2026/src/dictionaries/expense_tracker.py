
'''We can build a simple expense tracker using a dictionary:

The keys will be the expense heads (like "food", "rent", "travel").
The values will be the total amount spent under that head.
We will write two functions:

update_expenses(expense_list, expenses_dict) → updates the dictionary with new expenses.

expense_list is a list of tuples like [("food", 200), ("rent", 1000)].
expenses_dict is the dictionary where totals are stored.
print_expenses(expenses_dict) → prints the overall expenses under each head in a clean way.'''   

def update_expenses(expense_list, expenses_dict):
    if expenses_dict == None:
        expenses_dict ={}
    for ele in expense_list:
        key = ele[0]
        val = ele[1]
        if not key in expenses_dict:
            expenses_dict[key]=val             
        else:
            new_val =int(expenses_dict[key])+int(val) #int(result[key])+1
            expenses_dict[key] =new_val
        #print(expenses_dict)
             
def print_expenses( expenses_dict):
    for dict_val in expenses_dict:
        key = dict_val
        val = expenses_dict[dict_val]
        print(dict_val,":",expenses_dict[dict_val])
       