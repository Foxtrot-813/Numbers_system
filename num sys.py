while True:
    s = "★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★"
    choice = input("Please choose one of the operations:\n1- Number Systems.\n2- Binary Operations.\n3- Negative "
                   "Decimal to Binary\n4- Quit\n")

    try:
        if choice == '4':
            break

        # Converting Systems.
        elif choice == '1':
            usr_choice = input('Please input the number of the converting systems:'
                               '\n1- Decimal to Binary\n2- Decimal to Hex\n3- Binary to '
                               'Decimal\n4- Binary to Hex\n5- Hex to decimal\n6- Hex to Binary\n7- Back\n8- Quit\n')
            if usr_choice == '8':
                break

            elif usr_choice == '7':
                continue

            elif usr_choice == '1':
                n = input('Please input the number: ')
                try:
                    print(f"{s}\n{bin(int(n)).replace('0b', '')}\n{s}")
                except ValueError:
                    print(f"{s}\nOnly integers allowed.\n{s}")

            elif usr_choice == '2':
                n = int(input('Please input the number: '))
                try:
                    print(f"{s}\n{hex(n).replace('0x', '')}\n{s}")
                except ValueError:
                    print(f"{s}\nOnly integers allowed.\n{s}")

            elif usr_choice == '3':
                n = input('Please input the number: ')
                try:
                    print(f"{s}\n{int(n, 2)}\n{s}")
                except ValueError:
                    print(f"{s}\nOnly 0 and 1 should be given.\n{s}")

            elif usr_choice == '4':
                n = input('Please input the number: ')
                try:
                    # convert binary to decimal
                    dec = int(n, 2)
                    # convert decimal to hexadecimal
                    hex_num = hex(dec)
                    print(f"{s}\n{hex_num.replace('0x', '')}\n{s}")
                except ValueError:
                    print(f"{s}\nOnly 0 and 1 should be given.\n{s}")

            elif usr_choice == '5':
                n = input('Please input the Hex number: ')
                try:
                    print(f"{s}\n{int(n, 16)}\n{s}")
                except ValueError:
                    print(f"{s}\nOnly hexadecimal should be given.\n{s}")

            elif usr_choice == '6':
                n = input('Please input the Hex number: ')
                try:
                    # convert hex to decimal
                    x = int(n, 16)
                    # convert decimal to binary
                    print(f"{s}\n{bin(x).replace('0b', '')}\n{s}")
                except ValueError:
                    print(f"{s}\nOnly hexadecimal should be given.\n{s}")

            else:
                print(f"{s}\nInvalid input.\n{s}")

        # Binary Operations.
        elif choice == '2':
            bin_operations = input("Please choose one of the operations:\n1- Addition.\n2- Subtraction.\n3- "
                                   "Multiplication.\n4- Quit\n")
            if bin_operations == '4':
                break

            elif bin_operations == '1':
                n1, n2 = input("Please input the binary numbers separated with '-': ").split('-')
                print(f"{s}\n{bin(int(n1, 2) + int(n2, 2)).replace('0b', '')}\n{s}")

            elif bin_operations == '2':
                n1, n2 = input("Please input the binary numbers separated with '-': ").split('-')
                print(f"{s}\n{bin(int(n1, 2) - int(n2, 2)).replace('0b', '')}\n{s}")

            elif bin_operations == '3':
                n1, n2 = input("Please input the binary numbers separated with '-': ").split('-')
                print(f"{s}\n{bin(int(n1, 2) * int(n2, 2)).replace('0b', '')}\n{s}")

            else:
                print("Invalid input.")
        elif choice == '3':
            complement_choice = input("Please choose one of the operations:\n1- Signed Magnitude.\n2- One's "
                                      "complement.\n3- Two's complement.\n4- Quit\n")
            if complement_choice == '4':
                break
            elif complement_choice == '1':
                negative_num = int(input("Please input a negative number:\n"))
                if negative_num > 0:
                    negative_num = -negative_num
                else:
                    continue

                def magnitude_complement(num):
                    positive_binary = bin(int(-num)).replace('0b', '')
                    if len(positive_binary) < 8:
                        n = 8 - len(positive_binary) - 1
                        negative_binary = '1' + ('0' * n) + positive_binary
                        return f"{s}\n{negative_binary}\n{s}"
                    elif len(positive_binary) == 8 and positive_binary.startswith('0'):
                        negative_binary = positive_binary[:1].replace('0', '1') + positive_binary[1:]
                        return f"{s}\n{negative_binary}\n{s}"

                print(magnitude_complement(negative_num))

            elif complement_choice == '2':
                pass
            elif complement_choice == '3':
                pass

        else:
            print("Invalid input.")

    except ValueError:
        print(f"{s}\nError, invalid value.\n{s}")
