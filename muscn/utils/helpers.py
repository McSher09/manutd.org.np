import sys


def insert_row(ws, row, args):
    for i, value in enumerate(args):
        cell = ws.cell(row=row, column=i + 1)
        cell.value = value
    return row + 1


def fix_unicode(st):
    if st:
        try:
            return st.encode('latin1').decode('utf8')
        except UnicodeEncodeError:
            return st
        except UnicodeDecodeError:
            return str(st.encode('utf8'), errors='ignore')


def show_progress(percent):
    percent = int(percent)
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %d%%" % ('=' * percent, percent))
    sys.stdout.flush()
