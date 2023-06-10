import csv
import yagmail
import os
import sys

from enums import (
    TEST_EMAIL,
    SENDED_TXT,
    NOT_SENDED_TXT,
    EMAILS_TO_IGNORE,
    MAIN_EMAIL,
    TOKEN,
)
from helpers import (
    get_email,
    get_customer_name,
    get_address,
    get_installation_date,
    is_it_test,
    build_body,
    get_kommun,
)


def send_emails(argv):
    uniq_recievers = set()
    run_test = is_it_test(argv)
    
    # Removing sended log
    if os.path.isfile(SENDED_TXT):
        os.remove(SENDED_TXT)
        print(f"File {SENDED_TXT} has been removed.")

    # Removing not sended log
    if os.path.isfile(NOT_SENDED_TXT):
        os.remove(NOT_SENDED_TXT)
        print(f"File {NOT_SENDED_TXT} has been removed.")
    
    with yagmail.SMTP(MAIN_EMAIL, TOKEN) as yag:
        with open("table.csv", mode="r") as file:
            csv_reader = csv.DictReader(file)
            line_count = 0

            for row in csv_reader:
                if row['Signerad'] != 'Ja':
                    continue
                
                email = get_email(row)
                customer_name = get_customer_name(row)
                address = get_address(row)
                installation_date = get_installation_date(row)
                kommun = get_kommun(row)

                if email in EMAILS_TO_IGNORE:
                    continue

                reciever = f"{email} {address}"
                
                if reciever in uniq_recievers:
                    continue

                uniq_recievers.add(reciever)

                body = build_body(
                    customer_name,
                    address,
                    installation_date,
                    kommun,
                )

                if not run_test:
                    print("Sending email to customers...")                
                    try:
                        yag.send(f"{email}", 'Fiberinstallation', body)
                        line_count += 1
                    except:
                        with open(f"{NOT_SENDED_TXT}", 'a') as f:
                            # Define the data to be written
                            data = f"{customer_name} {address} {email}"
                            # Use a for loop to write each line of data to the file
                            f.write(data + '\n')
                        continue


                    with open(f"{SENDED_TXT}", 'a') as f:
                        # Define the data to be written
                        data = f"{customer_name} {address} {email}"
                        # Use a for loop to write each line of data to the file
                        f.write(data + '\n')
                
    print(f'Processed {line_count} lines.')
    if run_test:
        yag.send(f'{TEST_EMAIL}', 'Fiberinstallation', body)
        
if __name__ == "__main__":
    send_emails(sys.argv[1:])