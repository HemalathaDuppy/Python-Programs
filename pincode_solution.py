import re

def extract_pincode(address):
    pattern = r"\b[1-9][0-9]{2}\s?[0-9]{3}\b"
    
    match = re.search(pattern, address)

    if match:
        print(match.group().replace(" ", ""))  # Remove space if present
    else:
        print("-1")

# Sample Test Cases:
#Test Case 1:
address1 = "Flat No. 12B, Green Heights, Mumbai-400076, India"
extract_pincode(address1)
#Test case 2:
address2= "Block 21, MG Road, Kolkata 700 001"
extract_pincode(address2)
#Test case 3:
address3= "Some random text with no pin" 
extract_pincode(address3)
#Test case 4:
address4= "A random number 999123456789 in text" 
extract_pincode(address4)
#Test case 5: 
address5= "PINs: 500081, 110092, 400076" 
extract_pincode(address5)
     