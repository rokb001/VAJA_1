# Projetkna naloga 
## SmartTV
Izdelava strežnika ter spletne strani (local host), na katero se lahko povežejo uporabniki istega omrežja. Na spletni strani, ki je hostana na index.html si lahko vsak izbere svojo poljubno video vsebino ter uporabi funkcijo vrnitve nazaj na main page po končanem ogledu.

# Naprave
- Rassberry Pi 4 (4gb)
- Televizija

## Knjižnice 
- express: Uporabljen za ustvarjanje spletnega strežnika.
- path: Zagotavlja pomoč pri oblikovanju poti do datotek.
- morgan: Uporabljen za logging dogodkov strežnika.
- keypress: Omogoča preprosto spremljanje dogodkov na tipkovnici.
- fs: Uporabljen za branje vsebine datotek iz sistema.
- opn: Uporabljen za odpiranje povezav v privzetem spletnem brskalniku

### Kaj lahko pričakujem ko zaženem strežnik in funkcije na spletni strani
Na naslovu loocalhost:8080 se odpre spletna stran modre barve, kjer so predstavljene aktualne funkcije, ki jih spletna stran predstavlja. Zaenkrat so te 3, ob pritisku tipke "q" se ponovno naloži začetna spletna stran, ob pritisku tipke "w" se začne predvajati video o naravi, iz spletnega mesta youtube in ob pritisku tipke "e" se začne predvajati zbirka božičnih pesmi. Ob želji na ponovno izbiro video vsebin pritisni "q" ter ponovno lahko izbereš željene vsebine. 

### Kako zagnati strežnik?
1) Namesti vse potrebne knjižnice
2) V mapi zaženi terminal ter z ukazom node app2.js zaženi localhost.
3) Odpri brskalnik ter v search vpiši localhost:8080
4) Uživaj v gledanju televizije :)

## Možnosti za nadgradnjo
Projekt ima velik potencial za nadrandjo na IR krmiljenje. To lahko omogočimo z vklučitvijo knjižnice LIRC (Linux Infrared Remote Control) in ustreznim IR sprejemnikom. Pazljivi moramo biti, da si ne izberemo zahtevnega IR oddajniko oziroma primeren daljinec (ki ne uporablja naprednega - kodiranega oddajanja).
