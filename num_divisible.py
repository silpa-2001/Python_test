def divisible(start, end, divisor):
    divisible_no = [n for n in range(start, end + 1) if n % divisor == 0]
    return divisible_no
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor: "))
divisible_no = divisible(start, end, divisor)
if(divisible):
    print(f"Numbers divisible by {divisor} between {start} and {end} are : {divisible_no}")
else:
    print(f"There are no numbers divisible by {divisor} between {start} and {end}.")
