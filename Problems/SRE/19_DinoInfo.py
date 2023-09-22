'''
Given the above two data sets, print a list of bipedal dinosaur _names_, sorted
by speed.

speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
where g = 9.8 m/s^2 (gravitational constant)
'''
import math


# NAME, LEG_LENGTH, DIET
dataset1 = [
    ("Hadrosaurus", 1.2, "herbivore"),
    ("Struthiomimus", 0.92, "omnivore"),
    ("Velociraptor", 1.0, "carnivore"),
    ("Euoplocephalus", 1.6, "herbivore"),
    ("Stegosaurus", 1.40, "herbivore"),
    ("Tyrannosaurus Rex", 2.5, "carnivore"),
    ("Pythonicus", 2.7, "stringivore"),
    ("Nonexistus", 3.4, "fastfoodivore"),
]

# NAME, STRIDE_LENGTH, STANCE
dataset2 = [
    ("Euoplocephalus", 1.87, "quadrupedal"),
    ("Stegosaurus", 1.90, "quadrupedal"),
    ("Tyrannosaurus Rex", 5.76, "bipedal"),
    ("Ultrasarus", 1.23, "bipedal"),
    ("Hadrosaurus", 1.4, "bipedal"),
    ("Trogdor", 4.2, "wingaling"),
    ("Struthiomimus", 1.34, "bipedal"),
    ("Velociraptor", 2.72, "bipedal"),
]


def calc_speed(stride_len, leg_len):
    speed = ((stride_len/leg_len)-1) * math.sqrt(leg_len * 9.8)
    return round(speed, 2)


# def print_bipedal_dinosaurs(dataset1, dataset2):
#     bipedal_dino_info = {}
#
#     # This loop will add STRIDE_LENGTH, STANCE to dict
#     for dino in dataset2:
#         dino_attrs = {}
#         dino_name = dino[0]
#         dino_stride_len = dino[1]
#         dino_stance = dino[2]
#
#         if dino_stance == 'bipedal':
#             dino_attrs['stride_len'] = dino_stride_len
#             dino_attrs['stance'] = dino_stance
#
#             # Add stride_len and stance attrs to dict
#             bipedal_dino_info[dino_name] = dino_attrs
#
#     # This loop will add LEG_LENGTH to dict
#     for dino in dataset1:
#         dino_name = dino[0]
#         dino_leg_len = dino[1]
#         if dino_name in bipedal_dino_info:
#             bipedal_dino_info[dino_name]['leg_len'] = dino_leg_len
#
#     # Calculate speed and add speed attribute to dict
#     for dname, dattr in bipedal_dino_info.items():
#         if len(dattr) == 3:
#             speed = calc_speed(float(dattr['stride_len']),
#                                float(dattr['leg_len']))
#             bipedal_dino_info[dname]['speed'] = round(speed, 2)
#
#     # Print dinosaur names sorted by speed
#     speed_list = []
#     for k, v in bipedal_dino_info.items():
#         if len(v) == 4:
#             speed_list.append((k, bipedal_dino_info[k]['speed']))
#
#     for item in sorted(speed_list, key=lambda i: i[1], reverse=True):
#         dname, speed = item[0], item[1]
#         print(dname, bipedal_dino_info[dname])


def print_bipedal_dinosaurs(dataset1, dataset2):
    bipedal_dino_info = {}

    # Iterate through second dataset
    for dino in dataset2:
        name = dino[0]
        stride_len = dino[1]
        stance = dino[2]

        if stance == "bipedal":
            bipedal_dino_info[name] = {
                'stride_len': stride_len,
            }

    # Iterate through first dataset
    for dino in dataset1:
        name = dino[0]
        leg_len = dino[1]
        if name not in bipedal_dino_info:
            # If dino doesn't have stats like Nonexistus
            continue
        bipedal_dino_info[name]['leg_len'] = leg_len
        bipedal_dino_info[name]['speed'] = calc_speed(stride_len, bipedal_dino_info[name]['leg_len'])

    # Print dinosaur names sorted by speed
    speed_list = []
    for name, v in bipedal_dino_info.items():
        if len(v) == 3:
            speed_list.append((name, bipedal_dino_info[name]['speed']))

    for item in sorted(speed_list, key=lambda x: x[1], reverse=True):
        name, speed = item[0], item[1]
        print(name, bipedal_dino_info[name])


def main():
    print_bipedal_dinosaurs(dataset1, dataset2)


if __name__ == '__main__':
    main()
