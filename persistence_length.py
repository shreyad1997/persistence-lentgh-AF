import sys
import operator
import pdb
import numpy as np
import math
import matplotlib.pyplot as plt

atom = {
    "id" : '0',
    "type" : '0',
    "mol" : '0',
    "x" : '0.1000',
    "y" : '0.1000',
    "z" : '0.1000',
    "ix" : '0.1000',
    "iy" : '0.1000',
    "iz" : '0.1000'
}



tangents = []
coms = []

'''
This is to "unit vectorize" a vector
CHECKED
'''
def unit_vector(vector):

    if len(vector) != 3:
        print("Error converting vector to a unit vector")
    else:
        scalar_value = math.sqrt(vector[0] * vector[0] +
                                 vector[1] * vector[1] +
                                 vector[2] * vector[2])

        vector[0] = vector[0]/scalar_value
        vector[1] = vector[1]/scalar_value
        vector[2] = vector[2]/scalar_value

        return vector


'''
CHECKED
'''
def dot_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        print("Error converting vector to a unit vector")
    else:
        product = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2]
        return product

'''
This is to get the batch sorted
CHECKED
'''
def get_sorted_batch(file_name):
    flag = 0;
    atom_number = 0;
    atom_list = [];

    file_handler = open('config.custom')
    #file_handler = open(file_name)


    for line in file_handler:
        list = line.split()
        if (list[0] == 'ITEM:'):
            if (flag == 4):
                print("Batch iterated")
                break;
            flag = flag + 1
        elif (flag == 4):
            atom["id"] = int(list[0])
            atom["type"] = int(list[1])
            atom["mol"] = int(list[2])
            atom["x"] = float(list[3])
            atom["y"] = float(list[4])
            atom["z"] = float(list[5])
            atom["ix"] = float(list[6])
            atom["iy"] = float(list[7])
            atom["iz"] = float(list[8])
            atom_list.append(dict(atom));
            atom_number = atom_number + 1;

    new_list = sorted(atom_list, key = lambda k:k['id'])

    return new_list


'''
This is to get the center of mass for
the 56-atom batch

@return com_coordinates is a list that contains
                        the coordinates of the
                        center of mass
CHECKED
'''
def com_56(batch):
    com_coordinates = [0.0, 0.0, 0.0];
    for i in range(len(batch)):
        atom = batch[i]
        com_coordinates[0] += atom['x']
        com_coordinates[1] += atom['y']
        com_coordinates[2] += atom['z']

    com_coordinates[0] /= 56
    com_coordinates[1] /= 56
    com_coordinates[2] /= 56

    return com_coordinates

'''
'''
def populate_coms(whole_batch):

    start = 0;
    finish = 55;

    while (finish < len(whole_batch)):


        start += 56;
        finish += 56;





'''
This is to get the center of mass for
a cluster of three batches

@return the equivalent center of mass
CHECKED
'''
def com_trimer(whole_batch, start):
    s = start;
    f = start + 55;

    com1 = com_56(whole_batch[s:f]);

    s += 56;
    f += 56;

    com2 = com_56(whole_batch[s:f]);

    s += 56;
    f += 56;

    com3 = com_56(whole_batch[s:f]);

    com_eq = [0, 0, 0]

    com_eq[0] = (com1[0] + com2[0] + com3[0])/3;
    com_eq[1] = (com1[1] + com2[1] + com3[1])/3;
    com_eq[2] = (com1[2] + com2[2] + com3[2])/3;

    return com_eq;


'''
To get a set of tangents and store it in a
global list
'''
def populate_tangents(whole_batch):

    global tangents
    size = len(whole_batch)

    i = 0;
    temp_count = 1;
    while i < size:
        first_point = com_trimer(whole_batch, i)
        second_point = com_trimer(whole_batch, i + 168)
        i += 168

        tangent_vector_s = [0, 0, 0]

        tangent_vector_s[0] = second_point[0] - first_point[0]
        tangent_vector_s[1] = second_point[1] - first_point[1]
        tangent_vector_s[2] = second_point[2] - first_point[2]

        tangents.append(unit_vector(tangent_vector_s))

def main():

    #file_name = input("Enter the file name (or file path): ")
    batch = get_sorted_batch("config.custom");
    #populate_tangents(batch)
    global tangents

    #for atom in batch:
    #    print(atom)
    populate_coms(batch)
    populate_tangents(batch)

    print(len(tangents))

    #s = int(input("Enter 's': "))
    ln = []

    a = 0
    for s in tangents:
        denom = np.log(dot_product(tangents[0], s))
        ln.append(denom)
        a += 1

    s = list(range(1, len(ln) + 1))

    #print(ln)
    plt.plot(s, ln, color='blue', marker='o')#, markerfacecolor='blue', markersize=12)

    plt.show()


if __name__ == "__main__":
    main()
