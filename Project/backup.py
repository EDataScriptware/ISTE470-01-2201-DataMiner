if fixPriceIndex:
                print('hi')
                if float(data[57]) < 4.99:
                    record += "lower,"
                elif  4.99 <= float(data[57]) and float(data[57]) < 9.99:
                    record += "low,"
                elif 9.99 <= float(data[57]) and float(data[57]) < 19.99:
                    record += "medium,"
                elif 19.99 <= float(data[57]) and float(data[57]) < 49.99:
                    record += "prehigh,"
                else:
                    record += "high,"

                # PriceHigh
                checkErrorTypes(data[57],count)
                if float(data[58]) < 4.99:
                    record += "lower"
                elif  4.99 <= float(data[58]) and float(data[58]) < 9.99:
                    record += "low"
                elif 9.99 <= float(data[58]) and float(data[58]) < 19.99:
                    record += "medium"
                elif 19.99 <= float(data[58]) and float(data[58]) < 49.99:
                    record += "prehigh"
                else:
                    record += "high"