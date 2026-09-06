indian = ["samosa","daal","naan"]
Chinese = ["egg role","pot sticker","Fried rice"]
italian = ["Pizza","Pasta","risotto"]
dish = input("Enter a dish name:")

if dish in indian:
    print("indian")
elif dish in italian:
    print("italian")
elif dish in Chinese:
    print("Chinese")
else:
    print("dish not found")