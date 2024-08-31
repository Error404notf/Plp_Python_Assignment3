def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

def main():
    # Prompt the user to enter the original price and discount percentage
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price
        print(f"The final price after applying the discount is: {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the main function
if __name__ == "__main__":
    main()
