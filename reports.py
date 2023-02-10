def import_data(filename='booking.txt'):
    """
    Import data from a file to a list. The columns are marked as follows:
    hotel;arrival_date;booked_nights;adults;children;babies;meal;country;reservation_status;reservation_status_date
    Expected returned data format:
        [["Resort Hotel", "01/22/2017", 4, 2, 0, 0, "YES", "PL", "Check-Out", "09/20/2022"],
        ["City Hotel", "01/22/2017", 2, 2, 0, 0, "NO", "FR", "Cancelled", "09/20/2022"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing accomodation booking data
    :rtype: list
    """
    bookings = []
    with open(filename, 'r') as file:
        for line in file:
            booking = line.strip().split(';')
            bookings.append(booking)
    
    return bookings

# print(import_data('booking.txt'))
    


def export_data(bookings, filename='booking.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list booking: booking data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode not in ['a', 'w']:
        raise ValueError('Wrong write mode')
    else:
        with open(filename, mode) as file:
            for booking in bookings:
                file.write(';'.join(booking) + '\n')

# bookings = import_data('booking.txt')
# export_data(bookings, 'booking.txt', 'a')

def get_rows_by_booking_status(rows, status):
    """
    Get booking rows by status

    :param list: booking data
    :param str status: status to filter by e.g. Canceled, Checked-out

    :raises ValueError: if given status is not present in the list. Error message: 'Status is not present in list'
    :returns: all rows of given status
    :rtype: list
    """
    booking_by_status = []
    for booking in rows:
        if booking[8] == status:
            booking_by_status.append(booking)

    if not len(booking_by_status):
        raise ValueError('Status is not present in list')
    else:
        return booking_by_status

    

def get_rows_by_date(rows, date_in, date_out):
    """
    Get rows filtred by specific date

    :param list rows: rows data, date in, date out
    :returns: list of booking in date range betwee date_in and date_out
    :rtype: list
    """
    booking_by_date = []
    for booking in rows:
        if booking[1] >= date_in and booking[1] <= date_out:
            booking_by_date.append(booking)

    return booking_by_date

# rows = import_data('booking.txt')
# print(get_rows_by_date(rows,'08/15/2022','09/18/2022'))

def children_number_in_date(rows, date, hotel):
    """
    Thos method should return amount of children in selected date and specific hotel

    :param list rows: booking data, date, hotel name
    :returns: number of chidren
    :rtype: int
    """
    number_of_children = 0
    for booking in rows:
        if booking[1] == date and booking[0] == hotel:
            number_of_children += int(booking[4])
    
    return number_of_children

rows = import_data('booking.txt')
# print(children_number_in_date(rows, '09/20/2022', 'Resort Hotel'))

def display_reservation(rows, date):
    """
    Method return table representation of reservation in format:

    hotel | check in   | check out  | adults | children | babies | status
    Ibis  | 20/09/2022 | 25/09/2022 | 2      | 0        | 0      | checked-in


    Please get check out date based on arrival_date and booked nights
    """
    lenght = 0
    column_name = ["hotel", "check in","check out","adults","children","babies","status"]
    reservation = []
    for row in rows:
        if row[1] == date:
            reservation.append(row)
        for info in row:
            if len(info) > lenght:
                lenght = len(info)
    
    print(f'{column_name[0].center(lenght)} | {column_name[1].center(lenght)} | {column_name[2].center(lenght)} | {column_name[3].center(lenght)} | {column_name[4].center(lenght)} | {column_name[5].center(lenght)} | {column_name[6].center(lenght)} ')
    for i in reservation:
        print(f'{i[0].center(lenght)} | {i[1].center(lenght)} | {column_name[2].center(lenght)} | {column_name[3].center(lenght)} | {column_name[4].center(lenght)} | {column_name[5].center(lenght)} | {column_name[6].center(lenght)} ')
    pass

# display_reservation(rows, '09/20/2022')