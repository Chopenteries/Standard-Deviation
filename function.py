import math


def run():

    samples = input("Input your samples: \n").split()
    for n in range(0, len(samples)):
        samples[n] = int(samples[n])
    print(samples)

    try_again = True
    while try_again is True:
        print("\nPopulation Standard Deviation: "
              "\nThe population standard deviation,"
              "the standard definition of σ, is used when an entire population can be measured, and is the square "
              "root of "
              "the variance of a given data set. "
              " In cases where every member of a population can be sampled,"
              " the following equation can be used to find the standard deviation of the entire population:")
        print()
        print("Sample Standard Deviation: "
              "\nIn many cases, it is not possible to sample every member within a population, requiring that the "
              "above "
              "equation be modified so that the standard deviation can be measured through a random sample of the "
              "population being studied. A common estimator for σ is the sample standard deviation, typically denoted "
              "by "
              "s.")
        print("\nWhich data type do you want?")
        data_type = input("A: Population Standard Deviation(n) \nB: Sample Standard Deviation(n-1) \n")

        if data_type == "A" or data_type == "a":
            print(find_population_sd(samples))
            break

        if data_type == "B" or data_type == "b":
            print(find_sample_sd(samples))
            break

        else:
            try_again = True
            print("Wrong answer!! try again!!")


def find_population_sd(x):
    sum_of_powered_x_minus_x_bar = 0
    for n in range(0, len(x)):
        this_x = int(x[n])
        x_bar = sum(x) / len(x)
        power_of_x_minus_x_bar = (this_x - x_bar) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / len(x)
    answer = math.sqrt(v)
    return answer


def find_sample_sd(x):
    sum_of_powered_x_minus_x_bar = 0
    for n in range(0, len(x)):
        this_x = int(x[n])
        x_bar = sum(x) / len(x)
        power_of_x_minus_x_bar = (this_x - x_bar) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / (len(x) - 1)
    answer = math.sqrt(v)
    return answer
