import numpy as np


def load():
    # data copied from the csv file
    list = [
        2013, "Centennial High School", 1224, 591, 572, 558,
        2014, "Centennial High School", 1224, 599, 592, 598,
        2015, "Centennial High School", 1224, 558, 585, 598,
        2016, "Centennial High School", 1224, 625, 555, 600,
        2017, "Centennial High School", 1224, 611, 617, 582,
        2018, "Centennial High School", 1224, 485, 540, 582,
        2019, "Centennial High School", 1224, 463, 481, 556,
        2020, "Centennial High School", 1224, 455, 436, 437,
        2013, "Robert Thirsk School", 1679, 472, 346, 0,
        2014, "Robert Thirsk School", 1679, 444, 452, 341,
        2015, "Robert Thirsk School", 1679, 419, 411, 463,
        2016, "Robert Thirsk School", 1679, 345, 396, 436,
        2017, "Robert Thirsk School", 1679, 433, 374, 450,
        2018, "Robert Thirsk School", 1679, 398, 423, 391,
        2019, "Robert Thirsk School", 1679, 355, 430, 455,
        2020, "Robert Thirsk School", 1679, 360, 352, 437,
        2013, "Louise Dean School", 9626, 45, 57, 52,
        2014, "Louise Dean School", 9626, 40, 49, 55,
        2015, "Louise Dean School", 9626, 29, 36, 68,
        2016, "Louise Dean School", 9626, 16, 47, 56,
        2017, "Louise Dean School", 9626, 15, 48, 58,
        2018, "Louise Dean School", 9626, 23, 25, 58,
        2019, "Louise Dean School", 9626, 13, 23, 52,
        2020, "Louise Dean School", 9626, 12, 21, 34,
        2013, "Queen Elizabeth High School", 9806, 160, 176, 189,
        2014, "Queen Elizabeth High School", 9806, 151, 137, 173,
        2015, "Queen Elizabeth High School", 9806, 137, 115, 106,
        2016, "Queen Elizabeth High School", 9806, 155, 93, 137,
        2017, "Queen Elizabeth High School", 9806, 115, 123, 106,
        2018, "Queen Elizabeth High School", 9806, 150, 83, 120,
        2019, "Queen Elizabeth High School", 9806, 146, 146, 127,
        2020, "Queen Elizabeth High School", 9806, 137, 143, 142,
        2013, "Forest Lawn High School", 9813, 426, 483, 567,
        2014, "Forest Lawn High School", 9813, 430, 404, 572,
        2015, "Forest Lawn High School", 9813, 373, 403, 532,
        2016, "Forest Lawn High School", 9813, 431, 384, 567,
        2017, "Forest Lawn High School", 9813, 395, 378, 531,
        2018, "Forest Lawn High School", 9813, 395, 402, 527,
        2019, "Forest Lawn High School", 9813, 383, 397, 441,
        2020, "Forest Lawn High School", 9813, 378, 361, 438,
        2013, "Crescent Heights High School", 9815, 620, 584, 585,
        2014, "Crescent Heights High School", 9815, 662, 611, 602,
        2015, "Crescent Heights High School", 9815, 659, 643, 583,
        2016, "Crescent Heights High School", 9815, 440, 514, 659,
        2017, "Crescent Heights High School", 9815, 408, 388, 529,
        2018, "Crescent Heights High School", 9815, 568, 426, 510,
        2019, "Crescent Heights High School", 9815, 556, 615, 530,
        2020, "Crescent Heights High School", 9815, 565, 555, 629,
        2013, "Western Canada High School", 9816, 658, 631, 632,
        2014, "Western Canada High School", 9816, 618, 639, 605,
        2015, "Western Canada High School", 9816, 624, 610, 594,
        2016, "Western Canada High School", 9816, 682, 571, 630,
        2017, "Western Canada High School", 9816, 798, 665, 636,
        2018, "Western Canada High School", 9816, 716, 688, 651,
        2019, "Western Canada High School", 9816, 723, 724, 798,
        2020, "Western Canada High School", 9816, 690, 727, 734,
        2013, "Central Memorial High School", 9823, 289, 280, 311,
        2014, "Central Memorial High School", 9823, 323, 370, 395,
        2015, "Central Memorial High School", 9823, 271, 227, 316,
        2016, "Central Memorial High School", 9823, 183, 210, 230,
        2017, "Central Memorial High School", 9823, 355, 368, 491,
        2018, "Central Memorial High School", 9823, 387, 388, 419,
        2019, "Central Memorial High School", 9823, 391, 391, 409,
        2020, "Central Memorial High School", 9823, 543, 401, 459,
        2013, "James Fowler High School", 9825, 496, 465, 528,
        2014, "James Fowler High School", 9825, 422, 437, 524,
        2015, "James Fowler High School", 9825, 564, 383, 455,
        2016, "James Fowler High School", 9825, 197, 237, 459,
        2017, "James Fowler High School", 9825, 215, 193, 330,
        2018, "James Fowler High School", 9825, 242, 204, 254,
        2019, "James Fowler High School", 9825, 251, 234, 322,
        2020, "James Fowler High School", 9825, 290, 234, 315,
        2013, "Ernest Manning High School", 9826, 523, 467, 517,
        2014, "Ernest Manning High School", 9826, 522, 549, 529,
        2015, "Ernest Manning High School", 9826, 565, 530, 543,
        2016, "Ernest Manning High School", 9826, 581, 583, 546,
        2017, "Ernest Manning High School", 9826, 607, 557, 555,
        2018, "Ernest Manning High School", 9826, 685, 576, 535,
        2019, "Ernest Manning High School", 9826, 674, 692, 629,
        2020, "Ernest Manning High School", 9826, 491, 662, 680,
        2013, "William Aberhart High School", 9829, 487, 413, 457,
        2014, "William Aberhart High School", 9829, 537, 502, 416,
        2015, "William Aberhart High School", 9829, 469, 491, 499,
        2016, "William Aberhart High School", 9829, 460, 438, 499,
        2017, "William Aberhart High School", 9829, 491, 439, 423,
        2018, "William Aberhart High School", 9829, 437, 473, 428,
        2019, "William Aberhart High School", 9829, 476, 447, 507,
        2020, "William Aberhart High School", 9829, 420, 465, 434,
        2013, "National Sport School", 9830, 29, 29, 45,
        2014, "National Sport School", 9830, 36, 44, 44,
        2015, "National Sport School", 9830, 48, 37, 43,
        2016, "National Sport School", 9830, 41, 46, 48,
        2017, "National Sport School", 9830, 45, 50, 56,
        2018, "National Sport School", 9830, 38, 45, 57,
        2019, "National Sport School", 9830, 61, 56, 69,
        2020, "National Sport School", 9830, 34, 59, 64,
        2013, "Henry Wise Wood High School", 9836, 399, 361, 380,
        2014, "Henry Wise Wood High School", 9836, 362, 371, 354,
        2015, "Henry Wise Wood High School", 9836, 361, 337, 373,
        2016, "Henry Wise Wood High School", 9836, 341, 367, 377,
        2017, "Henry Wise Wood High School", 9836, 422, 338, 390,
        2018, "Henry Wise Wood High School", 9836, 417, 391, 398,
        2019, "Henry Wise Wood High School", 9836, 458, 434, 424,
        2020, "Henry Wise Wood High School", 9836, 532, 449, 431,
        2013, "Bowness High School", 9847, 210, 225, 359,
        2014, "Bowness High School", 9847, 219, 200, 222,
        2015, "Bowness High School", 9847, 215, 209, 212,
        2016, "Bowness High School", 9847, 233, 207, 221,
        2017, "Bowness High School", 9847, 249, 241, 232,
        2018, "Bowness High School", 9847, 386, 238, 249,
        2019, "Bowness High School", 9847, 391, 381, 254,
        2020, "Bowness High School", 9847, 402, 382, 364,
        2013, "Lord Beaverbrook High School", 9850, 657, 566, 501,
        2014, "Lord Beaverbrook High School", 9850, 569, 619, 562,
        2015, "Lord Beaverbrook High School", 9850, 578, 489, 590,
        2016, "Lord Beaverbrook High School", 9850, 535, 546, 543,
        2017, "Lord Beaverbrook High School", 9850, 583, 506, 534,
        2018, "Lord Beaverbrook High School", 9850, 229, 250, 495,
        2019, "Lord Beaverbrook High School", 9850, 241, 245, 299,
        2020, "Lord Beaverbrook High School", 9850, 482, 251, 293,
        2013, "Jack James High School", 9856, 163, 146, 228,
        2014, "Jack James High School", 9856, 131, 164, 208,
        2015, "Jack James High School", 9856, 116, 126, 201,
        2016, "Jack James High School", 9856, 74, 95, 179,
        2017, "Jack James High School", 9856, 127, 127, 191,
        2018, "Jack James High School", 9856, 81, 112, 135,
        2019, "Jack James High School", 9856, 102, 77, 146,
        2020, "Jack James High School", 9856, 128, 102, 144,
        2013, "Sir Winston Churchill High School", 9857, 587, 611, 648,
        2014, "Sir Winston Churchill High School", 9857, 604, 641, 720,
        2015, "Sir Winston Churchill High School", 9857, 726, 626, 651,
        2016, "Sir Winston Churchill High School", 9857, 691, 740, 680,
        2017, "Sir Winston Churchill High School", 9857, 706, 680, 763,
        2018, "Sir Winston Churchill High School", 9857, 703, 705, 744,
        2019, "Sir Winston Churchill High School", 9857, 749, 677, 744,
        2020, "Sir Winston Churchill High School", 9857, 739, 746, 709,
        2013, "Dr. E. P. Scarlett High School", 9858, 514, 577, 522,
        2014, "Dr. E. P. Scarlett High School", 9858, 549, 541, 581,
        2015, "Dr. E. P. Scarlett High School", 9858, 515, 523, 529,
        2016, "Dr. E. P. Scarlett High School", 9858, 556, 528, 568,
        2017, "Dr. E. P. Scarlett High School", 9858, 546, 580, 549,
        2018, "Dr. E. P. Scarlett High School", 9858, 533, 496, 580,
        2019, "Dr. E. P. Scarlett High School", 9858, 488, 514, 503,
        2020, "Dr. E. P. Scarlett High School", 9858, 540, 463, 503,
        2013, "John G Diefenbaker High School", 9860, 435, 364, 509,
        2014, "John G Diefenbaker High School", 9860, 438, 431, 459,
        2015, "John G Diefenbaker High School", 9860, 461, 406, 494,
        2016, "John G Diefenbaker High School", 9860, 420, 456, 511,
        2017, "John G Diefenbaker High School", 9860, 459, 418, 517,
        2018, "John G Diefenbaker High School", 9860, 443, 438, 460,
        2019, "John G Diefenbaker High School", 9860, 474, 449, 531,
        2020, "John G Diefenbaker High School", 9860, 452, 482, 475,
        2013, "Lester B. Pearson High School", 9865, 504, 530, 512,
        2014, "Lester B. Pearson High School", 9865, 518, 501, 565,
        2015, "Lester B. Pearson High School", 9865, 552, 495, 515,
        2016, "Lester B. Pearson High School", 9865, 459, 512, 564,
        2017, "Lester B. Pearson High School", 9865, 497, 423, 582,
        2018, "Lester B. Pearson High School", 9865, 551, 456, 473,
        2019, "Lester B. Pearson High School", 9865, 535, 528, 553,
        2020, "Lester B. Pearson High School", 9865, 537, 533, 559]


    """Creating ndarray and dictionary"""
    # convert the data in a 2d ndarray, as in the csv file
    all_data = np.array(list).reshape(160, 6)

    # create a dictionary from the 2nd and 3rd column of the data, mapping school name with school code
    all_data_dict = dict(all_data[:, 1:3])

    # change the datatype of values of the dictionary from numpy string to int
    for k in all_data_dict.keys():
        all_data_dict[k] = int(all_data_dict[k])

    # cast the whole array into int, after deleting the school names
    # school names are now not required as dictionary is already created
    all_data = np.delete(all_data, 1, 1).astype('int')


    """Sorting begins"""
    # create a temporary array that will be used for sorting the all_data priming
    # input with string "YYYY CCCCC" because numpy has a weird behavior of treating
    # empty string arrays of one length. More information is at below link
    # https://stackoverflow.com/questions/13717554/weird-behaviour-initializing-a-numpy-array-of-string-data
    sorting_array = np.full((160, 1), "YYYY CCCCC")

    # join the year and school code, to sort the temporary array with year and then school code
    for i in range(160):
        sorting_array[i] = str(all_data[i, 0]) + " " + str(all_data[i, 1])

    # now actually sorting the all_data array
    all_data = all_data[sorting_array[:, 0].argsort()]


    """Making 3D array"""
    # reshape the 2d all_data ndarray into a 3d one
    all_data = all_data.reshape(8, 20, 5)

    return all_data, all_data_dict


if __name__ == '__main__':
    load()
