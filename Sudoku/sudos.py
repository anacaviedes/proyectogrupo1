import urllib3
from bs4 import BeautifulSoup


def sudo():
    url = "https://nine.websudoku.com/?"
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    soup = BeautifulSoup(r.data, "html.parser")

    filas = soup.find("div", attrs={"id": "puzzle_container"}).find("table").find_all("tr")

    Sudo = []

    for f in filas:
        celdas = f.find_all("td")
        fila = []
        for c in celdas:
            try:
                val = c.find("input").attrs["value"]
                fila.append(int(val))
            except:
                fila.append(0)
        Sudo.append(fila)
    return Sudo


if __name__ == "__main__":
    Sudokus = []
    for i in range(4):
        sud = []
        for j in range(5):
          sud.append(sudo())
        Sudokus.append(sud)
    print(Sudokus)