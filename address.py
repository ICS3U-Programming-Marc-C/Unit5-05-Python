#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program format addresses


# Defining the function that format the address
def format_address(
    adressee,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartement_number=None,
):

    formatted = "{}\n{} {}\n{} {} {}".format(
        adressee, street_number, street_name, city, province, postal_code
    )

    formatted_with_apartement_num = "{}\n{} {} {}\n{} {} {}".format(
        adressee,
        street_number,
        apartement_number,
        street_name,
        city,
        province,
        postal_code,
    )

    if apartement_number == None:
        return formatted
    else:
        return formatted_with_apartement_num


if __name__ == "__main__":
    # Getting the user input
    user_adressee = input("Enter a adressee: ")
    user_street_number = input("Enter a street number: ")
    user_apartement_number = input(
        "Enter a apartement number if any. (Press enter to skip this): "
    )
    user_street_name = input("Enter a street name: ")
    user_city = input("Enter a city: ")
    user_province = input(
        "Enter a province (as a abbreviation, EX: ON, AB, BC, QC, ect.) : "
    )
    user_postal_code = input("Enter a postal_code: ")

    formatted_adress = format_address(
        user_adressee,
        user_street_number,
        user_street_name,
        user_city,
        user_province,
        user_postal_code,
        user_apartement_number,
    )
    print("")
    print(formatted_adress)
