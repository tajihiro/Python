F = 98.6
C = (F - 32) * (5/9)

print('{0:.2f}度'.format(C))


def print_menu():
    print('1: Kilometers to Miles')
    print('2: Miles to Kilometers')

def km_miles():
    km = float(input('Enter distance in Kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0} miles'.format(miles))

def miles_km():
    miles = float(input('Enter distance in Miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0} Km'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()

