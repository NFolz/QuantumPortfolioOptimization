input_data = {}

def removeDoubles(input_data):
    new_input_data = {}
    
    for stock, val in input_data.items():
        search = stock + "," + stock
        
        # Add to the new dictionary only if the concatenated key doesn't exist
        if search not in new_input_data:
            new_input_data[stock] = val

    return new_input_data

# Example usage
input_data = removeDoubles(input_data)
