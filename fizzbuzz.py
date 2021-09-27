def main(first, last):
    thirds_increment = 0
    fifths_increment = 0
    starting_num = first
    fizzbuzz_range = last - first
    for i in range(fizzbuzz_range):
        thirds_increment = thirds_increment + 3
        fifths_increment = fifths_increment + 5
        if starting_num == thirds_increment:
            print("Fizz")

        




