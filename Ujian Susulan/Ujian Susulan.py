
## Soal 1

sentence = str(input("Masukan Sentence : "))
single_sentence = "Many"

def find_short(s):
    s_list = s.split(" ")
    minimum = 0
    
    for index, word in enumerate(s_list):
        if len(word) < minimum:
            minimum = len(word)
        elif index == 0:
            minimum = len(word)
            
    
    return minimum

print(find_short(sentence))

print(find_short(single_sentence))

# Soal 2 

number = str(input("number: "))

def persistence(n):
    n_str = str(n)
    n_list = list(n_str) # ["3", "9"] => 27 => "27" => ["2", "7"] => 14 => "14" => ["1", "4"] => 4  
        
    mult_result_single_digit = False
    amount_mult = 0
    
    if len(n_list) == 1:
        return amount_mult
    
    while mult_result_single_digit == False:
        mult_result = 1 
        
        for n in n_list:
            mult_result = mult_result * int(n)
            
        amount_mult = amount_mult + 1    
        
        n_list = list(str(mult_result))
        
        if len(n_list) == 1:
            mult_result_single_digit = True
    
    return amount_mult


print(persistence(number))
# Soal 3
def multiplication_table(row, col):
    table = []
    
    for r in range(row):
        row_list = []
        
        for c in range(col):
            row_list.append((r+1) * (c+1))
            
        table.append(row_list)
            
    
    return table


print(multiplication_table(3,3))
# Soal 4
text_input = input("text: ")

def alphabet_position(text):
    c_list = list(text)
    pos_list = []
    
    for c in c_list:
        c_ascii_num = int(ord(c.capitalize())) # "A" => 65, "Z" => 90
        
        if c_ascii_num >= 65 and c_ascii_num <= 90:
            c_pos = c_ascii_num - 64
            pos_list.append(c_pos)
    
    
    return pos_list
    
print(alphabet_position(text_input))