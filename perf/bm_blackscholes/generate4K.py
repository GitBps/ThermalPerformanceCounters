import random

def generate_blackscholes_input(filename, num_options=4096):
    with open(filename, 'w') as f:
        for _ in range(num_options):
            sptprice = random.uniform(10.0, 100.0)     # Stock price
            strike = random.uniform(10.0, 100.0)      # Strike price
            rate = random.uniform(0.01, 0.1)          # Risk-free rate
            volatility = random.uniform(0.1, 0.5)     # Volatility
            time = random.uniform(0.1, 5.0)           # Time to maturity
            option_price = random.uniform(1.0, 20.0)  # Random option price (dummy for input)
            divyield = random.uniform(0.01, 0.05)     # Dividend yield
            error = random.uniform(0.001, 0.01)       # Error (dummy for input)
            option_type = random.choice(['C', 'P'])   # 'C' for CALL, 'P' for PUT
            
            # Write to file in the specified format
            f.write(f"{sptprice:.6f} {strike:.6f} {rate:.6f} {volatility:.6f} {time:.6f} {option_price:.6f} {option_type} {divyield:.6f} {error:.6f}\n")

# Generate a file named in_4K.txt with 4096 options
generate_blackscholes_input("in_4K.txt")
