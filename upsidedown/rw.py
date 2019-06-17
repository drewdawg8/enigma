def write_to_drive(offset, data):
    drive = open('/dev/sdb', 'rb+')
    drive.seek(offset * 512)
    drive.write(data)
    drive.close()

def read_from_drive(offset, size):
    drive = open('/dev/sdb', 'rb+')
    drive.seek(offset*512)
    data = drive.read(size)
    drive.close()
    return data

