import des
import string
import random
import statistics
import matplotlib.pyplot as plt


# function to generate a random string of a specific length
def gen_random_string(length):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for x in range(length))

# function to flip specific number of bits in the given string
def perturb_string(strng, num):
    strng = strng[::-1]
    perturbedString = ""
    for i in range(len(strng)):
        if i < num: 
            perturbedString += chr(ord(strng[i]) ^ 8)
        else: 
            perturbedString += strng[i]
    perturbedString = perturbedString[::-1]
    return perturbedString

# calculate the hamming distance between two bit strings
def calc_hamming_distance(string1, string2):
    if len(string1) != len(string2):
        raise ValueError("Strings must be of equal length")
    hamming_distance = 0
    for i in range(len(string1)):
        hamming_distance += (string1[i] != string2[i])
    return hamming_distance

# Code to generate and save the required plot
def generate_plot(HD, title, initial_distances):

    HD_RoundWise = [initial_distances,] + list(zip(*HD))
    fig = plt.figure(figsize=(10, 8))                           
    plt.boxplot(HD_RoundWise, positions = [l for l in range(0,17)])
    medians= [ statistics.median(HD_current) for HD_current in HD_RoundWise]
    plt.plot(medians)
    fig.suptitle("Plot for " + title, fontsize = 14, fontweight = 'bold')
    plt.xlabel('Round Number')
    plt.ylabel('Hamming distance')
    fig.savefig(f'{title}.png')
    plt.show()

# function to perform the experiments with desired configuration changes in parts
def perform_experiment(change_plain_text, change_key, change_hamming_distance, experiment_name):

    HD = []
    initial_distances = []

    print("Demonstrating Avalanche Effect with " + experiment_name, end = "\n\n")

    print("Plain Text", "Key\t", "Cypher Text", end = "\n\n", sep = "\t\t")

    for i in range(1, 6):

        initial_distance = change_plain_text + i * change_hamming_distance # Hamming distance between plain text

        # Perform DES to generate original cypher
        key = gen_random_string(8)
        plainText = gen_random_string(8)
        d = des.des(key = bytes(key, 'ascii'))
        cypherText = d.encrypt(bytes(plainText,'ascii'))
        original_intermediate_cyphers = d.intermediate_cyphers

        print(plainText, key, cypherText, sep = "\t\t")

        # Perform DES to generate perturbed cypher
        perturbedText = perturb_string(plainText, initial_distance)
        perturbedKey = perturb_string(key, change_key)
        d= des.des(key = bytes(perturbedKey, 'ascii'))
        perturbedCypherText = d.encrypt(bytes(perturbedText, 'ascii'))
        perturbed_intermediate_cyphers = d.intermediate_cyphers

        print(perturbedText, perturbedKey, perturbedCypherText, end = "\n\n", sep = "\t\t")

        hd = [calc_hamming_distance(str1,str2) for str1,str2 in zip(original_intermediate_cyphers, perturbed_intermediate_cyphers)]
        HD.append(hd)
        initial_distances.append(initial_distance)
        
    generate_plot(HD, experiment_name, initial_distances)

    print("\n\n\n\n")




if __name__=="__main__":

    # Assignment - Part 1 --> for five different plain texts and their purturbation
    perform_experiment(change_plain_text = 1, change_key = 0, change_hamming_distance = 0, experiment_name = "Five Different Plain Texts and their Purturbation")

    # Assignment - Part 2 --> five different Hamming distances between plain texts
    perform_experiment(change_plain_text = 0, change_key = 0, change_hamming_distance = 1, experiment_name = "Five Different Hamming Distances between Plain Texts")

    # Assignment - Part 3 --> for five different keys and their purturbation
    perform_experiment(change_plain_text = 0, change_key = 1, change_hamming_distance = 0, experiment_name = "Five Different Keys and their Purturbation")