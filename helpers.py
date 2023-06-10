import getopt


def get_email(row: dict) -> str:
    try:
        return row["E-postadress"]
    except KeyError:
        raise Exception("Email column is not supported.")

def get_customer_name(row: dict) -> str:
    try:
        return row["Kundnamn"]
    except KeyError:
        raise Exception("Customer name column is not supported.")
    
def get_address(row: dict) -> str:
    try:
        return row["Adress"]
    except KeyError:
        return f"{row['Gatunamn']} {row['Gatunummer']}"
    except:
        raise Exception("Addres column is not supported.")

def get_installation_date(row: dict) -> str:
    try:
        return row["Datum installation"]
    except KeyError:
        raise Exception("Installation date column is not supported.")

def get_kommun(row: dict) -> str:
    try:
        return row["Kommun"]
    except:
        raise Exception("Kommun column is not supported.")

def is_it_test(argv: list) -> bool:
    opts, _ = getopt.getopt(argv, "t")
    try:
        if opts[0][0] == "-t":
            return True
    except IndexError:
        return False

def build_body(
    customer_name: str,
    address: str,
    installation_date: str,
    kommun: str,
) -> str:
    return f"""
        Installation av fiberbox - Open Infra

        Hej {customer_name},

        På uppdrag av Open Infra är vi nu på gång att förbereda fiber till din fastighet!

        För tillfället pågår fiberinstallationer i <strong>{kommun}</strong> och vi önskar installera er fastighet;

        <strong>{address}</strong>

        <strong>{installation_date}</strong>

        <strong>Vänligen bekräfta bokad tid genom att svara på detta mail.</strong>

        <strong>Installation</strong>
        Vid installationen monterar vi två stycken fiberboxar, en på utsidan (fasad box) och en på insidan. Boxarna måste sitta vägg-i-vägg med varandra och den invändiga boxen behöver monteras max en meter ifrån ett eluttag. Installationen tar ca 40 minuter.

        OBS. Se till att ni har förberett en plats inne i fastigheten där fiberboxen ska installeras.

        <strong>Tomtgrävning</strong>
        I samband med installationen projekterar vi tomt grävningen (30 cm schaktdjup) mellan kopplingspunkt och fasad box. Om 30 cm schaktdjup inte kan uppfyllas, kommer fiberkabeln att förläggas i skyddsrör. Vid projektering behöver ni påvisa vart befintliga ledningar (t.ex elektricitet, vatten, avlopp) finns på tomten.

        OBS. Grävning kan komma att ske vid ett senare tillfälle.


        Vid övriga frågor är ni välkomna att kontakta Open Infra på kundtjanst@openinfra.com

        --
        Med Vänliga Hälsningar
        Nik
        BGS Latvia AB
    """