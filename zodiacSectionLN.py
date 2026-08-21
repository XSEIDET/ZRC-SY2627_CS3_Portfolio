try:
    #Get user input and convert to integer
    year_input = input("Enter your birth year: ")
    birth_year = int(year_input)

    #Validate user input
    if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900")
        
    else:
        #Calculate 12-year cycle remainder
        zodiac_remainder = (birth_year - 1900) % 12
        
        #Selection structure to determine zodiac sign
        if zodiac_remainder == 0:
            zodiac_sign = "Rat (鼠 / Shǔ)"
        elif zodiac_remainder == 1:
            zodiac_sign = "Ox (牛 / Niú)"
        elif zodiac_remainder == 2:
            zodiac_sign = "Tiger (虎 / Hǔ)"
        elif zodiac_remainder == 3:
            zodiac_sign = "Rabbit (兔 / Tù)"
        elif zodiac_remainder == 4:
            zodiac_sign = "Dragon (龙 / Lóng)"
        elif zodiac_remainder == 5:
            zodiac_sign = "Snake (蛇 / Shé)"
        elif zodiac_remainder == 6:
            zodiac_sign = "Horse (马 / Mǎ)"
        elif zodiac_remainder == 7:
            zodiac_sign = "Goat (羊 / Yáng)"
        elif zodiac_remainder == 8:
            zodiac_sign = "Monkey (猴 / Hóu)"
        elif zodiac_remainder == 9:
            zodiac_sign = "Rooster (鸡 / Jī)"
        elif zodiac_remainder == 10:
            zodiac_sign = "Dog (狗 / Gǒu)"
        else:
            zodiac_sign = "Pig (猪 / Zhū)"

        #Output the result
        print(f"Your Chinese Zodiac Sign is : {zodiac_sign}")

except ValueError:
    #Error handling for non-numeric typing errors
    print("Invalid Input! Please enter a valid numerical year.")
