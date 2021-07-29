# turn shoe-data.txt into a list of dicts

# iterate over that list and print each of the dicts out

def line_to_dict(one_line):
    brand, color, size = one_line.strip().split("\t")
    return {"brand": brand,
            "color": color,
            "size": size}


def line_to_dict2(one_line):
    return dict(zip(["brand", "color", "size"],
                    one_line.strip().split("\t")))


shoes = [line_to_dict2(one_line)
         for one_line in open("../00-project-files/shoe-data.txt")]

adidas_shoes = [one_shoe
                for one_shoe in shoes
                if one_shoe["brand"] == "Adidas" and one_shoe["size"] > "40"]

print(adidas_shoes)

# print(shoes[0])
